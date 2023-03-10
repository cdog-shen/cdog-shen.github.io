# Untitled - By: cdog - 周六 11月 26 2022

import sensor, image, time

DISTANCE_CONSTANT = 23*240  # 测距常量, 勿动

# 定义颜色值
black = (0, 6, -10, 1, 8, -128)
blue = (16, 0, 18, -13, -10, -36)

# 传感器设置部分, 无需勿改
sensor.reset()
sensor.set_pixformat(sensor.RGB565)
sensor.set_framesize(sensor.QVGA)
sensor.set_auto_whitebal(False)
sensor.skip_frames(time = 2000)

clock = time.clock()

while(True):

    clock.tick()
    img = sensor.snapshot()
    all_blobs = img.find_blobs([black, blue])
    for blob in all_blobs:

        #blob filter
        if blob.h()*blob.w() < 1200:
            continue

        #distance calc
        distance = DISTANCE_CONSTANT/((blob.h()+blob.w())/2)

        #info out
        x = blob.x()
        y = blob.y()
        remind = "c:" +str(blob.code()) + " " + "d:" + str(int(distance))
        img.draw_rectangle(blob.rect())
        img.draw_string(x, y, remind)
