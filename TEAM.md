# Team

## Thông tin nhóm

- Tên nhóm (`TenNhom`, không dấu, không khoảng trắng): TruongGiangYen
- Lớp: `L3A`
- Repo của bàn: `K5-L3A-DAY10-TruongGiangYen-PoCtoPilotGate1`
- Thẻ sự cố đã bốc (S1–S8):

## Thành viên

Họ tên đầy đủ và MSSV của **mọi** thành viên; thêm dòng nếu cần. Vai: Kỹ sư cổng · Sản phẩm và kinh doanh · Vận hành và pháp lý (README mục 3, phút 0–15).

| STT | Họ và tên | MSSV | Vai | Trưởng nhóm |
| --: | --------- | ---- | --- | :---------: |
|   1 | Trần Xuân Trường | 2A202603617 | Kỹ sư cổng | X |
|   2 |  Nguyễn Thị Hải Yến | 2A202603567 | Sản phẩm và kinh doanh | |
|   3 |  Nguyễn Thị Hương Giang | 2A202603538 | Vận hành và pháp lý | |

Ghi `members` trong `submission/submission.json` theo dạng `"HoVaTen-MSSV"`, khớp bảng trên.

## Cá nhân

Mỗi thành viên tự viết một mục bên dưới (chép mẫu, đổi tiêu đề thành họ tên không dấu và MSSV, ví dụ `## NguyenVanAn-20241234`).

## TranXuanTruong-2A202603617

### Phần việc phụ trách
- Vai: Kỹ sư cổng (Trưởng nhóm).
- Phụ trách quản trị Git repo, cấu hình môi trường, chạy các lệnh lab (`criteria sign`, `eval`, `gate`, `checkpoint`, `grade`, `check_submission`).
- Kỹ thuật: Viết code cổng trong `lab10/guards.py`, kiểm thử `--adhoc` độc lập, làm các mục kỹ thuật trong Phiếu A (Câu 1.3, 1.5), Phiếu B (B0, B1, B2, B7.1–B7.3).
- Đại diện nhóm tổng hợp toàn bộ nội dung từ các thành viên và thực hiện commit/push lên Git để đảm bảo an toàn mã hash và tránh xung đột.

### Đóng góp cụ thể
- Thiết kế và triển khai 3 cổng bảo vệ cấp hệ thống trong `guards.py`: ép đối chiếu ngày trễ với Tracking DB, chặn hoàn sai, chặn phạt oan hãng VNX và ghim phiên bản chính sách.
- Đưa kết quả đánh giá vòng 1 mốc `prepared` lên mức tuyệt đối: pass_rate 1.0 (110/110), pass_k 1.0, hoàn sai 0đ, lỗi hãng oan 0.
- Thực hiện chốt cổng vòng 1 (`lab10.checkpoint`) với mã hash `59d6ce2a`.

### Bằng chứng
- Mã commit: `364acc4` (Sign criteria), `85272cc` (Chốt cổng vòng 1 v1).
- Mã lần chạy: `R-base-before-20261118-144927-bde05c`, `R-base-prepared-20261118-152504-2b3245`.
- Dòng mục trong phiếu: A2 (câu 1.3), A3 (câu 1.5), B0, B1, B2, B7.1, B7.2, B7.3.

### Exit ticket
- Một điều học được: Cổng bảo vệ cấp hệ thống (system-level guard) can thiệp trực tiếp vào lệnh ghi hiệu quả và tin cậy hơn nhiều so với việc chỉ trông cậy vào prompt hay model.
- Một điều còn chưa chắc: Cách thức tối ưu để đồng bộ dữ liệu khi tracking của các hãng vận chuyển khác nhau bị trễ không đồng đều.

---

## NguyenThiHaiYen-2A202603567

### Phần việc phụ trách
- Vai: Sản phẩm và kinh doanh.
- Phụ trách phân tích mục tiêu kinh doanh, thiết kế bản tiêu chí nghiệm thu và hiệu quả tài chính.
- Điền Phiếu A (Câu 1.1 Mục tiêu hệ thống, Câu 1.6 Bản tiêu chí), Phiếu B (mục B3 Bản đồ dữ liệu & data drift, mục B7.4 Cổng kinh doanh), cùng chốt Quyết định v1 (B8).
- Soạn nội dung và chuyển cho Trưởng nhóm commit vào repo chung.

### Đóng góp cụ thể
- Xây dựng Bản tiêu chí nghiệm thu và 4 quy tắc quyết định Gate 1 khớp với thực tế vận hành LogiX-VN.
- Xác định và cấu hình các thông số kinh doanh trong `config/operating_gates.json`: trần ngân sách hoàn tự động 2.000.000đ/ngày, trần LLM 1.500đ/ticket, ROI mục tiêu ≥ 0.2 (thực tế đạt 1.38).
- Phân tích bản đồ dữ liệu và kịch bản data drift dịp Tết Nguyên Đán.

### Bằng chứng
- Dòng mục trong phiếu: A1 (câu 1.1), A4 (câu 1.6), B3, B7.4, B8.
- Cấu hình kinh doanh trong `config/operating_gates.json` mục `business`.

### Exit ticket
- Một điều học được: Trước khi đưa AI vào vận hành thật (Pilot), bắt buộc phải có trần tài chính và quy tắc dừng rõ ràng để tránh rủi ro tài chính cho doanh nghiệp.
- Một điều còn chưa chắc: Làm thế nào để ước tính chính xác chi phí LLM khi độ dài tin nhắn khiếu nại của khách hàng biến động lớn.

---

## NguyenThiHuongGiang-2A202603538

### Phần việc phụ trách
- Vai: Vận hành và pháp lý.
- Phụ trách phân tích rủi ro hệ thống, bảo vệ dữ liệu cá nhân (PII), quy trình CSKH và kịch bản trực ca.
- Điền Phiếu A (Câu 1.2 Góc nhìn Kế toán & CSKH, Câu 1.4 Telemetry production), Phiếu B (mục B4 HAZOP vòng 1, mục B5 Checklist 9 việc go-live, mục B7.5 & B7.6 Soạn Runbook 1–3 và Giờ cao điểm).
- Soạn nội dung và chuyển cho Trưởng nhóm commit vào repo chung.

### Đóng góp cụ thể
- Lập bảng phân tích rủi ro HAZOP toàn diện (gồm cả kỹ thuật và mở rộng ngoài kỹ thuật cho người duyệt và ngân sách).
- Hoàn thành checklist 9 nhóm việc go-live có gắn tên người chịu trách nhiệm (PIC) cụ thể.
- Xây dựng Runbook trực ca CSKH chi tiết với 3 ngưỡng tín hiệu (Bình thường, Vàng, Đỏ) và phương án ứng phó giờ cao điểm cho đội ngũ vận hành.

### Bằng chứng
- Dòng mục trong phiếu: A1 (câu 1.2), A2 (câu 1.4), B4, B5, B7.5, B7.6.
- Cấu hình vận hành và pháp lý trong `config/operating_gates.json` mục `operations` và `legal`.

### Exit ticket
- Một điều học được: Tầm quan trọng của Runbook thực tế và điều kiện dừng khẩn cấp để nhân viên trực ca biết chính xác phải làm gì khi hệ thống gặp lỗi vào ban đêm.
- Một điều còn chưa chắc: Tỷ lệ lấy mẫu kiểm tra thủ công (review sampling) bao nhiêu % là tối ưu để cân bằng giữa chi phí nhân sự và độ an toàn.
