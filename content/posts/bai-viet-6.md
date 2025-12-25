---
title: "WebSocket – Giao tiếp realtime trong Java & JavaScript"
date: 2025-12-23
draft: false
categories: ["Development", "WebSocket", "Realtime"]
---

Nếu HTTP giống như một cuộc gọi điện thoại (kết nối xong rồi ngắt), thì WebSocket giống như bộ đàm – kết nối được duy trì liên tục và cho phép hai bên trao đổi dữ liệu theo thời gian thực.



## 1. Tổng quan về WebSocket

WebSocket là một giao thức cho phép **giao tiếp song công toàn phần (full-duplex)** giữa Client và Server thông qua **một kết nối TCP duy nhất**.

Khác với HTTP truyền thống:
- **HTTP**: Client phải chủ động gửi request để nhận response.
- **WebSocket**: Server có thể **chủ động gửi dữ liệu** cho Client bất kỳ lúc nào.

WebSocket bắt đầu bằng một **HTTP Handshake**, sau đó được **nâng cấp (Upgrade)** sang giao thức WebSocket (`ws://` hoặc `wss://`).



## 2. Quy trình hoạt động của WebSocket

Quá trình giao tiếp WebSocket diễn ra theo các bước:
1. Client gửi HTTP request yêu cầu nâng cấp kết nối.
2. Server chấp nhận và chuyển sang WebSocket.
3. Kết nối được giữ mở liên tục.
4. Client và Server trao đổi dữ liệu hai chiều.
5. Kết nối chỉ đóng khi một trong hai bên chủ động ngắt.

Nhờ cơ chế này, WebSocket giảm đáng kể độ trễ so với HTTP Polling hoặc Long Polling.



## 3. Ví dụ code WebSocket

### Java: Xử lý message từ Client

```java
@OnMessage
public void processMessage(String clientMessage, Session session) {
    System.out.println("Received: " + clientMessage);
    try {
        session.getBasicRemote().sendText("Server echo: " + clientMessage);
    } catch (IOException e) {
        e.printStackTrace();
    }
}
```

Đoạn mã trên minh họa cách Server Java nhận dữ liệu, xử lý và phản hồi ngay lập tức. Trong thực tế, Java thường sử dụng **Java EE WebSocket API** hoặc **Spring Boot WebSocket**.

### JavaScript: Kết nối WebSocket Client

```javascript
const socket = new WebSocket("ws://blog.local/realtime");

socket.onopen = () => {
    console.log("WebSocket connected");
};

socket.onmessage = (event) => {
    updateNotification(event.data);
};

socket.onclose = () => {
    console.log("WebSocket closed");
};
```

JavaScript giữ kết nối WebSocket luôn mở, cho phép nhận dữ liệu realtime từ Server mà không cần gửi request liên tục.



## 4. So sánh WebSocket và HTTP Polling

| Tiêu chí | WebSocket | HTTP Polling |
| :--- | :--- | :--- |
| **Kết nối** | Duy trì liên tục | Mở/đóng nhiều lần |
| **Giao tiếp hai chiều** | Có (Full-duplex) | Không (Half-duplex) |
| **Độ trễ** | Rất thấp | Cao |
| **Tài nguyên** | Tiết kiệm | Tốn kém |



## 5. Ứng dụng thực tế của WebSocket

WebSocket được sử dụng phổ biến trong:
- **Ứng dụng chat realtime**: Nhận tin nhắn ngay lập tức.
- **Game online**: Đồng bộ hóa trạng thái người chơi.
- **Sàn chứng khoán**: Theo dõi giá cổ phiếu nhảy số từng giây.
- **Hệ thống thông báo**: Notification nhảy ra ngay khi có sự kiện.
- **Dashboard IoT**: Giám sát dữ liệu cảm biến thời gian thực.

## Kết luận

WebSocket mang lại khả năng giao tiếp realtime hiệu quả cho các ứng dụng hiện đại. Trong khi Java đảm nhiệm tốt vai trò Server xử lý kết nối, JavaScript giúp Client nhận và phản hồi thông tin tức thời, tạo nên trải nghiệm người dùng mượt mà và sống động.
