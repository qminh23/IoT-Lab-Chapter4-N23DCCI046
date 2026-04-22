from machine import Pin, ADC, PWM
import time

# Khởi tạo chân đọc Potentiometer (Biến trở) ở chân GP26
pot = ADC(Pin(26))

# Khởi tạo chân PWM cho LED đỏ ở chân GP15
red_pwm = PWM(Pin(15))
red_pwm.freq(1000) # Cài đặt tần số băm xung 1000Hz (1kHz)

while True:
    try:
        # Đọc giá trị từ biến trở (raw sẽ có giá trị từ 0 đến 65535)
        raw = pot.read_u16()
        
        # Bơm thẳng giá trị raw vào hàm điều chỉnh độ sáng PWM
        red_pwm.duty_u16(raw)
        
        # Tính toán phần trăm độ sáng để in ra Terminal cho chuyên nghiệp
        percent = (raw / 65535) * 100
        
        # In kết quả ra màn hình
        print(f'Giá trị biến trở: {raw:5d} | Mức độ sáng LED: {percent:5.1f}%')
        
        # Nghỉ 0.1s để vòng lặp chạy mượt, Terminal không bị trôi quá nhanh
        time.sleep(0.1)
        
    except Exception as e:
        print(f'Lỗi: {e}')
        time.sleep(1)