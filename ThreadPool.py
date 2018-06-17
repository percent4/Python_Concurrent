import math
import time
from concurrent.futures import ProcessPoolExecutor
unit = 100
PRIMES = [1,1*unit+1,2*unit+1]

def cal_pi(start):
    sum = 0
    for i in range(start, start+100, 1):
        sum += 1/(i**2)

    return sum

def main():
    t1 = time.time()
    sum = 0
    with ProcessPoolExecutor() as executor:
        for number, prime in zip(PRIMES, executor.map(cal_pi, PRIMES)):
            sum += prime

    print(sum)
    t2 = time.time()
    print(t2-t1)

if __name__ == '__main__':
    main()