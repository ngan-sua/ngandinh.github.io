---
title: "Mô hình Client – Server trong lập trình mạng"
date: 2025-12-23
draft: false
categories: ["Networking", "Client-Server"]
---

Mô hình **Client – Server** là nền tảng của hầu hết các hệ thống mạng và ứng dụng web hiện nay. Hầu như mọi thao tác trên Internet như truy cập website, đăng nhập hệ thống hay gọi API đều tuân theo kiến trúc này. Việc hiểu rõ mô hình Client – Server giúp lập trình viên nắm vững cách các ứng dụng giao tiếp và trao đổi dữ liệu qua mạng.



## 1. Khái niệm mô hình Client – Server

Trong kiến trúc Client – Server, công việc được phân chia rõ ràng giữa hai thành phần chính:

- **Client**: Thiết bị hoặc chương trình gửi yêu cầu (Request) đến Server  
  Ví dụ: Trình duyệt web, ứng dụng di động, phần mềm desktop
- **Server**: Máy chủ tiếp nhận yêu cầu, xử lý và trả về kết quả (Response)

Client và Server giao tiếp with nhau thông qua các **giao thức mạng** như HTTP, TCP/IP hoặc WebSocket.



## 2. Quy trình hoạt động

Quy trình giao tiếp trong mô hình Client – Server thường diễn ra theo các bước sau:
1. Client gửi yêu cầu đến Server thông qua mạng
2. Server tiếp nhận và xử lý yêu cầu
3. Server trả kết quả về cho Client
4. Client hiển thị hoặc xử lý dữ liệu nhận được

Mô hình này giúp hệ thống dễ quản lý và mở rộng khi số lượng người dùng tăng lên.



## 3. Ví dụ minh họa bằng code

### Java: Đọc dữ liệu từ Socket (Server)

```java
InputStream in = socket.getInputStream();
BufferedReader reader = new BufferedReader(new InputStreamReader(in));
String message = reader.readLine();
System.out.println("Client gửi: " + message);
```

Đoạn code trên minh họa cách Server trong Java nhận dữ liệu từ Client thông qua Socket.

### JavaScript: Gửi Request từ Client (Axios)

```javascript
axios.get("/api/v1/profile")
  .then(response => {
    renderUser(response.data);
  })
  .catch(error => {
    console.error("Error:", error);
  });
```

Client gửi yêu cầu HTTP đến Server và nhận dữ liệu phản hồi để hiển thị.



## 4. Ưu điểm và hạn chế của mô hình Client – Server

| Tiêu chí | Ưu điểm | Hạn chế |
| :--- | :--- | :--- |
| **Quản lý** | Tập trung tại Server | Server có thể bị quá tải |
| **Bảo mật** | Dễ kiểm soát truy cập | Điểm yếu tập trung (Single point of failure) |
| **Mở rộng** | Dễ dàng nâng cấp hạ tầng | Chi phí hạ tầng cao |



## 5. Ứng dụng thực tế

Mô hình Client – Server được áp dụng rộng rãi trong:
- Website và Web API
- Ứng dụng di động
- Hệ thống quản lý doanh nghiệp
- Dịch vụ ngân hàng và thương mại điện tử

Trong thực tế, các hệ thống lớn thường kết hợp thêm các mô hình khác như Load Balancing hoặc Microservices để khắc phục hạn chế của Client – Server truyền thống.

## Kết luận

Mô hình Client – Server là kiến thức nền tảng quan trọng trong lập trình mạng. Việc nắm vững kiến trúc này giúp lập trình viên hiểu rõ cách các hệ thống hoạt động, từ đó xây dựng các ứng dụng mạng ổn định, an toàn và dễ mở rộng.
