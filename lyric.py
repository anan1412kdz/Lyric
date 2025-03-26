import random
import sys
import time
import os
line = '.'
line1 = 'nếu lỡ một mai nay quên mat tên người'

line2 = 'Tôi sẽ khắc lại những lần quên bằng nụ cười'
line3a = 'ái cuộc đời này xem '
line3b = 'như '
line3c = 'hoa '
line3d = 'đã '
line3e = 'thay '
line3f = 'dần '
line3g = 'và...\n'
line4 = 'Ngày mai mọi thứ sẽ khác thôi em'
line5 = 'Và nếu lỡ một mai này em lãng quên tôi'
line6 = 'Thì bài hát dang dở '
line6a = 'vẫn '
line6b = 'cứ '
line6c = 'tiếp '
line6d = 'tục '
line6e = 'trôi '
line6f = 'oh'
line7 = 'Sẽ thấy lòng cần thêm thời gian để lành'
line8a = 'Gửi'
line8b = 'vào' 
line8c = 'làn'
line8d = 'mây'
line8e = 'vẫn'
line8f = 'chưa'
line8g = 'nắn'
line8h = 'nót'
line8j = 'hình'
line8k = 'hài'
def combined_effect(text, delay=0.1):
    length = len(text)
    brightness_levels = [90, 37, 97]  # Các mức độ sáng (mờ đến đậm)

    for i in range(length // 2 + 1):
        # Tạo phần trái và phải của văn bản
        left_part = text[:i]
        right_part = text[length - i:]
        combined_text = left_part + " " * (length - len(left_part) - len(right_part)) + right_part
        for level in brightness_levels:
            sys.stdout.write(f"\033[{level}m{combined_text}\033[0m\r")  
            sys.stdout.flush()  
            time.sleep(delay / len(brightness_levels))  

    print(text) 

def animated_fade_in_text(text, type_delay=0.05, fade_delay=0.2):
    # Gõ từng ký tự một
    for i in range(len(text) + 1):
        sys.stdout.write("\r" + text[:i])  # Hiển thị từng ký tự
        sys.stdout.flush()
        time.sleep(type_delay)
    
    # Các mức độ sáng từ mờ đến rõ
    brightness_levels = [90, 37, 97]  # Mờ, trung bình, sáng
    
    for level in brightness_levels:
        sys.stdout.write(f"\r\033[{level}m{text}\033[0m")  # Hiển thị với độ sáng khác nhau
        sys.stdout.flush()
        time.sleep(fade_delay)
    
    # Trả về chuỗi đã được xử lý và thêm \n để xuống dòng
    return text + "\n"
import random
import sys
import time

import sys
import time
import random

def random_fill(text, delay=0.1):
    # Tạo danh sách kết quả chứa các ký tự trắng
    result = [" "] * len(text)
    # Tạo danh sách các chỉ số vị trí
    indices = list(range(len(text)))

    # Lặp cho đến khi hoàn tất điền hết các ký tự
    while indices:
        # Chọn một chỉ số ngẫu nhiên từ danh sách các chỉ số
        idx = random.choice(indices)
        
        # Điền ký tự từ chuỗi gốc vào vị trí ngẫu nhiên
        result[idx] = text[idx]

        # Hiển thị chuỗi hiện tại với ký tự được điền
        sys.stdout.write("\r" + "".join(result))
        sys.stdout.flush()

        # Loại bỏ vị trí đã hoàn thành
        indices.remove(idx)

        # Chờ trước khi tiếp tục
        time.sleep(delay)

    # Xuống dòng sau khi hoàn thành
    print()  # Thêm dòng mới
import sys
import time

def fade_in_text(text, delay=0.2):
    brightness_levels = [2, 3, 7]  # Mã ANSI: 2 - mờ, 3 - vừa, 7 - sáng

    for level in brightness_levels:
        sys.stdout.write(f"\033[{level}m{text}\033[0m\r")  # Hiển thị với độ sáng khác nhau
        sys.stdout.flush()  # Làm mới bộ đệm
        time.sleep(delay)  # Tạo độ trễ giữa các mức sáng

    print(text)  # Hiển thị chữ rõ ràng sau khi hiệu ứng kết thúc
    sys.stdout.write(f"{text}\r\033[K")  # Hiển thị văn bản cuối cùng
    sys.stdout.flush()
    time.sleep(1)  # Giữ văn bản trong 1 giây trước khi xóa

    # Xóa văn bản bằng cách ghi đè lên bằng khoảng trắng
    sys.stdout.write("\r\033[K")  # Di chuyển con trỏ về đầu dòng và xóa nội dung
    sys.stdout.flush()


import sys
import time

def mar_text(text, width=30, delay=0.1):
    # Thêm khoảng trống hai bên để tạo hiệu ứng di chuyển
    padded_text = " " * width + text + " " * width

    # Lặp qua từng vị trí trong padded_text
    for i in range(len(padded_text) - width + 1):
        # Lấy đoạn văn bản có độ dài bằng width
        marquee_segment = padded_text[i:i + width]
        
        # Hiển thị đoạn văn bản
        sys.stdout.write("\r" + marquee_segment)  # \r để di chuyển con trỏ về đầu dòng
        sys.stdout.flush()  # Làm mới bộ đệm
        time.sleep(delay)  # Tạo độ trễ

    # Xóa dòng hiện tại và xuống dòng
    sys.stdout.write("\r\033[K")  # \033[K để xóa nội dung của dòng
    sys.stdout.flush()
    print()  # Xuống dòng sau khi hoàn thành
import sys
import time

def fade(text, delay=0.2):
    # Các mức độ sáng từ mờ đến đậm hơn
    brightness_levels = [90, 37, 97]  # ANSI màu: mờ (90), trung bình (37), sáng (97)
    
    for level in brightness_levels:
        sys.stdout.write(f"\033[{level}m{text}\033[0m\r")  # Hiển thị với độ sáng khác nhau
        sys.stdout.flush()  # Làm mới bộ đệm
        time.sleep(delay)  # Tạo độ trễ giữa các mức sáng
    print(text)  # Hiển thị chữ rõ ràng sau khi hiệu ứng kết thúc

# Gọi hàm

import os
os.system('clear')

combined_effect(f"{line1}",delay=0.13)
time.sleep(1.2)
animated_fade_in_text(f"{line2}", type_delay=0.06, fade_delay=0.3)
os.system('clear')
time.sleep(0.4)
random_fill(f"H{line3a}", delay=0.1)
time.sleep(0)
print(f"{line3b}", end = '', flush = True)
time.sleep(0.2)
print(f"{line3c}", end = '', flush = True)
time.sleep(0.2)
print(f"{line3d}", end = '', flush = True)
time.sleep(0.2)
print(f"{line3e}", end = '', flush = True)
time.sleep(0.2)
print(f"{line3f}", end = '', flush = True)
time.sleep(0.2)
print(f"{line3g}", end = '', flush = True)
fade_in_text(f"{line4}", delay=1)
os.system('clear')
mar_text(f"{line5}", width=12, delay=0.08)
print()
fade(f"{line6}", delay=0.5)
print(f"{line6a}", end = '', flush = True)
time.sleep(0.2)
print(f"{line6b}", end = '', flush = True)
time.sleep(0.2)
print(f"{line6c}", end = '', flush = True)
time.sleep(0.2)
print(f"{line6d}", end = '', flush = True)
time.sleep(0.2)
print(f"{line6e}", end = '', flush = True)
time.sleep(0.2)
print(f"{line6f} ", end = '', flush = True)
time.sleep(0.2)
print(f"{line6f}", end = '', flush = True)
time.sleep(0.5)
animated_fade_in_text(f"{line7}", type_delay=0.06, fade_delay=0.3)
print()
print(f"{line8a} ", end = '', flush = True)
time.sleep(0.2)
print(f"{line8b} ", end = '', flush = True)
time.sleep(0.5)
print(f"{line8c} ", end = '', flush = True)
time.sleep(0.5)
print(f"{line8d} ", end = '', flush = True)
time.sleep(0.2)
print(f"{line8e} ", end = '', flush = True)
time.sleep(0.2)
print(f"{line8f} ", end = '', flush = True)
time.sleep(0.2)
print(f"{line8g} ", end = '', flush = True)
time.sleep(0.2)
print(f"{line8h} ", end = '', flush = True)
time.sleep(0.2)
print(f"{line8j} ", end = '', flush = True)
time.sleep(0.5)
print(f"{line8k}", end = '', flush = True)
time.sleep(0.5)


