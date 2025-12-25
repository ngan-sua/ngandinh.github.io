---
title: "Lập trình Socket trong Java – Cơ bản"
date: 2025-12-23
draft: false
categories: ["Networking", "Java"]
---

Socket là một trong những khái niệm nền tảng của lập trình mạng, cho phép hai chương trình đang chạy trên các máy tính khác nhau giao tiếp với nhau thông qua mạng TCP/IP. Trong Java, lập trình Socket được sử dụng rộng rãi để xây dựng các ứng dụng client – server ở mức thấp, giúp lập trình viên hiểu rõ cơ chế truyền dữ liệu qua mạng.



## 1. Khái niệm Socket trong Java

Socket có thể được hiểu là **điểm cuối của một kênh giao tiếp** giữa hai tiến trình trên mạng. Java cung cấp các lớp hỗ trợ Socket trong gói `java.net`, cho phép lập trình viên dễ dàng triển khai mô hình Client – Server.

Các lớp chính bao gồm:
- **ServerSocket**: Được sử dụng ở phía Server để lắng nghe yêu cầu kết nối từ Client
- **Socket**: Đại diện cho kết nối giữa Client và Server sau khi kết nối được thiết lập



## 2. Quy trình hoạt động của Socket

Quy trình giao tiếp cơ bản giữa Client và Server sử dụng Socket gồm các bước:
1. Server tạo `ServerSocket` và lắng nghe tại một cổng (port)
2. Client tạo `Socket` và gửi yêu cầu kết nối đến Server
3. Server chấp nhận kết nối thông qua phương thức `accept()`
4. Hai bên trao đổi dữ liệu thông qua `InputStream` và `OutputStream`
5. Kết thúc giao tiếp và đóng kết nối



## 3. Ví dụ minh họa bằng code

### Server: Khởi tạo và chấp nhận kết nối

```java
ServerSocket server = new ServerSocket(9999);
System.out.println("Server đang chờ client kết nối...");

Socket socket = server.accept();
System.out.println("Client đã kết nối!");
```

Đoạn code trên tạo một Server lắng nghe kết nối tại cổng 9999 và chấp nhận một Client khi có yêu cầu.

### Client: Chủ động kết nối đến Server

```java
Socket socket = new Socket("127.0.0.1", 9999);
System.out.println("Kết nối tới server thành công!");
```

Client chủ động kết nối đến Server thông qua địa chỉ IP và cổng tương ứng.



## 4. Trao đổi dữ liệu qua Socket

Sau khi kết nối được thiết lập, Client và Server có thể gửi – nhận dữ liệu thông qua luồng vào/ra.

```java
// Gửi dữ liệu
OutputStream out = socket.getOutputStream();
PrintWriter writer = new PrintWriter(out, true);
writer.println("Hello Server!");

// Nhận dữ liệu
InputStream in = socket.getInputStream();
BufferedReader reader = new BufferedReader(new InputStreamReader(in));
String message = reader.readLine();
System.out.println("Nhận từ client: " + message);
```



## 5. Ưu điểm và hạn chế của Socket Java

| Tiêu chí | Ưu điểm | Hạn chế |
| :--- | :--- | :--- |
| **Kiểm soát** | Chi tiết quá trình truyền dữ liệu | Phải tự quản lý luồng dữ liệu |
| **Hiệu năng** | Cao, tin cậy (TCP) | Code phức tạp hơn REST API |
| **Ứng dụng** | Học thuật, hệ thống chuyên dụng | Khó mở rộng nếu không có framework |



## 6. Vị trí của Socket trong mô hình OSI

Lập trình Socket trong Java hoạt động chủ yếu ở tầng **Transport** của mô hình OSI, sử dụng giao thức TCP để đảm bảo dữ liệu được truyền đầy đủ, đúng thứ tự và không bị mất mát.

## Kết luận

Mặc dù hiện nay có nhiều framework và công nghệ cấp cao như REST API hay WebSocket, lập trình Socket vẫn là nền tảng quan trọng mà mọi kỹ sư mạng và backend cần nắm vững. Việc hiểu rõ Socket giúp lập trình viên hiểu sâu hơn cách các ứng dụng giao tiếp và trao đổi dữ liệu qua mạng.
