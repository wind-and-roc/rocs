import threading 
def show1():
    for i in range(1,52,2):
        lock_show2.acquire()
        print(i,end="")
        print(i+1,end="")
        lock_show3.release()

def show2():
    for i in range(26):
        lock_show1.acquire()
        print(chr(i+ord('A')),end=" ")
        lock_show1.release()
def show3():
    for i in range(26):
        lock_show3.acquire()
        print('show3')        
        lock_show2.release()
lock_show1= threading.Lock()
lock_show2= threading.Lock()
lock_show3= threading.Lock()
show1_thread = threading.Thread(target = show1)
show2_thread = threading.Thread(target = show2)
show3_thread = threading.Thread(target = show3 )

lock_show3.acquire() #因为线程执行顺序是无序的,保证show1()先执行
lock_show1.acquire()
show1_thread.start()
show2_thread.start()
show3_thread.start()
