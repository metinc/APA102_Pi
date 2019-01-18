from driver import apa102

strip = apa102.APA102(num_led=11, global_brightness=100, mosi = 10, sclk = 11,
                              order='rgb')
strip.clear_strip()