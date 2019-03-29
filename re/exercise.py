import re 

f = open('test.txt')

data = f.read()

#首字母大写单词
# pattern = r'\b[A-Z]\S*\b'

#匹配数字
# pattern = r'-?\d+\.?/?\d*%?'

#日期替换: 2018.7.12改为2018-7-12
pattern = r'\d{4}\.\d{1,2}\.\d{1,2}'  
regex = re.compile(pattern)
for i in regex.finditer(data):
    # print(i.group())
    s = i.group()
    print(re.sub(r'\.', '-', s))