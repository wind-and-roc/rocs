from multiprocessing import Process 
import time 

# 自定义进程类
class ClockProcess(Process):
    def __init__(self,*args):
        super().__init__()
        self.value = args[0]
    
    def f1(self):
        print("Hello world")
    
    def f2(self):
        print("Hello Kitty")
    
    def f3(self):
        print(time.ctime())
    
    # 重写run方法
    def run(self):
        for i in range(5):
            time.sleep(self.value)
            self.f1()
            self.f2()
            self.f3()

# 创建进程对象
p = ClockProcess(2)
# 启动进程，执行run
p.start()
p.join()



