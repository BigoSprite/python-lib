# -*- coding: utf-8 -*-


# 缩进
try:
    x = 100
     y = 200 # 抛出异常
except IndentationError:
    print('IndentationError: unexpected indent')

# 单行注释
'''
多行注释
多行注释
'''

# 多行代码
str = 'abcd' \
          'efgh'
print(str)

# 多行字符串
str = 'Hello\nworld'
print(str)
str = """Hello
world"""
print(str)
