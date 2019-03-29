from multiprocessing import Pool 
import time 

def fun(n):
    time.sleep(2)
    return n * n 

pool = Pool(4)

r = pool.map(fun,[1,2,3,4,5])

pool.close()
pool.join()

print("结果:",r)
