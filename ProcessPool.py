# 利用多进程计算pi值
# pi**2/6 = 1+1/(2*2)+1/(3*3)+1/(4*4)+...+1/(n*n)+...

import time
import math
from concurrent.futures import ProcessPoolExecutor, as_completed

def cal_pi1(start):
    sum = 0
    for i in range(start, start+5000000, 1):
        sum += 1/(i**2)

    return sum

def cal_pi2(start, end):
    sum = 0
    for i in range(start, end, 1):
        sum += 1 / (i ** 2)

    return sum

if __name__ == '__main__':

    t1 = time.time()
    sum = cal_pi2(1, 50000000)
    pi = math.sqrt(sum*6)

    t2 = time.time()
    print('不使用多进程，计算结果为：%s, 总共耗时：%s'%(pi, t2-t1))


    t3 = time.time()

    unit = 5000000
    PRIMES = [i*unit+1 for i in range(10)]

    sum = 0
    with ProcessPoolExecutor(max_workers=2) as executor:
        for number, prime in zip(PRIMES, executor.map(cal_pi1, PRIMES)):
            sum += prime

    pi = math.sqrt(sum * 6)

    t4 = time.time()
    print('使用多进程，计算结果为：%s, 总共耗时：%s' % (pi, t4 - t3))
