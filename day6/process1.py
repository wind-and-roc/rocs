import multiprocessing as mp 
from time import sleep 

a = 1

# 编写进程函数
def fun():
    sleep(6)
    print("进程执行的事件")

    global a 
    print("a = ",a)
    a = 10000

# 创建进程对象
p = mp.Process(target = fun)

# 启动进程
p.start() 

sleep(2)
print("父进程事件")

# 回收进程
p.join(1)

print("parent a:",a)
while True:
    pass 

