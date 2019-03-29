from multiprocessing import Pool 
from time import sleep,ctime 

# 进程事件
def worker(msg):
    sleep(2)
    print(msg)
    return ctime()

# 创建进程池
pool = Pool(4)

result = []
for i in range(10):
    msg = "Hello %d"%i
    r = pool.apply_async(func=worker,args=(msg,))
    result.append(r)
    
    # 同步执行
    # pool.apply(func=worker,args=(msg,))

# 关闭进程池
pool.close()

# 回收进程池
pool.join() 

for i in result:
    # 获取事件函数的返回值
    print(i.get())


