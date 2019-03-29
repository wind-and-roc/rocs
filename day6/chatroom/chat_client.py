from socket import * 
import os,sys 

# 服务端地址
ADDR = ('172.40.91.197',8888)

def send_msg(s,name):
    while True:
        try:
            text = input("发言:")
        except KeyboardInterrupt:
            text = 'quit'
        # 输入quit表示退出聊天室
        if text.strip() == 'quit':
            msg = 'Q ' + name 
            s.sendto(msg.encode(),ADDR)
            sys.exit("退出聊天室")
        msg = "C %s %s"%(name,text)
        s.sendto(msg.encode(),ADDR)

def recv_msg(s):
    while True:
        data,addr = s.recvfrom(1024)
        if data.decode() == 'EXIT':
            sys.exit()
        print(data.decode()+'\n发言:',end='')

# 创建网络连接
def main():
    s = socket(AF_INET,SOCK_DGRAM)

    while True:
        name = input("请输入姓名:")
        msg = 'L ' + name
        # 发送请求
        s.sendto(msg.encode(),ADDR)
        #等待回复
        data,addr = s.recvfrom(1024)
        if data.decode() == 'OK':
            print("您已进入聊天室")
            break
        else:
            print(data.decode())
    
    # 创建进程
    pid = os.fork()
    if pid < 0:
        return 
    elif pid == 0:
        send_msg(s,name)
    else:
        recv_msg(s)

main()