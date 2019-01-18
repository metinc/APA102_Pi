from driver import apa102

strip = apa102.APA102(num_led=11, global_brightness=100, mosi = 10, sclk = 11,
                              order='rgb')
strip.clear_strip()

for led in range(0, strip.num_led):
    strip.set_pixel_rgb(led, 0x0000FF, 100) # set to blue with 100 % brightness
strip.show()