# Auto Messenger
Tự động nhắn tin tới list UID với nội dung chỉ định

## Ưu điểm so với các ứng dụng khác:
- Deploy ứng dụng lên Heroku hoàn toàn miễn phí
- Sau khi deploy, mọi tính năng đều thực hiện thông qua tin nhắn tương tác với chính nick của bạn.
- Chỉ cần có thiết bị vào được facebook, messenger là bạn đã có thể sử dụng

## Cách hoạt động
- Tool sẽ tự động gửi tin nhắn tới các UID đã chỉ định khi bạn nhắn tin cho chính mình.
- Nội dung tin nhắn gửi đi là nội dung bạn gửi cho chính bạn
- Có cơ chế "nghỉ" để tránh facebook báo SPAM

## Cài đặt
- Cài đặt Python 3
- Trên terminal/cmd:
```bash
> pip install -r requirements.txt
> python chatbot.py
```

## Nâng cao
- Nếu bạn muốn hệ thống hoạt động 24/24, hãy deploy ứng dụng này lên Heroku. Xem hướng dẫn chi tiết [tại đây](#)

## Features
Dưới đây là các tính năng dự kiến sẽ phát triển:
[x] Tự động gửi tin nhắn
[] Hẹn giờ gửi tin nhắn
[] Thêm/ Xóa tài khoản trong danh sách nhận tin
[] Gửi tin nhắn kèm theo tên người dùng
[] Tự động chúc mừng sinh nhật

## Bugs
- Vui lòng report tại đây

## Authors:
- N: Nguyễn Văn Hiếu
- W: https://nguyenvanhieu.vn
- F: fb.me/nguyenvanhieu.me
- E: hieunv.dev@gmail.com
