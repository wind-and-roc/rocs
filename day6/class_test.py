from multiprocessing import Process 

class Process(object):
    def __init__(target=xx,args=xx,name=xx):
        .....
    
    def start(self):
        self.run()
    
    def join():
        ...
    
    def run():
        pass

Class Test(Process):
    def __init__(self,value):
        self.value = value 
        super(Test,self).__init__()
    
    def run():
        ...

t = Test()
t.start()