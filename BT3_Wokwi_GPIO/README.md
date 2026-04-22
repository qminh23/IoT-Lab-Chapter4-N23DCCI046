# BÁO CÁO BÀI TẬP THỰC HÀNH IOT - BÀI SỐ 3
## Hệ thống nhúng và Mô phỏng trên Wokwi

Tài liệu này tổng hợp 3 dự án mô phỏng được thực hiện trên nền tảng Wokwi, sử dụng vi điều khiển Raspberry Pi Pico để giải quyết các bài toán điều khiển cơ bản và giám sát cảm biến.

---

## 1. Danh sách dự án (Wokwi Share Links)

| STT | Tên Dự Án | Link Mô Phỏng |
|:---:|:---|:---|
| **01** | Hệ thống Đèn Giao Thông | [Truy cập Project 1](https://wokwi.com/projects/461895598211200001) |
| **02** | Giám sát DHT22 & LED Cảnh báo | [Truy cập Project 2](https://wokwi.com/projects/461896064553972737) |
| **03** | Điều khiển LED bằng Biến trở | [Truy cập Project 3](https://wokwi.com/projects/461896558398856193) |

---

## 2. Chi tiết kỹ thuật từng dự án

### Project 1: Hệ thống Đèn Giao Thông (Traffic Light)
* **Mô tả:** Mô phỏng chu kỳ hoạt động của đèn giao thông thực tế với 3 trạng thái: Xanh (Đi) -> Vàng (Chậm lại) -> Đỏ (Dừng lại).
* **Sơ đồ nối dây:**
    * LED Đỏ: `GP15`
    * LED Vàng: `GP14`
    * LED Xanh: `GP13`
* **Nguyên lý:** Sử dụng vòng lặp thời gian để thay đổi trạng thái chân xuất mức cao (High/1) lần lượt cho các LED.

### Project 2: Giám sát DHT22 & LED Cảnh báo
* **Mô tả:** Đọc dữ liệu nhiệt độ và độ ẩm từ cảm biến DHT22, hiển thị lên Terminal và đưa ra cảnh báo bằng đèn LED theo ngưỡng.
* **Sơ đồ nối dây:**
    * DHT22 Data: `GP16`
    * LED Đỏ (Cảnh báo Nhiệt độ > 30°C): `GP15`
    * LED Vàng (Cảnh báo Độ ẩm > 80%): `GP14`
    * LED Xanh (Trạng thái Bình thường): `GP13`
* **Chức năng:** Cập nhật dữ liệu mỗi 2 giây, hỗ trợ giám sát môi trường thời gian thực.

### Project 3: Điều khiển LED với Biến trở (Potentiometer)
* **Mô tả:** Đọc giá trị điện áp Analog từ biến trở thông qua bộ ADC và sử dụng giá trị đó để điều khiển hệ thống (độ sáng LED hoặc tốc độ chớp tắt).
* **Sơ đồ nối dây:**
    * Chân giữa Biến trở: `GP26` (ADC0)
    * Hai chân bìa Biến trở: Nối vào `3V3` và `GND`.
* **Chức năng:** Minh họa cách xử lý tín hiệu tương tự (Analog) sang kỹ thuật số (Digital) trên vi điều khiển.

---


---
