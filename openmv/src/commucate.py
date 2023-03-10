# Untitled - By: cdog - 周四 11月 24 2022

import sensor, image, time
from pyb import UART

DISTANCE_CONSTANT = 23*240  # 测距常量, 勿动

color_dic = {1:"k", 2:"b", 4:"r", 8:"g"}  # 定义颜色字典

# 定义颜色值
black = (0, 6, -10, 1, 8, -128)
blue = (16, 0, 18, -13, -10, -36)
red = (21, 100, 14, 63, -11, 59)
green = (34, 47, -57, -16, -128, 127)

COMport = UART(3, 115200)  # 定义串口, 需要自行匹配COM号

# 传感器设置部分, 无需勿改
sensor.reset()
sensor.set_pixformat(sensor.RGB565)
sensor.set_framesize(sensor.QVGA)
sensor.skip_frames(time = 2000)

clock = time.clock()

while(True):
    clock.tick()
    img = sensor.snapshot()
    #img.draw_line((107,0,107,240), (255,0,0))
    #img.draw_line((213,0,213,240), (255,0,0))
    all_blobs = img.find_blobs([black,blue,red,green])  # 查找哪些色块

    for blob in all_blobs:
        x = blob.x()
        y = blob.y()
        center = blob.x()+blob.w()/2
        pos = ""

        #blob filter
        if blob.h()*blob.w() < 1500:  # 小块过滤
            continue

        if blob.h()/blob.w()<0.85 or blob.w()/blob.h()<0.85:  #异形块过滤
            continue

        #postision dectect
        if center > 107:
            if center < 213:
                pos = "m"
            else:
                pos = "r"
        else:
            pos = "l"

        #distance calc
        distance = DISTANCE_CONSTANT/((blob.h()+blob.w())/2)

        #msg out
        remind = 'c'+color_dic[blob.code()] + "s" + pos + "d" + str(int(distance)) + ' '
        img.draw_rectangle(blob.rect())
        img.draw_string(x, y, remind)

        #COM commuicate
        COMport.write(remind)
