# Thực đơn cưới Minh & Thủy

Ứng dụng tiếng Việt cho bố mẹ chọn chung 11 món từ 156 lựa chọn của Seasons · 24/12/2026 · Seasons – Đào Duy Anh.

## Bản đơn giản: một mức ước tính cho mỗi khách

Luồng dùng: **Chọn 11 món → Xem thực đơn và giá/khách → Kiểm tra → Xác nhận lưu.**

Sau khi chọn đủ món, app chỉ hiện một mức như **“Khoảng 660.000đ/khách”**. Bố mẹ không nhập số bàn, số khách, VAT, đồ uống hay phụ thu.

Cách tính tự động, không có ô nhập dự toán:

1. Mỗi món lấy giá của các gói có món đó và tính trung bình. Ví dụ món có ở gói 630.000đ và 770.000đ → mức tham chiếu 700.000đ. Đây là giá gói tham chiếu, không phải giá riêng của món.
2. Cộng 11 mức tham chiếu (mỗi nhóm đúng một lần) rồi chia cho 11.
3. Tạm cộng phí phục vụ 5% và làm tròn đến 10.000đ, hiện một số “Khoảng …đ/khách”.

Món trong nhiều gói được trung bình trong chính nhóm đó, không được đếm nhiều lần làm nhóm đó có trọng số lớn hơn. Cả Cơm tám và các món chung nhiều gói vẫn được tính đúng một trong 11 nhóm. Đổi món sẽ tính lại từ các nguồn gói tương ứng.

Mức này chưa gồm đồ uống, VAT và phụ thu đổi món nếu có. Đây là cách ước lượng theo giá gói nguồn với trọng số ngang nhau cho 11 nhóm, không phải báo giá thực đơn kết hợp từ Seasons. Gói trùng nhiều món nhất chỉ còn là thông tin đối chiếu cho nhà hàng, không quyết định mức dự toán.

## Mở HTML

Mở `index.html` hoặc `Menu_Cuoi_Minh_Thuy.html` bằng Chrome, Edge hoặc Safari. Bản HTML thuần lưu bản nháp và thực đơn đã xác nhận **trên trình duyệt hiện tại**, không tự ghi Google Sheets. Nhãn bản dùng thử luôn cho biết giới hạn này.

Có thể đưa `index.html` lên GitHub Pages để có đường link mở app. Việc lưu dữ liệu trên GitHub Pages vẫn là lưu trên thiết bị; GitHub không tự chạy Apps Script hay biến localStorage thành dữ liệu dùng chung. Backend Google Sheets đi kèm cần được triển khai riêng theo phần dưới.

## Mã nguồn trong repo

| File | Mục đích |
| --- | --- |
| index.html | Toàn bộ ứng dụng trong một file, mở trực tiếp hoặc host tĩnh |
| Code.gs | Backend Apps Script: bảo vệ link, lưu, tải, lịch sử và báo cáo |
| Core.gs | Dữ liệu 156 món và các hàm kiểm tra, tính giá |
| Index.html | Trang mẫu cho Google Apps Script, chú ý chữ I hoa |
| Styles.html | CSS |
| Shared.html | Dữ liệu/hàm dùng ở trình duyệt, sinh từ Core.gs |
| Client.html | Luồng chọn món, xem lại, giá/khách, lưu, sao chép, in |
| appsscript.json | Thiết lập Apps Script |
| menu-data.json | Danh sách món và gói nguồn |
| build_preview.py | Sinh lại Shared.html và HTML độc lập sau khi sửa mã |
| test.cjs | 19 nhóm kiểm thử bằng Node.js, không cần khi dùng app |
| KIEM_THU.md | Phạm vi kiểm thử và phần cần thử với tài khoản Google thật |

Không đưa token truy cập, Google Sheet ID thật hay thông tin đăng nhập vào repo. `setup_` sinh token trong Script Properties của dự án Google, không ghi token vào mã nguồn.

## Triển khai Google Sheets: 10 bước

1. Tạo Google Sheet trống tại https://sheets.google.com, ví dụ “Thực đơn cưới Minh & Thủy”. Giữ quyền chỉnh sửa của Sheet riêng tư.
2. Trong Sheet chọn **Extensions / Tiện ích mở rộng → Apps Script** để mở dự án gắn với bảng tính.
3. Thay `Code.gs` có sẵn bằng mã cùng tên. Bấm **+ → Script**, tạo `Core`, dán `Core.gs`.
4. Bấm **+ → HTML**, tạo `Index`, `Styles`, `Shared`, `Client`, rồi dán nội dung file tương ứng. Trình soạn thảo tự thêm đuôi `.html`. Dùng `Index.html` có chữ I hoa cho Apps Script; không dán file HTML độc lập `index.html` vào đây.
5. Trong **Project Settings**, bật **Show appsscript.json manifest file in editor**. Thay nội dung manifest bằng `appsscript.json` đi kèm. Lưu tất cả file.
6. Chọn hàm `setup_` và bấm **Run**. Kiểm tra đúng dự án tự tạo và cấp quyền Google bằng tài khoản sở hữu Sheet. Hàm tự tạo các tab **THỰC ĐƠN HIỆN TẠI**, **LỊCH SỬ THỰC ĐƠN**, **BÁO GIÁ & DỰ TOÁN**; sinh mã truy cập riêng. Chạy lại trên cùng Sheet không xóa lịch sử hay đổi token.
7. Chọn **Deploy → New deployment → Web app**. Đặt **Execute as: Me**, **Who has access: Anyone** để bố mẹ không cần đăng nhập Google. Nếu tài khoản tổ chức không có lựa chọn này, cần dùng tài khoản phù hợp hoặc nhờ quản trị viên; không thể đảm bảo truy cập ẩn danh dưới chính sách chặn.
8. Sau khi Deploy, chọn hàm `getShareUrl_`, Run, mở **Execution log** và sao chép toàn bộ URL gồm `?token=...`. URL không có token sẽ không mở app. Chỉ gửi link riêng cho gia đình.
9. Thử link trong cửa sổ ẩn danh: chọn đủ 11 món, xem giá/khách, xác nhận lưu. Kiểm tra Sheet có 11 món, ước tính/khách và một dòng lịch sử. Số khách và số bàn phải ghi chưa cung cấp; không được hiểu là 1 khách dự tiệc hay mặc định 200 khách.
10. Mở lại trên điện thoại khác, chọn **Xem thực đơn đã lưu**, đổi một món rồi lưu. Xác nhận lịch sử thêm phiên bản và giữ bản cũ. Sau đó gửi link đầy đủ cho bố mẹ.

Chỉ bạn cần cấp quyền Google để thiết lập. Bố mẹ dùng link không cần cài app, tạo hồ sơ hay tải tài liệu.

## Quyền truy cập và lịch sử

“Execute as me” nghĩa là máy chủ thao tác Sheet bằng quyền của người triển khai. Người có link chứa token có thể xem và sửa thực đơn chung. Token được kiểm tra phía máy chủ khi mở, tải và lưu; không dùng mật khẩu chỉ kiểm tra trong trình duyệt.

Không chia sẻ link công khai hoặc đưa URL chứa token vào repo. Khi cần đổi link, chạy `rotateAccessToken_`, lấy link mới và gửi lại. Link cũ không dùng được nữa.

Backend chỉ nhận ID món hợp lệ đúng nhóm, tự tính lại trung bình giá gói nguồn và ước tính/khách, không tin giá do trình duyệt gửi. Lưu dùng `LockService`, mã yêu cầu chống trùng và kiểm tra phiên bản để tránh ghi đè thay đổi từ thiết bị khác. Lịch sử là nhật ký chỉ thêm mới; hai tab báo cáo có thể dựng lại nếu ghi bị gián đoạn.

## Bản nháp, sửa và lỗi lưu

- Bản nháp ở trên thiết bị; bản đã xác nhận trên Apps Script dùng chung qua Sheet.
- Có bản nháp mới hơn thì trang đầu cho chọn tiếp tục bản nháp hoặc mở bản đã lưu. Mở bản đã lưu sẽ thay nội dung đang mở bằng dữ liệu đã xác nhận.
- Nút **Đổi món** về đúng nhóm; **Xong, xem thực đơn** quay về ngay, giữ nguyên những nhóm khác.
- Lưu thất bại giữ nguyên lựa chọn. Thử lại không cố tình thêm lịch sử trùng.
- Nếu có phiên bản mới hơn từ máy khác, app chặn ghi đè và cho tải bản mới nhất. Không tự ghép hai bản sửa; nên sao chép lựa chọn riêng trước khi tải lại.
- Không xóa, sửa các dòng JSON trong tab lịch sử. Không đổi tên ba tab dữ liệu. Tab báo cáo được tạo tự động; sửa trực tiếp báo cáo không cập nhật dữ liệu chính của app.

## Sao chép và in

**Sao chép thực đơn** lấy danh sách gọn để dán Zalo/Messenger. **Sao chép yêu cầu báo giá** thêm gói gần nhất, các món khác gói và yêu cầu Seasons xác nhận giá/khách, phụ thu, đồ uống, phí phục vụ, VAT. Không tự gửi tin nhắn.

**In / lưu PDF** chỉ in thông tin cưới và 11 món; không có giá, gói hay nút bấm. Nếu clipboard bị chặn, app hiện ô chữ để chọn và sao chép thủ công.

## Cập nhật mã

Sau khi sửa `Core.gs`, `Styles.html`, `Client.html` hoặc `Index.html`, chạy:

```sh
python3 build_preview.py
node test.cjs
```

Đưa cả `Core.gs` và `Shared.html` mới vào Apps Script khi thay dữ liệu/hàm dùng chung. Chọn **Deploy → Manage deployments → Edit → New version → Deploy** để cập nhật cùng link. Giữ nguyên ID món và tên tab để tương thích lịch sử.

Bản cũ có dự toán toàn tiệc vẫn đọc được ở backend để giữ lịch sử. Giao diện mới chỉ tính giá/khách và không hỏi thông tin tài chính cũ.

## Giới hạn kiểm thử

Đã kiểm thử 19 nhóm logic, lưu/tải backend bằng mô hình dịch vụ Apps Script và luồng HTML trong trình duyệt ở 360, 375, 390, 430, 768px. Chưa cấp quyền, triển khai hoặc kiểm thử với Google Sheet thật của bạn. Cần thực hiện bước 9–10 trước khi gửi link Apps Script cho bố mẹ. Bản HTML không được gọi là đã kết nối Google Sheets.

Tài liệu Google: https://developers.google.com/apps-script/guides/web · https://developers.google.com/apps-script/guides/html/communication · https://developers.google.com/apps-script/reference/lock/lock-service
