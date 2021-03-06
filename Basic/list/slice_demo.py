#!/usr/bin/python
# coding:utf-8

# 切片

"""
取一个list或tuple的部分元素是非常常见的操作。
比如，一个list如下：
"""
L = ['Michael', 'Sarah', 'Tracy']
# 取前3个元素，用一行代码可以完成切片
# L[0:3]表示，从索引0开始取，直到索引3为止，但不包括索引3。即索引0,1,2，正好是3个元素
print("L列表中前3个元素为  : ", L[0:3])
# 如果第一个索引是0，还可以省略
print("L列表中前3个元素为  : ", L[:3])
# 从索引1开始，取出2个元素出来
print("L列表中索引从1开始，取2个元素", L[1:3])
# Python支持L[‐1] 取倒数第一个元素，那么它同样支持倒数切片
print(L[-2:])
print(L[-2:-1])

# 创建0-99的数列
L = list(range(100))
print(L)
# 前10个数
print(L[:10])
# 后10个数
print(L[-10:])
# 前11-20个数
print(L[10:20])
# 前10个数，每两个取一个
print(L[:10:2])
# 所有数，每5个取一个
print(L[::5])
# [:]原样复制一个list
print(L[:])

# tuple也是一种list,唯一区别是tuple不可变。因此tuple也可以用切片操作，只是操作的结果仍是tuple
print((0,1,2,3,4,5)[:3])
# 字符串'xxx' 或Unicode字符串u'xxx' 也可以看成是一种list，每个元素就是一个字符。因此，字符串也可以用切片
# 操作，只是操作结果仍是字符串：
print('ABCDEFG'[:3])
print('ABCDEFG'[::2])