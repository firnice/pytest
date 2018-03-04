
# This Python file uses the following encoding: utf-8
# -*- coding: utf-8 -*-
#指定编码方式
import urllib2 #导入urllib2库

response = urllib2.urlopen('http://www.baidu.com') #打开网址
html = response.read() #读出网址源码
#print html #在控制台中输出
with open('baidu.html','w') as f:
    f.write(html) #将html写入文件中