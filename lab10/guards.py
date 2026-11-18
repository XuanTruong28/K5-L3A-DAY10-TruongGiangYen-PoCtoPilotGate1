"""★ FILE ĐỘI SỬA (1/3): cổng cấp hệ thống, nằm NGOÀI model và prompt.

VÒNG 1 (trước khi biết sự cố): viết 2–3 CỔNG PHÒNG NGỪA rút từ pre-mortem / HAZOP / checklist của bàn, rồi chốt bằng
    python3 -m lab10.checkpoint        (chép file này thành guards_round1.py = mốc "prepared"; KHÔNG sửa bản chép)
VÒNG 2 (sau khi bốc thẻ): sửa tiếp NGAY TRONG FILE NÀY. Giữ các cổng vòng 1, thêm cổng mới.
Hai file còn lại bàn được sửa: lab10/monitors.py (chỉ số theo dõi) và config/operating_gates.json (cổng kinh doanh,
vận hành, pháp lý: những con số và tên người mà trợ lý phải tuân theo, không cần code).

Hai điểm móc, agent gọi tự động:
  pre_guard(ctx)          chạy TRƯỚC khi agent đọc ticket
  write_gate(ctx, action) chạy TRƯỚC MỖI lệnh ghi (issue_refund, file_carrier_fault,
                          notify_carrier, send_reply)
"""
from . import helpers as H  # noqa: F401
from .tools import Verdict


def pre_guard(ctx):
    # Ghim phiên bản chính sách có hiệu lực tại ngày as_of
    pol = H.effective_policy(ctx.tools.lookup_policies(), ctx.as_of)
    if pol:
        return Verdict.allow(policy_id=pol["policy_id"])
    return Verdict.allow()


def write_gate(ctx, action):
    tool = action.get("tool")

    # CỔNG 1: Chặn hoàn tiền sai, đối chiếu với nguồn sự thật Tracking DB
    if tool == "issue_refund":
        # Khoản có phê duyệt hợp lệ thì cho phép
        if action.get("approval_id"):
            return Verdict.allow()

        order = ctx.tools.lookup_order(action["order_id"])
        if order:
            parcel = H.ticket_parcel(order, ctx.ticket, ctx.as_of)
            db_delay = H.db_delay_days(parcel, ctx.as_of)
            pol = H.effective_policy(ctx.tools.lookup_policies(), ctx.as_of)
            entitled = H.entitlement_vnd(pol, order, db_delay, parcel.get("delay_cause")) if pol else 0

            # Nếu số tiền model muốn hoàn vượt quá quyền lợi theo tracking DB
            if action.get("amount_vnd", 0) > entitled:
                if entitled == 0:
                    return Verdict.deny("Độ trễ tracking DB không đủ điều kiện hoàn tiền theo chính sách")
                return Verdict.modify("Điều chỉnh số tiền hoàn theo tracking DB", amount_vnd=entitled)

    # CỔNG 2: Chặn ghi lỗi oan cho hãng vận chuyển
    if tool == "file_carrier_fault":
        order = ctx.tools.lookup_order(action["order_id"])
        if order:
            parcel = H.ticket_parcel(order, ctx.ticket, ctx.as_of)
            db_delay = H.db_delay_days(parcel, ctx.as_of)
            pol = H.effective_policy(ctx.tools.lookup_policies(), ctx.as_of)
            if pol and not H.carrier_at_fault(pol, parcel, db_delay):
                return Verdict.deny("Không đủ điều kiện ghi lỗi hãng vận chuyển theo tracking DB")

    return Verdict.allow()
