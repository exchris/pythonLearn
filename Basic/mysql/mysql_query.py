#!/usr/bin/python
# -*- coding:utf-8 -*-

"""
Python查询Mysql使用 fetchone() 方法获取单条数据, 使用fetchall() 方法获取多条数据。

fetchone(): 该方法获取下一个查询结果集。结果集是一个对象
fetchall(): 接收全部的返回结果行.
rowcount: 这是一个只读属性，并返回执行execute()方法后影响的行数。
"""

import pymysql

# 打开数据库连接
db = pymysql.connect("127.0.0.1", "root", "root", "test")

# 使用cursor()方法获取操作游标
cursor = db.cursor()

# SQL查询语句
sql = "SELECT * FROM EMPLOYEE \
       WHERE INCOME > '%f' " %(1000)

try:
    # 执行SQL语句
    cursor.execute(sql)
    db.commit()
    # 获取所有记录列表
    results = cursor.fetchall()
    for row in results:
        fname = row[0]
        lname = row[1]
        age = row[2]
        sex = row[3]
        income = row[4]
        # 打印结果
        print("fname=%s,lname=%s,age=%d,sex=%s,income=%d" % \
              (fname, lname, age, sex, income))

except:
    print("Error: unable to fetch data")
    # 发生错误时进行回滚操作
    db.rollback()

# 关闭数据库连接
db.close()