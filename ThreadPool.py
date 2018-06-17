import math
import time
from concurrent.futures import ThreadPoolExecutor, wait, ALL_COMPLETED

def task(i):
    time.sleep(1)
    print('这是第%d个任务'%i)

def main():

    t1 = time.time()

    for i in range(1, 10):
        task(i)

    t2 = time.time()
    print('不使用多线程，总共耗时：%s'%(t2-t1))

    t3 = time.time()

    executor = ThreadPoolExecutor(max_workers=20)  # 可以自己调整max_workers
    # submit()的参数： 第一个为函数， 之后为该函数的传入参数，允许有多个
    future_tasks = [executor.submit(task, i) for i in range(1, 21)]
    wait(future_tasks, return_when=ALL_COMPLETED)

    t4 =time.time()
    print('使用多线程，总共耗时：%s' % (t4 - t3))

main()
