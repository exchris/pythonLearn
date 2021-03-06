#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/7/28 0028 下午 2:56
# @Author  : Exchris Tsai
# @Site    : 
# @File    : images_tiebaone.py
# @Software: PyCharm

__author__ = 'Exchris Tsai'

# 爬取贴吧图片,网址: http://tieba.baidu.com/p/2166231880
import urllib.request
import re
import os

def fetch_pictures(url):
    html_content = urllib.request.urlopen(url).read()
    r = re.compile('<img pic_type="0" class="BDE_Image" src="(.*?)"')
    picture_url_list = r.findall(html_content.decode('utf-8'))

    os.mkdir('pictures')
    os.chdir(os.path.join(os.getcwd(),'pictures'))
    for i in range(len(picture_url_list)):
        picture_name = str(i) + '.jpg'
        try:
            urllib.request.urlretrieve(picture_url_list[i],picture_name)
            print("Success to download" + picture_url_list[i])
        except:
            print("Fail to download" + picture_url_list[i])

if __name__ == "__main__":
    fetch_pictures("http://tieba.baidu.com/p/2166231880")