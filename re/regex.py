import re
# s = 'zhang:1994 li:1995'
# pattern = r'(\w+):(\d+)'

#re模块调用  @@@@@@
# l = re.findall(pattern,s)
# print(l)

# regex 对象 @@@@@@
# regex = re.compile(pattern)
# l = regex.findall(s)
# print(l)

# l = re.split(r'\s+','hello     world')
# print(l)   

# s = re.subn(r'垃圾', '**', '前面，有垃圾,有垃圾,有垃圾',2)
# print(s)

s = "2019年4月28日"
pattern = r'\d+'

it = re.finditer(pattern,s)

# print(dir(next(it)))
# match 对象 @@@@@
for i in it:
    print(i.group())  # 获取match 对象匹配到的内容

obj = re.fullmatch(r'\w+','hello_world')
print(obj.group())    #　这里最好用try

#匹配开头
obj = re.match(r'[A-Z]\w+','Hello,world')
print(obj.group())    #　这里最好用try

# 匹配第一处
obj = re.search(r'\d+','今天2019-3-28')
print(obj.group())    #　这里最好用try    