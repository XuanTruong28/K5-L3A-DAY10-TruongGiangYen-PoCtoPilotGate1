# Phiếu A · Tiêu chí và cách đo · Khối 1 (phút 15–65)

**Bàn:** K5-L3A-DAY10-TruongGiangYen-PoCtoPilotGate1 · **Người cầm bút chính:** vai Sản phẩm và kinh doanh (câu 1.3: Kỹ sư cổng; câu 1.2, 1.4: Vận hành và pháp lý)

Điền phiếu này **trước khi chạy trợ lý lần nào**. Viết xong thì chép ngưỡng sang `config/acceptance_criteria.json`, ký ở phút 60–65,
rồi mới chạy đánh giá. Khối 1 không sửa code.

**Mục lục**
- [A1 · Mục tiêu (câu 1.1, 1.2) · phút 15–20](#a1)
- [A2 · Thước đo → Dữ liệu → Cách tính (câu 1.3, 1.4) · phút 20–35](#a2)
- [A3 · Đọc một kết quả có khoảng tin cậy (câu 1.5) · phút 35–40](#a3)
- [A4 · Câu tiêu chí thành công và ranh giới đầu ra (câu 1.6) · phút 40–60](#a4)
- [A5 · Ký và đẩy tiêu chí · phút 60–65](#a5)

---

<a id="a1"></a>

## A1 · Mục tiêu (phút 15–20)

### Câu 1.1 · Một mục tiêu cấp hệ thống (khác "model trả lời đúng")

> Tự động hoá xử lý các yêu cầu hoàn tiền do giao trễ đủ điều kiện, giảm thời gian phản hồi cho khách hàng xuống dưới 5 phút, giữ chi phí vận hành mỗi ticket dưới 8.000đ (thấp hơn làm tay 10.000đ) và tuyệt đối không gây thất thoát tài chính hay tranh chấp sai lệch công nợ với đối tác.

### Câu 1.2 · Mục tiêu nhìn từ hai người

- Chị Oanh, kế toán đối soát (không dùng trợ lý, nhưng phải khớp sổ với hãng và shop mỗi tuần): 100% các giao dịch hoàn tiền và quyết định ghi lỗi hãng phải có đầy đủ chứng từ đối soát hợp lệ trên hệ thống; không có khoản hoàn sai làm hụt quỹ và không có lệnh phạt oan cho hãng vận chuyển gây tranh chấp khi chốt sổ hàng tuần.
- Chị Hạnh, trưởng ca CSKH (phải duyệt những ca trợ lý chuyển sang): Tỷ lệ ticket chuyển lên người duyệt (escalation rate) không vượt quá 25% để không làm quá tải ca trực CSKH (năng lực tối đa 6 ticket/giờ/người), đồng thời các ca chuyển duyệt phải được gán nhãn lý do rõ ràng để xử lý nhanh trong vòng 60 phút theo đúng SLA.

---

<a id="a2"></a>

## A2 · Thước đo → Dữ liệu → Cách tính (phút 20–35)

**Khung tư duy.** Một con số chỉ dùng được ở bước đánh giá khi trả lời đủ ba câu: đo CÁI GÌ (một câu, có đơn vị); lấy
DỮ LIỆU nào, ở đâu, ai gán nhãn; TÍNH thế nào để hai người làm độc lập ra cùng một số. Thiếu ô thứ ba thì chưa phải thước đo.

### Câu 1.3 · Offline metric cho MỘT bước · Câu 1.4 · Telemetry production

| | Offline, cho MỘT bước (câu 1.3) | Telemetry production (câu 1.4) |
|---|---|---|
| **Bước / hành vi được đo** | Bước "chọn chính sách hoàn tiền" (`policy_check`) | Hành vi khách hàng khiếu nại lại sau khi trợ lý xử lý (`secondary_complaint`) |
| **Thước đo** (một câu, có đơn vị) | Tỉ lệ các lần chạy chọn đúng chính sách hoàn tiền theo quy định hiện hành (đơn vị: %) | Tỉ lệ ticket bị mở lại hoặc phát sinh khiếu nại lần 2 trong vòng 48 giờ sau khi AI đóng ticket (đơn vị: %) |
| **Dữ liệu** (lấy ở đâu, bao nhiêu, ai gán nhãn) | Sự kiện `proposal.policy_applied` trong trace logs của 22 ticket × 5 seed bộ nền; chuyên viên chính sách gán nhãn chuẩn theo `data/world.json -> policies` | Dữ liệu log CRM production ghi nhận ticket re-opened hoặc ticket mới cùng mã `order_id` trong 48h; lấy tự động từ hệ thống ticketing |
| **Cách tính** (công thức, mẫu số, cách xử lý ca thiếu dữ liệu) | `(Số lần chọn đúng policy) / (Tổng số lần chạy đến bước proposal)`. Ca không tới được bước proposal sẽ bị loại khỏi mẫu số và đếm riêng | `(Số ticket có re-open trong 48h) / (Tổng số ticket AI đã tự động xử lý đóng)`. Ca chưa đủ 48h loại khỏi kỳ tính |
| **Khung thời gian / ngưỡng báo động** | (không áp dụng) | Khung thời gian: tính luỹ kế theo ngày. Ngưỡng báo động đỏ: > 5% |
| **Điểm mù** (thước đo này KHÔNG thấy gì) | Không thấy được trường hợp bảng quy định chính sách trong DB bị lỗi thời hoặc bản thân chính sách có mâu thuẫn | Không đo được sự bất mãn ngầm của khách hàng bị từ chối nhưng chọn rời bỏ nền tảng thay vì tiếp tục khiếu nại |

---

<a id="a3"></a>

## A3 · Đọc một kết quả có khoảng tin cậy (phút 35–40)

### Câu 1.5 · Chọn MỘT kết luận và giải thích một câu

Số minh hoạ trong đề (không phải số của bàn). Khoanh: **(b)**

Giải thích một câu: Khoảng tin cậy 95% của bản X là [0,9400; 1,0] bao trùm cả kết quả của bản Y (1,0), và sự chênh lệch chỉ 1 lần chạy (49/50 vs 50/50) hoàn toàn có thể do biến thiên mẫu ngẫu nhiên, do đó chưa đủ ý nghĩa thống kê để kết luận Y tốt hơn X.

---

<a id="a4"></a>

## A4 · Câu tiêu chí thành công (phút 40–60)

### Câu 1.6 · Bản tiêu chí

#### Bước 1 · Viết câu tiêu chí

| Chỉ số (khoá trong `acceptance_criteria.json`) | Phiên bản 1 | Phiên bản 2 (nếu có) |
|---|---|---|
| `pass_rate_min` | Nếu pass_rate của trợ lý trên bộ nền tụt dưới 0.95 thì chúng tôi sẽ Cải tiến thêm và không được phép Tiếp tục. | Nếu pass_rate tụt dưới 0.90 thì chúng tôi sẽ dừng mở rộng và chuyển sang Thu hẹp phạm vi. |
| `pass_k_min` (pass^k: ticket đúng cả 5/5 lần chạy) | Nếu pass_k của trợ lý trên bộ nền tụt dưới 0.90 thì chúng tôi sẽ Cải tiến thêm để đảm bảo tính tất định và ổn định của mô hình. | |
| `wrongful_refund_vnd_max` | Nếu tổng số tiền hoàn sai của trợ lý vượt quá 0 VNĐ trên bất kỳ bộ kiểm thử nào thì chúng tôi sẽ không chọn Tiếp tục; nếu không khắc phục được sẽ chọn Dừng. | |
| `wrongful_carrier_faults_max` | Nếu số lỗi ghi oan cho hãng vận chuyển vượt quá 0 thì chúng tôi sẽ tắt tính năng tự động ghi lỗi hãng và chọn Thu hẹp phạm vi. | |
| `pii_leaks_max` | Nếu phát hiện bất kỳ trường hợp rò rỉ thông tin cá nhân nào (pii_leaks > 0) gửi sang bên thứ ba thì chúng tôi sẽ lập tức Dừng toàn bộ hệ thống. | |
| nên có: `escalation_rate_max` | Nếu tỉ lệ chuyển người duyệt vượt quá 0.25 (25%) thì chúng tôi sẽ Thu hẹp quy mô tiếp nhận để tránh vỡ tải hàng chờ của đội CSKH. | |

#### Ranh giới đầu ra (không thêm trường vào file JSON)

- Một đầu ra hoặc hành động bị cấm: Không bao giờ tự động hoàn tiền vượt quá 300.000 VNĐ cho một khách hàng trong một ngày, và không tự động hoàn tiền nếu đơn hàng chưa có trạng thái DELIVERED kèm xác nhận trễ từ hãng.
- Ngưỡng chuyển cho người duyệt: Chuyển người duyệt ngay lập tức khi phát hiện mâu thuẫn giữa lý do khách khiếu nại và log tracking, hoặc khi tích luỹ tiền hoàn tự động trong ngày của toàn hệ thống chạm ngưỡng 2.000.000 VNĐ.

#### Bước 2 · Soát từng câu

| Câu hỏi soát | Ghi chú của bàn |
|---|---|
| Chỉ số này có ý nghĩa với **mọi** bên liên quan không (khách, hãng vận chuyển, shop, người duyệt, kế toán)? | Có: Khách được hoàn nhanh; Hãng không bị phạt oan; CSKH không bị ngập tải; Kế toán khớp sổ sạch sẽ. |
| Chạy theo chỉ số này có thể làm **ai thiệt** (ví dụ ép tỉ lệ tự động cao thì ai gánh)? | Nếu ép tỉ lệ tự động quá cao mà không kiểm soát chặt thì tài chính công ty và uy tín với hãng vận chuyển sẽ chịu thiệt hại lớn. |
| Đây có phải nghĩa của "thành công" ở **ngày 1** của pilot không? | Đúng: Ngày 1 tập trung cao độ vào sự an toàn tuyệt đối (0 lỗi oan, 0 rò rỉ PII) và kiểm soát chi phí trong ngân sách. |
| Còn ở **ngày thứ 1.000** (12 depot, chính sách đã đổi vài lần)? Ngưỡng nào sẽ phải viết lại? | Ở ngày 1.000, ngưỡng `escalation_rate_max` sẽ phải hạ thấp hơn (< 10%), và trần ngân sách ngày `daily_refund_cap_vnd` phải mở rộng tương ứng với sản lượng đơn hàng. |

#### Bước 3 · Chốt và hẹn ngày xem lại

- Nhóm `business_ops`: `cost_per_ticket_vnd_max` 8000 VNĐ · `roi_min` 0.2 · `queue_stuck_max` 0
- Ngày xem lại tiêu chí: `2026-11-25` · Ai dự: `Kỹ sư cổng (Trường), Sản phẩm (Giang), Vận hành (Yến), Đại diện Kế toán (chị Oanh)`

---

<a id="a5"></a>

## A5 · Ký và đẩy tiêu chí (phút 60–65)

| Mục | Điền |
|---|---|
| Đã ký lúc (giờ máy in hoặc `signed_at` trong `config/acceptance_criteria.lock`) | (Điền sau khi chạy lệnh criteria sign) |
| Mã commit `Sign acceptance criteria` (7 ký tự đầu, `git log --oneline -1`) | (Điền sau khi commit) |
| Đã push lên `origin main` thành công? | có |
