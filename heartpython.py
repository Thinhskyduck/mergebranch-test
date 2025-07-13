import random
from math import sin, cos, pi
from tkinter import *

# Kích thước canvas
WIDTH, HEIGHT = 1000, 1500
CENTER_X, CENTER_Y = WIDTH // 2, HEIGHT // 2
SCALE = 12  # Phóng to hình trái tim
COLOR = "#f76070"  # Màu trái tim

def heart(t):
    """Hàm tạo hình trái tim theo tham số t"""
    x = SCALE * 16 * sin(t) ** 3
    y = -SCALE * (13 * cos(t) - 5 * cos(2 * t) - 2 * cos(3 * t) - cos(4 * t))
    return CENTER_X + x, CENTER_Y + y

def draw_heart(canvas, frame):
    canvas.delete("all")  # Xóa khung vẽ cũ

    # Vẽ các điểm trái tim
    for i in range(0, 100, 1):  # Giảm số lượng điểm để nhẹ hơn
        t = 2 * pi * i / 100
        x, y = heart(t)

        # Thêm hiệu ứng nhấp nháy nhỏ
        size = random.choice([1, 2])
        dx = random.randint(-1, 1)
        dy = random.randint(-1, 1)
        canvas.create_oval(x+dx, y+dy, x+dx+size, y+dy+size, fill=COLOR, width=0)

    # Vẽ halo đơn giản xung quanh trái tim
    for _ in range(100):
        t = random.uniform(0, 2 * pi)
        x, y = heart(t)
        x += random.uniform(-10, 10)
        y += random.uniform(-10, 10)
        canvas.create_oval(x, y, x+1, y+1, fill=COLOR, width=0)

    # Lặp lại sau 100ms
    root.after(100, draw_heart, canvas, frame+1)

# Khởi tạo giao diện
root = Tk()
root.title("Simple Heart Animation")
canvas = Canvas(root, bg="black", width=WIDTH, height=HEIGHT)
canvas.pack()

draw_heart(canvas, 0)
root.mainloop()

