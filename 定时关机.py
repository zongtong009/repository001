# -*- coding: utf-8 -*-
import time
import os


def time_end():
    for i in range(70):
        print("\r本程序还有%.1f秒关闭" % (0.1 * (70 - i)), end='')
        time.sleep(0.1)


def main():
    print("输入 off 取消任务 ")
    while True:
        time_in = input('请输入关机时间,格式如："小时：分钟": ')
        if time_in == 'off':
            print(123)  # 取消关机任务
            os.system("shutdown -a")
            input_end = input("输入end结束,输入其他继续: ")
            if input_end == "end":
                return
        elif len(time_in) >= 3:
            if time_in[2] == ':' or time_in[2] == '：':
                break
        else:
            continue
    try:
        h1 = int(time_in[0:2])
        m1 = int(time_in[3:5])
        my_time = time.strftime("%H:%M:%S")  # 当前时间
        h2 = int(my_time[0:2])
        m2 = int(my_time[3:5])
        if h1 > 24:
            h1 = 24
            m1 = 0  # 大于24点按24:00算
        if m1 > 60:
            m1 = 60  # 大于60分按60算
        if h1 * 60 + m1 <= h2 * 60 + m2:  # 判断time1>time2
            h1 = h1 + 24
        s1 = ((h1 * 60 + m1) - (h2 * 60 + m2)) * 60  # 秒
        if s1 <= 0:
            print('error')
        else:  # h m s ->>时分秒
            h = s1 // 3600
            m = (s1 - h * 3600) // 60
            s = s1 - h * 3600 - m * 60
            print("距离关机还有 %d 小时%d 分 %d 秒" % (h, m, s))
            os.system("shutdown -s -t %d" % s1)
        return
    except ValueError:
        main()


if __name__ == "__main__":
    main()
    time_end()
