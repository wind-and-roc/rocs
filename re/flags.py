import re 

s = '''Welcome to 
达内
'''
#只匹配ASCII字符
# regex = re.compile(r'\w+')

# l = regex.findall(s)

# regex = re.compile(r'\w+', flags = re.A)

# ^ $ 可以匹配每一行的开头结尾位置
# regex = re.compile(r'达内', flags = re.M)

# 为正则表达式添加注释
pattern = r'''[A-Z]\W+    #第一个单词
\s+\w+\s+     # 空格和第二个单词
\S+          # 匹配汉字    
'''

l = regex.findall(s)
print(l)