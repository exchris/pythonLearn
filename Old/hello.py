"""
Created on 八月 02 2017
@author: dev.erxuan@gmail.com
"""
# -*- coding: utf-8 -*-
# 一个最小的Flask应用
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

if __name__ == "__main__":
    app.run()


