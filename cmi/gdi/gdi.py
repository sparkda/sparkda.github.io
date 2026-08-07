import win32gui
import win32con
import win32api
import random
import time
import math

VERSION = "1.0"
# Made by SparKda
# cmi Repo : sparkda.github.io/cmi/



def screen_size():
    return (
        win32api.GetSystemMetrics(0),
        win32api.GetSystemMetrics(1)
    )


def get_screen():
    return win32gui.GetDC(0)


def release_screen(hdc):
    win32gui.ReleaseDC(0, hdc)


def random_color():
    return win32api.RGB(
        random.randint(0, 255),
        random.randint(0, 255),
        random.randint(0, 255)
    )



def invert(duration=5):
    hdc = get_screen()
    w, h = screen_size()

    start = time.time()

    while time.time() - start < duration:
        win32gui.BitBlt(
            hdc, 0, 0, w, h,
            hdc, 0, 0,
            win32con.NOTSRCCOPY
        )

    release_screen(hdc)



def shake(duration=5, amount=20):
    hdc = get_screen()
    w, h = screen_size()

    start = time.time()

    while time.time() - start < duration:

        x = random.randint(-amount, amount)
        y = random.randint(-amount, amount)

        win32gui.BitBlt(
            hdc,
            x,
            y,
            w,
            h,
            hdc,
            0,
            0,
            win32con.SRCCOPY
        )

    release_screen(hdc)



def glitch(duration=5):
    hdc = get_screen()
    w, h = screen_size()

    start = time.time()

    while time.time() - start < duration:

        y = random.randint(0, h - 1)
        height = random.randint(1, 50)
        offset = random.randint(-100, 100)

        win32gui.BitBlt(
            hdc,
            offset,
            y,
            w,
            height,
            hdc,
            0,
            y,
            win32con.SRCCOPY
        )

    release_screen(hdc)



def color_flash(duration=5):
    hdc = get_screen()
    w, h = screen_size()

    start = time.time()

    while time.time() - start < duration:

        brush = win32gui.CreateSolidBrush(random_color())

        old = win32gui.SelectObject(hdc, brush)

        win32gui.PatBlt(
            hdc,
            0,
            0,
            w,
            h,
            win32con.PATINVERT
        )

        win32gui.SelectObject(hdc, old)
        win32gui.DeleteObject(brush)

    release_screen(hdc)



def tunnel(duration=5):
    hdc = get_screen()
    w, h = screen_size()

    start = time.time()

    while time.time() - start < duration:

        win32gui.StretchBlt(
            hdc,
            20,
            20,
            w - 40,
            h - 40,
            hdc,
            0,
            0,
            w,
            h,
            win32con.SRCCOPY
        )

    release_screen(hdc)



def shrink(duration=5):
    hdc = get_screen()
    w, h = screen_size()

    start = time.time()

    while time.time() - start < duration:

        nw = int(w * 0.9)
        nh = int(h * 0.9)

        win32gui.StretchBlt(
            hdc,
            (w - nw) // 2,
            (h - nh) // 2,
            nw,
            nh,
            hdc,
            0,
            0,
            w,
            h,
            win32con.SRCCOPY
        )

    release_screen(hdc)



def expand(duration=5):
    hdc = get_screen()
    w, h = screen_size()

    start = time.time()

    while time.time() - start < duration:

        win32gui.StretchBlt(
            hdc,
            -50,
            -50,
            w + 100,
            h + 100,
            hdc,
            0,
            0,
            w,
            h,
            win32con.SRCCOPY
        )

    release_screen(hdc)



def mosaic(duration=5, block=25):
    hdc = get_screen()
    w, h = screen_size()

    start = time.time()

    while time.time() - start < duration:

        x = random.randrange(0, w, block)
        y = random.randrange(0, h, block)

        win32gui.StretchBlt(
            hdc,
            x,
            y,
            block * 2,
            block * 2,
            hdc,
            x,
            y,
            block,
            block,
            win32con.SRCCOPY
        )

    release_screen(hdc)



def mirror_horizontal(duration=5):
    hdc = get_screen()
    w, h = screen_size()

    start = time.time()

    while time.time() - start < duration:

        win32gui.StretchBlt(
            hdc,
            w,
            0,
            -w,
            h,
            hdc,
            0,
            0,
            w,
            h,
            win32con.SRCCOPY
        )

    release_screen(hdc)



def mirror_vertical(duration=5):
    hdc = get_screen()
    w, h = screen_size()

    start = time.time()

    while time.time() - start < duration:

        win32gui.StretchBlt(
            hdc,
            0,
            h,
            w,
            -h,
            hdc,
            0,
            0,
            w,
            h,
            win32con.SRCCOPY
        )

    release_screen(hdc)



def random_copy(duration=5):
    hdc = get_screen()
    w, h = screen_size()

    start = time.time()

    while time.time() - start < duration:

        x1 = random.randint(0, w - 100)
        y1 = random.randint(0, h - 100)

        x2 = random.randint(0, w - 100)
        y2 = random.randint(0, h - 100)

        size = random.randint(20, 200)

        win32gui.BitBlt(
            hdc,
            x2,
            y2,
            size,
            size,
            hdc,
            x1,
            y1,
            win32con.SRCCOPY
        )

    release_screen(hdc)



def color_blocks(duration=5):
    hdc = get_screen()
    w, h = screen_size()

    start = time.time()

    while time.time() - start < duration:

        x = random.randint(0, w - 100)
        y = random.randint(0, h - 100)

        width = random.randint(20, 300)
        height = random.randint(20, 300)

        brush = win32gui.CreateSolidBrush(random_color())

        old = win32gui.SelectObject(hdc, brush)

        win32gui.PatBlt(
            hdc,
            x,
            y,
            width,
            height,
            win32con.PATCOPY
        )

        win32gui.SelectObject(hdc, old)
        win32gui.DeleteObject(brush)

    release_screen(hdc)



def circles(duration=5):
    hdc = get_screen()

    w, h = screen_size()

    start = time.time()

    while time.time() - start < duration:

        x = random.randint(0, w)
        y = random.randint(0, h)

        size = random.randint(10, 300)

        brush = win32gui.CreateSolidBrush(random_color())
        old = win32gui.SelectObject(hdc, brush)

        win32gui.Ellipse(
            hdc,
            x,
            y,
            x + size,
            y + size
        )

        win32gui.SelectObject(hdc, old)
        win32gui.DeleteObject(brush)

    release_screen(hdc)



def rectangles(duration=5):
    hdc = get_screen()

    w, h = screen_size()

    start = time.time()

    while time.time() - start < duration:

        x = random.randint(0, w)
        y = random.randint(0, h)

        width = random.randint(20, 400)
        height = random.randint(20, 400)

        brush = win32gui.CreateSolidBrush(random_color())

        old = win32gui.SelectObject(hdc, brush)

        win32gui.Rectangle(
            hdc,
            x,
            y,
            x + width,
            y + height
        )

        win32gui.SelectObject(hdc, old)
        win32gui.DeleteObject(brush)

    release_screen(hdc)



def lines(duration=5):
    hdc = get_screen()

    w, h = screen_size()

    start = time.time()

    while time.time() - start < duration:

        pen = win32gui.CreatePen(
            win32con.PS_SOLID,
            random.randint(1, 10),
            random_color()
        )

        old = win32gui.SelectObject(hdc, pen)

        win32gui.MoveToEx(
            hdc,
            random.randint(0, w),
            random.randint(0, h)
        )

        win32gui.LineTo(
            hdc,
            random.randint(0, w),
            random.randint(0, h)
        )

        win32gui.SelectObject(hdc, old)
        win32gui.DeleteObject(pen)

    release_screen(hdc)



def rgb_glitch(duration=5):
    hdc = get_screen()

    w, h = screen_size()

    start = time.time()

    while time.time() - start < duration:

        offset = random.randint(-30, 30)

        win32gui.BitBlt(
            hdc,
            offset,
            0,
            w,
            h,
            hdc,
            0,
            0,
            win32con.SRCCOPY
        )

        win32gui.BitBlt(
            hdc,
            -offset,
            0,
            w,
            h,
            hdc,
            0,
            0,
            win32con.NOTSRCCOPY
        )

    release_screen(hdc)



def waves(duration=5):
    hdc = get_screen()

    w, h = screen_size()

    start = time.time()
    t = 0

    while time.time() - start < duration:

        for y in range(0, h, 10):

            offset = int(
                math.sin(t + y * 0.03) * 30
            )

            win32gui.BitBlt(
                hdc,
                offset,
                y,
                w,
                10,
                hdc,
                0,
                y,
                win32con.SRCCOPY
            )

        t += 0.2

    release_screen(hdc)



def static(duration=5):
    hdc = get_screen()

    w, h = screen_size()

    start = time.time()

    while time.time() - start < duration:

        for _ in range(500):

            x = random.randint(0, w)
            y = random.randint(0, h)

            color = random_color()

            brush = win32gui.CreateSolidBrush(color)

            old = win32gui.SelectObject(hdc, brush)

            win32gui.PatBlt(
                hdc,
                x,
                y,
                3,
                3,
                win32con.PATCOPY
            )

            win32gui.SelectObject(hdc, old)
            win32gui.DeleteObject(brush)

    release_screen(hdc)



def spiral(duration=5):
    hdc = get_screen()

    w, h = screen_size()

    cx = w // 2
    cy = h // 2

    start = time.time()
    angle = 0

    while time.time() - start < duration:

        x = int(cx + math.cos(angle) * 300)
        y = int(cy + math.sin(angle) * 300)

        brush = win32gui.CreateSolidBrush(random_color())

        old = win32gui.SelectObject(hdc, brush)

        win32gui.Ellipse(
            hdc,
            x - 20,
            y - 20,
            x + 20,
            y + 20
        )

        win32gui.SelectObject(hdc, old)
        win32gui.DeleteObject(brush)

        angle += 0.1

    release_screen(hdc)



def random_invert(duration=5):
    hdc = get_screen()

    w, h = screen_size()

    start = time.time()

    while time.time() - start < duration:

        x = random.randint(0, max(0, w - 200))
        y = random.randint(0, max(0, h - 200))

        width = random.randint(20, 300)
        height = random.randint(20, 300)

        win32gui.BitBlt(
            hdc,
            x,
            y,
            width,
            height,
            hdc,
            x,
            y,
            win32con.NOTSRCCOPY
        )

    release_screen(hdc)