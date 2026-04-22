from machine import Pin
import dht
import time

# Khởi tạo cảm biến DHT22 nối vào chân GP16
sensor = dht.DHT22(Pin(16))

# Khởi tạo các chân LED cảnh báo
red = Pin(15, Pin.OUT)
yellow = Pin(14, Pin.OUT)
green = Pin(13, Pin.OUT)

while True:
    try:
        # Cập nhật dữ liệu từ cảm biến
        sensor.measure()
        temp = sensor.temperature()
        hum = sensor.humidity()
        
        # Lấy thời gian (giờ:phút:giây)
        t = time.localtime()
        ts = f'{t[3]:02d}:{t[4]:02d}:{t[5]:02d}'
        
        # In kết quả nhiệt độ và độ ẩm ra Terminal
        print(f'[{ts}] Temp: {temp:.1f}°C | Humidity: {hum:.1f}%')
        
        # Logic cảnh báo theo yêu cầu Bước 4
        if temp > 30:
            # Nhiệt độ cao -> Bật Đỏ, tắt Vàng/Xanh
            red.value(1)
            yellow.value(0)
            green.value(0)
            print('  >> CẢNH BÁO: NHIỆT ĐỘ CAO!')
            
        elif hum > 80:
            # Độ ẩm cao -> Bật Vàng, tắt Đỏ/Xanh
            red.value(0)
            yellow.value(1)
            green.value(0)
            print('  >> CẢNH BÁO: ĐỘ ẨM CAO!')
            
        else:
            # Bình thường -> Bật Xanh, tắt Đỏ/Vàng
            red.value(0)
            yellow.value(0)
            green.value(1)
            print('  Bình thường.')
            
    except Exception as e:
        print(f'Lỗi đọc cảm biến: {e}')
        
    # Tạm dừng 2 giây trước vòng lặp tiếp theo
    time.sleep(2)