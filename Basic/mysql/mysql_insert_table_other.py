#!/usr/bin/python
# -*- coding:utf-8 -*-

import pymysql

# 打开数据库连接
db = pymysql.connect("127.0.0.1", "root", "root", "test")

# 使用cursor()方法获取操作游标
cursor = db.cursor()

# SQL插入语句
sql = "INSERT INTO EMPLOYEE(FIRST_NAME, \
    LAST_NAME, AGE, SEX, INCOME ) \
    VALUES('%s', '%s', '%d', '%c', '%f')" % \
    ('Mac', 'Mohan', 20, 'M', 2000)

try:
    # 执行sql语句
    cursor.execute(sql)
    # 执行sql语句
    db.commit()
except:
    # 发生错误时回滚
    db.rollback()

# 关闭数据库连接
db.close()