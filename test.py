import mmap
import os
import struct
import fcntl

class Framebuffer:
    def __init__(self, fb_path="/dev/fb0"):
        self.fb = os.open(fb_path, os.O_RDWR)
        self.width, self.height = self._get_resolution()
        self.bpp = self._get_bpp()
        self.fbmem = mmap.mmap(self.fb, self.width * self.height * (self.bpp // 8), mmap.MAP_SHARED, mmap.PROT_WRITE | mmap.PROT_READ)

    def _get_resolution(self):
        with open("/sys/class/graphics/fb0/virtual_size", "r") as f:
            width, height = f.read().strip().split(",")
            return int(width), int(height)

    def _get_bpp(self):
        with open("/sys/class/graphics/fb0/bits_per_pixel", "r") as f:
            return int(f.read().strip())

    def draw_pixel(self, x, y, color):
        offset = (x + y * self.width) * (self.bpp // 8)
        self.fbmem[offset:offset + 4] = struct.pack("I", color)

    def fill_screen(self, color):
        for y in range(self.height):
            for x in range(self.width):
                self.draw_pixel(x, y, color)

    def draw_rect(self, x, y, w, h, color):
        for i in range(y, y + h):
            for j in range(x, x + w):
                if 0 <= j < self.width and 0 <= i < self.height:
                    self.draw_pixel(j, i, color)

    def close(self):
        self.fbmem.close()
        os.close(self.fb)

fb = Framebuffer()

# Fill screen black
fb.fill_screen(0x00000000)

# Draw red rectangle
fb.draw_rect(100, 100, 200, 150, 0x00FF0000)  # Red in BGRA
import time
time.sleep(3)
fb.close()
import os
os.system("clear")
