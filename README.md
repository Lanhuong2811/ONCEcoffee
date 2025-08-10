# ONCE Specialty Coffee & Roastery

#### Video Demo:  [https://youtu.be/kbsSKE9HVv0](https://youtu.be/kbsSKE9HVv0)

#### Description:

#### Description:

ONCE Specialty Coffee & Roastery là một website thương mại điện tử được xây dựng để đại diện cho thương hiệu cà phê đặc sản mang phong cách trẻ trung, sáng tạo và mang tính nghệ thuật. Dự án này được phát triển trong khuôn khổ bài Final Project của CS50, với mục tiêu tạo nên một nền tảng thân thiện với người dùng, tích hợp đầy đủ chức năng bán hàng trực tuyến cơ bản như duyệt sản phẩm, giỏ hàng, đăng ký người dùng và thanh toán (giả lập).

Website được xây dựng bằng Python và Flask, với các template HTML sử dụng Jinja2, cùng với CSS và JavaScript để đảm bảo giao diện đẹp, mượt mà và responsive. Ngoài ra, thư viện SwiperJS được tích hợp để tạo hiệu ứng slider cho phần sản phẩm, góp phần tăng tính thẩm mỹ và trải nghiệm người dùng.

Trang chủ của website giới thiệu ngắn gọn về ONCE, sử dụng hình ảnh minh họa trẻ trung và gam màu hồng pastel làm chủ đạo để truyền tải sự nhẹ nhàng, thân thiện nhưng vẫn nổi bật của thương hiệu. Trang giới thiệu (About) kể lại hành trình phát triển của ONCE, sứ mệnh, tầm nhìn và giá trị cộng đồng mà ONCE hướng tới. Trang sản phẩm (Shop) trình bày các bộ sưu tập cà phê như Double Honey và Gesha, mỗi sản phẩm đều có hình ảnh minh họa, mô tả, và nút thêm vào giỏ.

Người dùng có thể đăng ký tài khoản, đăng nhập và thêm sản phẩm vào giỏ hàng. Các dữ liệu người dùng, sản phẩm và đơn hàng được lưu trữ trong SQLite — một cơ sở dữ liệu nhẹ nhưng đủ mạnh để đáp ứng nhu cầu của dự án nhỏ. Chức năng bảo mật cơ bản được thực hiện thông qua việc mã hóa mật khẩu bằng Werkzeug.

Quá trình thực hiện dự án giúp tôi rèn luyện kỹ năng tổ chức cấu trúc ứng dụng web theo mô hình MVC, tương tác cơ sở dữ liệu, xử lý form, session và trạng thái người dùng. Tôi cũng học được cách tạo giao diện thân thiện người dùng và đảm bảo trải nghiệm xuyên suốt trên cả desktop và mobile.

Dự án là bước khởi đầu cho khả năng phát triển thành nền tảng thương mại điện tử hoàn chỉnh, với các chức năng nâng cao như tích hợp cổng thanh toán thực tế, theo dõi đơn hàng, phân tích dữ liệu người dùng, v.v.

---

### Các tính năng chính:

- **Trang chủ (Home):**
  - Thiết kế hiện đại với màu hồng pastel đặc trưng.
  - Ảnh bìa, logo và các hình minh họa mang dấu ấn thương hiệu.
  - Câu slogan giới thiệu ONCE và liên kết đến các phần khác.

- **Trang Giới thiệu (About):**
  - Kể câu chuyện hình thành ONCE.
  - Chia sẻ mục tiêu, triết lý hoạt động và định hướng xây dựng cộng đồng cà phê.
  - Kèm ảnh minh họa hài hòa, đồng bộ.

- **Trang Sản phẩm (Shop):**
  - Hiển thị các bộ sưu tập đặc biệt như Double Honey và Gesha.
  - Sử dụng SwiperJS để trình bày sản phẩm đẹp mắt, có mô tả chi tiết.
  - Nút “Add to Cart” và logic thêm vào giỏ hàng.

- **Chức năng Giỏ hàng (Cart):**
  - Hiển thị danh sách sản phẩm đã chọn.
  - Tính tổng chi phí và hỗ trợ thanh toán (mô phỏng).
  - Cho phép xóa hoặc cập nhật sản phẩm trong giỏ.

- **Đăng ký/Đăng nhập người dùng:**
  - Hệ thống xác thực bảo mật bằng hash mật khẩu.
  - Người dùng có thể đăng nhập, đăng ký và theo dõi hoạt động của mình.

- **Cơ sở dữ liệu SQLite:**
  - Quản lý người dùng, sản phẩm, giỏ hàng và đơn hàng.
  - Các thao tác truy vấn SQL chính xác và an toàn.

---

### Công nghệ sử dụng:

- **Backend:** Python + Flask + Jinja2
- **Frontend:** HTML5, CSS3, JavaScript, SwiperJS
- **Database:** SQLite
- **Khác:** Bootstrap, Werkzeug, Font Poppins, Thiết kế Responsive

---

### Mục tiêu dự án:

- Tái hiện thương hiệu ONCE Specialty Coffee qua một website mang màu sắc và cá tính riêng.
- Kết hợp kỹ thuật lập trình backend/frontend và kỹ năng UI/UX.
- Đáp ứng đầy đủ tiêu chí của bài tập cuối kỳ CS50 Final Project.
- Là nền tảng mở rộng để phát triển các chức năng nâng cao như thanh toán trực tuyến, blog chia sẻ kiến thức cà phê, loyalty point,…


