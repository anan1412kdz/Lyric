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
    brightness_levels = [90, 37, 97]

    for i in range(length // 2 + 1):
        left_part = text[:i]
        right_part = text[length - i:]
        combined_text = left_part + " " * (length - len(left_part) - len(right_part)) + right_part
        for level in brightness_levels:
            sys.stdout.write(f"\033[{level}m{combined_text}\033[0m\r")  
            sys.stdout.flush()  
            time.sleep(delay / len(brightness_levels))  

    print(text) 

def animated_fade_in_text(text, type_delay=0.05, fade_delay=0.2):
    for i in range(len(text) + 1):
        sys.stdout.write("\r" + text[:i])
        sys.stdout.flush()
        time.sleep(type_delay)
    
    brightness_levels = [90, 37, 97]
    
    for level in brightness_levels:
        sys.stdout.write(f"\r\033[{level}m{text}\033[0m")
        sys.stdout.flush()
        time.sleep(fade_delay)
    
    return text + "\n"

def random_fill(text, delay=0.1):
    result = [" "] * len(text)
    indices = list(range(len(text)))

    while indices:
        idx = random.choice(indices)
        result[idx] = text[idx]
        sys.stdout.write("\r" + "".join(result))
        sys.stdout.flush()
        indices.remove(idx)
        time.sleep(delay)

    print()

def fade_in_text(text, delay=0.2):
    brightness_levels = [2, 3, 7]

    for level in brightness_levels:
        sys.stdout.write(f"\033[{level}m{text}\033[0m\r")
        sys.stdout.flush()
        time.sleep(delay)

    print(text)
    sys.stdout.write(f"{text}\r\033[K")
    sys.stdout.flush()
    time.sleep(1)

    sys.stdout.write("\r\033[K")
    sys.stdout.flush()

def mar_text(text, width=30, delay=0.1):
    padded_text = " " * width + text + " " * width

    for i in range(len(padded_text) - width + 1):
        marquee_segment = padded_text[i:i + width]
        sys.stdout.write("\r" + marquee_segment)
        sys.stdout.flush()
        time.sleep(delay)

    sys.stdout.write("\r\033[K") 
    sys.stdout.flush()
    print()  

def fade(text, delay=0.2):
    brightness_levels = [90, 37, 97]
    
    for level in brightness_levels:
        sys.stdout.write(f"\033[{level}m{text}\033[0m\r") 
        sys.stdout.flush()  
        time.sleep(delay)  
    print(text)  

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