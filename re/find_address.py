import re
import sys,os
def findAddress():
    port = sys.argv[1]
    print(port)
    f = open('1.txt')
    #找到端口所在段落
    while True:
        data = ''
        for line in f:
            
            if line != '\n':
                data += line
            else:
                break
               
            if not data:
                print('No PORT')
                break
        
        #获取每一段首单词 10.124.3.85/24
        try:
            PORT = re.match(r'\S+',data).group()
            print("PORT",PORT)
        except Exception:
            continue
        if PORT == port:
            pattern = r'([0-9a-f]{4}\.[0-9a-f]{4}\.[0-9a-f]{4})|(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{2,3}\/\d{2,3})'
             
            address = re.search(pattern,data).group()
            print("patt ",address)
            break        
    f.close()

findAddress()    