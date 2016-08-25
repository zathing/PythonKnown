# -*- coding: utf-8 -*-
'''
功能：检验字符串中是否存在相同的字符
重点：如何在找到一对相同的字符之后就停止双重循环？
'''

# 传统做法：使用布尔值标志位，找到一对相同的字符后修改标志位状态
my_string = "This is a string to test"
mark = False
for i in range(len(my_string)):
    if not mark:
        for j in range(i+1, len(my_string)):
            if my_string[i] == my_string[j]:
                print my_string[i]
                mark = True
                break

# 更高端的做法： 使用生成器生成需要的索引对，将双重循环抽象到生成器内部
def unique_pairs(n):
    for i in range(n):
        for j in range(i+1, n):
            yield i, j

my_string = "This is a string to test"
for i,j in unique_pairs(len(my_string)):
    if my_string[i] == my_string[j]:
        print my_string[i]
        break