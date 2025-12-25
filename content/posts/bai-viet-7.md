---
title: "Bảo mật cơ bản trong lập trình mạng"
date: 2025-12-23
draft: false
categories: ["Development", "Security", "Networking"]
---

Mạng máy tính là môi trường mở, nơi dữ liệu luôn phải di chuyển qua nhiều thiết bị trung gian. Nếu không được bảo vệ đúng cách, thông tin có thể bị đánh cắp, chỉnh sửa hoặc giả mạo mà người dùng không hề hay biết.



## 1. Tổng quan về bảo mật trong lập trình mạng

Bảo mật mạng tập trung vào việc **bảo vệ dữ liệu khi truyền tải** và **ngăn chặn các truy cập trái phép** vào hệ thống.  
Lập trình viên cần hiểu rằng mọi dữ liệu đến từ mạng đều **không đáng tin cậy** cho đến khi được kiểm chứng.

Một số mối đe dọa phổ biến trong lập trình mạng:
- **Man-in-the-Middle (MitM)**: Kẻ tấn công nghe lén hoặc thay đổi dữ liệu trên đường truyền.
- **Sniffing**: Bắt gói tin mạng để đọc thông tin nhạy cảm.
- **SQL Injection**: Chèn câu lệnh SQL độc hại thông qua input.
- **Cross-Site Scripting (XSS)**: Chèn mã độc vào trình duyệt người dùng.



## 2. Các biện pháp bảo mật cơ bản

### HTTPS và mã hóa dữ liệu

HTTPS sử dụng TLS/SSL để:
- Mã hóa dữ liệu truyền giữa Client và Server.
- Xác thực danh tính Server.
- Đảm bảo dữ liệu không bị thay đổi trong quá trình truyền.

👉 Mọi ứng dụng web hiện đại **bắt buộc phải sử dụng HTTPS**.



### Token-Based Authentication

Thay vì lưu session truyền thống, hệ thống hiện đại thường sử dụng:
- **JWT (JSON Web Token)**
- **Access Token / Refresh Token**

Cơ chế này giúp:
- Giảm nguy cơ bị chiếm quyền phiên.
- Dễ mở rộng cho hệ thống phân tán (Microservices).



## 3. Ví dụ code bảo mật

### Java: Hash mật khẩu với BCrypt

```java
String hashedPassword = BCrypt.hashpw(plainPass, BCrypt.gensalt());
```

Việc sử dụng BCrypt giúp:
- Không lưu mật khẩu dạng plaintext.
- Tự động thêm salt.
- Chống lại tấn công brute-force hiệu quả.

### JavaScript: Ngăn chặn XSS từ dữ liệu người dùng

```javascript
const safeText = userContent
  .replace(/</g, "&lt;")
  .replace(/>/g, "&gt;");
```

Việc escape ký tự nguy hiểm giúp:
- Ngăn script độc hại thực thi trong trình duyệt.
- Bảo vệ người dùng khỏi đánh cắp cookie hoặc token.



## 4. Nguyên tắc bảo mật quan trọng

Một số nguyên tắc mà lập trình viên mạng cần ghi nhớ:
- Không bao giờ tin tưởng input từ Client.
- Luôn validate và sanitize dữ liệu.
- Không truyền dữ liệu nhạy cảm qua HTTP thường.
- Áp dụng nguyên tắc Least Privilege (quyền tối thiểu).
- Log và giám sát các hành vi bất thường.

Bảo mật không phải là một bước trong dự án mà là một quy trình xuyên suốt vòng đời phần mềm.

## Kết luận

Bảo mật trong lập trình mạng không phải là lựa chọn, mà là yêu cầu bắt buộc. Việc kết hợp giữa mã hóa, xác thực, và xử lý dữ liệu an toàn giúp hệ thống tránh được phần lớn các cuộc tấn công phổ biến. Một lập trình viên giỏi không chỉ biết viết code chạy được, mà còn phải biết viết code an toàn.
