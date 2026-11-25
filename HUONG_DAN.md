# Thực đơn cưới Minh & Thủy

Ứng dụng tiếng Việt trên điện thoại, giúp bố mẹ chọn chung 11 món từ 156 lựa chọn của Seasons. Ngày cưới 24/12/2026, Seasons – Đào Duy Anh.

Luồng sử dụng: Chọn món → Xem thực đơn và một giá tham khảo/khách → Xác nhận → Lưu trên thiết bị.

Không có ô nhập dự toán hay phần giải thích cách tính trong giao diện. Có thể đổi riêng từng món, sao chép thực đơn/yêu cầu báo giá, in hoặc lưu PDF. Bản in chỉ có thông tin cưới và 11 món.

## Mở ứng dụng

Mở `index.html` bằng trình duyệt hoặc host file này trên GitHub Pages. Không cần cài thư viện, đăng nhập hay kết nối dịch vụ bên ngoài. Font trực tuyến có font hệ thống thay thế.

Lựa chọn và bản đã xác nhận được lưu trong localStorage của trình duyệt hiện tại. Các thiết bị không tự đồng bộ. Dữ liệu cũ trong trình duyệt được tiếp tục nhận diện. Không xóa dữ liệu trình duyệt nếu muốn giữ thực đơn.

## Mã nguồn

- `Index.html`: trang mẫu để sửa bố cục.
- `Styles.html`: giao diện.
- `core.js`: dữ liệu món và quy tắc ước tính nội bộ.
- `Client.html`: chọn món, xem lại, sao chép, in và lưu trên thiết bị.
- `index.html`: ứng dụng hoàn chỉnh trong một file, được sinh từ các file trên.
- `build_preview.py`: sinh lại file hoàn chỉnh.
- `test.cjs`: kiểm tra dữ liệu, giá và luồng lưu/tải trên thiết bị.

Sau khi sửa mã:

```sh
python3 build_preview.py
node test.cjs
```

## Thiết lập nội bộ dành cho người duy trì

Mức tham chiếu của mỗi món là trung bình giá các gói có món đó. Trung bình 11 mức tham chiếu cho ra giá nền. Ước tính hiển thị = giá nền × 1,05 + 100.000đ/khách, làm tròn đến 10.000đ.

Khoản đồ uống 1.000.000đ được **tạm hiểu là mỗi bàn 10 người**, tương đương 100.000đ/khách. Đây là giả định cần chủ tiệc kiểm tra lại. Các hằng số nằm trong `ESTIMATE_SETTINGS` của `core.js`: `serviceRate`, `drinksPerTable`, `guestsPerTable`, `rounding`.

Quy tắc tính chỉ nằm trong mã và tài liệu duy trì, không xuất hiện trên giao diện hoặc nội dung sao chép cho người dùng. Giá là ước tính tham khảo; Seasons xác nhận báo giá thực đơn kết hợp.

## Kiểm tra

11 kiểm tra tự động: đủ 156 món/11 nhóm; Cơm tám chọn sẵn; tính đúng giá nền và phần cộng thêm; không nhân đôi món nhiều gói; đổi món cập nhật giá; chặn dữ liệu sai; HTML khớp nguồn; chọn/xem đủ 11 món; lưu và tải lại; nhận dữ liệu cũ; lưu thất bại giữ lựa chọn.

Kiểm thử luồng sử dụng qua mô hình trình duyệt trong Node.js. Chưa kiểm tra lại trên điện thoại vật lý.
