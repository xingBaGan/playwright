# -*- encoding=utf8 -*-
__author__ = "jzj"

from airtest.core.api import *
import random
import threading

auto_setup(__file__)

# 预先生成一组随机坐标池
coordinate_pool = [(random.randint(520, 540), random.randint(1200, 1350)) for _ in range(100)]

def click_operation():
    while True:
        for x, y in coordinate_pool:
            touch([x, y], duration=0.001)
            

num_threads = 3  # 假设创建5个线程来并行执行点击操作
threads = []


for _ in range(num_threads):
    thread = threading.Thread(target=click_operation)
    thread.start()
    threads.append(thread)


for thread in threads:
    thread.join()
