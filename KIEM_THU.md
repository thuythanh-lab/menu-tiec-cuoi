# Phạm vi kiểm thử

Ngày 21/11/2026. Kết quả áp dụng bản mã nguồn đi kèm.

## Kiểm thử tự động: đạt 19 nhóm

Chạy `node test.cjs` (Node.js có sẵn trên máy phát triển; không cần khi triển khai Apps Script).

1. Đủ 11 nhóm, 156 ID duy nhất, dữ liệu và liên kết gói khớp bảng nguồn.
2. Cơm tám chọn sẵn; từ chối thiếu nhóm, sai nhóm và nhóm dư.
3. Đếm món nhiều gói và chọn gói giá mẫu thấp hơn khi đồng hạng.
4. 200 khách, gói 630.000đ + 5% = 132.300.000đ; các khoản chưa biết vẫn chờ.
5. Số khách trực tiếp thay số khách theo bàn; số 0 xác nhận khác chưa báo giá.
6. Báo giá tiền ăn Seasons thay giá gói và phụ thu, không cộng hai lần.
7. Cơ sở phí phục vụ trên ăn/ăn + uống và VAT phải xác nhận trước khi tính.
8. Từ chối NaN, số âm, số khách phân số, mã gói/cơ sở không hợp lệ và giá tiền ăn bằng 0.
9. Máy chủ từ chối token sai và ID món bị giả.
10. Lưu 11 món, dữ liệu dự toán, lịch sử và tải lại trong mô hình dịch vụ Google.
11. Cùng mã yêu cầu không thêm phiên bản trùng; thay nội dung cùng mã bị từ chối.
12. Xung đột phiên bản bị chặn; xác nhận sửa đổi thêm dòng lịch sử.
13. Giả lập lỗi ghi báo cáo sau khi đã ghi lịch sử; thử lại phục hồi, không thêm lịch sử trùng.
14. Chuỗi có thể là công thức được escape trước khi ghi các ô văn bản báo cáo.

15. Bộ 11 món đầu tiên: tổng 11 mức tham chiếu 6.452.500đ; trung bình 586.590,91đ; cộng 5% thành 615.920đ, hiển thị khoảng 620.000đ/khách.
16. Thay súp bằng món thuộc gói 690/770: mức tham chiếu súp 730.000đ, dự toán thành khoảng 630.000đ/khách. Món nhiều gói vẫn chỉ chiếm một nhóm, không có trọng số cao hơn.
17. Chế độ mỗi khách không giả định số khách, số bàn, VAT hay tổng toàn tiệc.
18. Backend tính lại trung bình từ ID món; bỏ qua giá tham chiếu/giá trung bình tùy ý phía trình duyệt.
19. Lưu đủ 11 món, giá/khách mới, thông tin số khách chưa cung cấp và tải lại đúng.

Mã JavaScript frontend cũng được kiểm tra cú pháp.

## Bản mới: giao diện chỉ hiện giá/khách

Đã kiểm tra lại ở 360, 375, 390, 430, 768px: không cuộn ngang; đúng một khung ước tính cho mỗi khách; không có ô nhập tài chính. Xem đủ 11 món, xác nhận bản HTML, tải lại và mở bản đã lưu giữ nguyên giá/khách.

Các kiểm tra dưới đây từ bản trước được giữ để ghi nhận tính tương thích của bộ dữ liệu và backend cũ. Giao diện dự toán toàn tiệc đã được thay bằng một mức giá/khách.

## Kiểm thử giao diện bản trước bằng trình duyệt

Đã thực hiện trong bản dùng thử, không dùng Google thật:

- Màn hình 360, 375, 390, 430 và 768px qua khung nhìn cùng chiều rộng, với scrollbar mặc định của Chrome. `scrollWidth` bằng `clientWidth` trên màn hình chọn món và dự toán; không cuộn ngang. Không phải thử trên iPhone/Android vật lý.
- Thẻ món có chiều cao tối thiểu khoảng 146px trong màn hình kiểm tra; nút dưới cùng tối thiểu 52px, tăng chiều cao khi chữ xuống dòng.
- Chọn món có nhiều gói, trạng thái đã chọn rõ và chỉ một lựa chọn mỗi nhóm.
- Tải lại trang, tiếp tục bản nháp và giữ món đã chọn.
- Đi qua đủ 11 nhóm, gồm Cơm tám đã chọn sẵn; xem đủ 11 món theo đúng thứ tự.
- Đổi riêng món cá ở trang xem lại; đối chiếu 11 món trước/sau chỉ thay đúng một món.
- Chuyển gói tham khảo thủ công sang Tiêu chuẩn; tổng 200 khách là 132.300.000đ.
- Nhập 250 khách trực tiếp; tổng tăng ngay thành 165.375.000đ.
- Nhập báo giá Seasons 700.000đ/khách: 250 khách + 5% = 183.750.000đ. Nhập VAT 8% chỉ cho ví dụ thử và xác nhận cơ sở ăn + uống + phục vụ: 198.450.000đ. Đây là số kiểm thử, không được dùng làm VAT mặc định hoặc báo giá thực tế.
- Xác nhận bản dùng thử, tải lại và mở thực đơn đã lưu đủ 11 món.
- Sao chép thực đơn; đọc clipboard đối chiếu có ngày, địa điểm và món đã chọn.
- Bản dùng thử luôn có nhãn chưa kết nối Google Sheets.

## Cần kiểm thử trong tài khoản của bạn

Chưa thể xác nhận các việc sau từ môi trường hiện tại:

- Chấp thuận quyền Google, triển khai HTML Service và mở app không cần đăng nhập.
- Lưu/tải thật qua `google.script.run` vào Google Sheets, định dạng tab và lịch sử thật.
- Cạnh tranh ghi giữa hai phiên Google thật và retry sau gián đoạn mạng thật.
- In PDF từ trình duyệt điện thoại; font, bàn phím, safe-area và thanh công cụ trên thiết bị iPhone/Android thật.

Checklist sau khi triển khai: mở ẩn danh bằng link chứa token → chọn 11 món → lưu → kiểm tra 3 tab → mở trên máy thứ hai → đổi một món → lưu lại → kiểm tra lịch sử tăng đúng 1 phiên bản → không chia sẻ link công khai.
