---
title: "REST API và JSON trong Java & JavaScript"
date: 2025-12-23
draft: false
categories: ["Development", "REST API", "JSON"]
---

REST API và JSON là hai thành phần không thể thiếu trong các hệ thống web và ứng dụng hiện đại. Chúng đóng vai trò trung tâm trong việc giúp các ứng dụng khác nhau có thể giao tiếp, trao đổi dữ liệu một cách hiệu quả và linh hoạt. Trong bài viết này, mình sẽ trình bày tổng quan về REST API, JSON và cách Java cùng JavaScript sử dụng chúng trong thực tế.



## 1. Tổng quan về REST API

REST (Representational State Transfer) là một kiến trúc thiết kế dịch vụ web, trong đó mỗi tài nguyên được biểu diễn thông qua một URL cụ thể. REST API sử dụng các **HTTP Method** để thực hiện các thao tác trên tài nguyên.

Các phương thức HTTP phổ biến trong REST API:
- **GET**: Lấy dữ liệu
- **POST**: Tạo mới dữ liệu
- **PUT**: Cập nhật dữ liệu
- **DELETE**: Xóa dữ liệu

REST API giúp hệ thống:
- Dễ mở rộng
- Dễ tích hợp với nhiều nền tảng
- Hoạt động tốt trong môi trường phân tán



## 2. JSON – Định dạng trao đổi dữ liệu phổ biến

JSON (JavaScript Object Notation) là định dạng dữ liệu nhẹ, dễ đọc và dễ phân tích. Hiện nay, JSON là định dạng trao đổi dữ liệu mặc định trong hầu hết các REST API.

### Ưu điểm của JSON
- Cấu trúc đơn giản, dễ hiểu
- Dễ parse trong JavaScript
- Được hỗ trợ tốt trong Java và nhiều ngôn ngữ khác
- Nhẹ hơn XML, giảm dung lượng truyền tải

### Ví dụ cấu trúc JSON

```json
{
  "user_id": 100,
  "status": "active",
  "roles": ["admin", "dev"]
}
```



## 3. Java xử lý REST API và JSON

Trong các hệ thống backend, Java thường được sử dụng để xây dựng REST API và xử lý dữ liệu JSON.

### Java: Tạo dữ liệu JSON trả về cho Client

```java
JSONObject response = new JSONObject();
response.put("status", "success");
response.put("code", 200);
response.put("message", "Request processed successfully");
```

Đoạn mã trên minh họa cách Java tạo một đối tượng JSON để gửi phản hồi cho Client thông qua REST API. Trong thực tế, Java thường kết hợp với các framework như **Spring Boot** để xây dựng REST API một cách nhanh chóng và hiệu quả.



## 4. JavaScript tiêu thụ REST API

JavaScript đóng vai trò là Client, gửi request đến REST API và xử lý dữ liệu JSON phản hồi từ Server.

```javascript
fetch("/api/users/100")
  .then(response => response.json())
  .then(data => {
    console.log("User ID:", data.user_id);
    console.log("Status:", data.status);
  })
  .catch(error => {
    console.error("Error:", error);
  });
```

JavaScript có khả năng parse JSON một cách tự nhiên, giúp việc xử lý dữ liệu từ Server trở nên rất thuận tiện.



## 5. So sánh JSON và XML

| Tiêu chí | JSON | XML |
| :--- | :--- | :--- |
| **Độ gọn nhẹ** | Cao | Thấp |
| **Dễ đọc** | Dễ | Khó |
| **Parse trong JS** | Tự nhiên | Phức tạp |
| **Phổ biến hiện nay** | Rất cao | Giảm dần |



## 6. Ứng dụng thực tế của REST API và JSON

REST API và JSON được sử dụng rộng rãi trong:
- **Ứng dụng web và mobile**: Kết nối người dùng với dữ liệu.
- **Kiến trúc Microservices**: Giao tiếp giữa các dịch vụ trong hệ thống lớn.
- **Hệ thống tách biệt Frontend – Backend**: Cho phép đội ngũ phát triển độc lập.
- **Tích hợp bên thứ ba**: Ví dụ như tích hợp thanh toán, bản đồ, hay API mạng xã hội.

## Kết luận

REST API và JSON là cặp công nghệ nền tảng trong phát triển phần mềm hiện đại. Java đảm nhiệm tốt vai trò xây dựng và xử lý REST API ở phía Server, trong khi JavaScript giúp Client giao tiếp và xử lý dữ liệu JSON một cách hiệu quả. Việc nắm vững REST và JSON là yêu cầu bắt buộc đối với bất kỳ lập trình viên nào hiện nay.
