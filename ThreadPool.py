import time
from concurrent.futures import ThreadPoolExecutor, wait, ALL_COMPLETED

def task(index):
    time.sleep(1)
    print('This is %d'%index)

def main():

    t1 = time.time()
    for index in range(1, 10):
        task(index)
    t2 = time.time()
    print('不使用多线程，总共耗时：%s'%(t2-t1))

    print('\n'+'*'*80)
    t3 = time.time()
    executor = ThreadPoolExecutor(max_workers=4) # 可以自己调整max_workers
    # submit()的参数： 第一个为函数， 之后为该函数的传入参数，允许有多个
    future_tasks = [executor.submit(task, index) for index in range(1, 10)]
    wait(future_tasks, return_when=ALL_COMPLETED)
    t4 = time.time()
    print('使用多线程，总共耗时：%s'%(t4-t3))

main()