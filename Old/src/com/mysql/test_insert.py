# -*- coding:UTF-8 -*-

import MySQLdb

# 打开数据库连接
db = MySQLdb.connect("localhost","root","root","ttpaobu")

# 使用cursor()方法获取操作游标
cursor = db.cursor()

# SQL插入语句
sql = """INSERT INTO EMPLOYEE(FIRST_NAME,
LAST_NAME,AGE,SEX,INCOME)
VALUES('Mac','Mohan',20,'M',2000)        
"""

try:
    # 执行sql语句
    cursor.execute(sql)
    # 提交到数据库执行
    db.commit()
    # 返回影响行数
    print(cursor.rowcount)
except:
    # Rollback in case there is any error
    db.rollback()
    print("插入失败")

# 关闭游标
cursor.close()
# 关闭数据库连接
db.close();