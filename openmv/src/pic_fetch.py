# Untitled - By: cdog - 周四 11月 24 2022

import sensor, image, time

# 传感器设置部分, 无需勿改
sensor.reset()
sensor.set_pixformat(sensor.RGB565)
sensor.set_framesize(sensor.QVGA)
sensor.skip_frames(time = 2000)

clock = time.clock()

# 图片抓取主函数
while(True):
    clock.tick()
    img = sensor.snapshot()
    print(clock.fps())
