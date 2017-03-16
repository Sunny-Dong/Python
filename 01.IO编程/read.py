# -*- coding: utf-8 -*-
"""
Created on Thu Mar 16 12:50:04 2017

@author: sunnyday
"""

f=open('/Users/sunnyday/Documents/GitHub/Python/text.txt','r')  #/
f.read()
f.close()

with open('/Users/sunnyday/Documents/GitHub/Python/text.txt','r') as f:
    print(f.read())

f=open('/Users/sunnyday/Documents/GitHub/Python/text.txt','r')
for line in f.readlines():
    print(line.strip())     

f.read(6)

a=open('/Users/sunnyday/Documents/GitHub/Python/1.jpg','rb') ##二进制 图片

#要读取非UTF-8编码的文本文件，需要给open()函数传入encoding参数，
#例如，读取GBK编码的文件：
f = open('/Users/sunnyday/Documents/GitHub/Python/gbk.txt', 'r', encoding='gbk')
>>> '你好 中国'

##open()函数还接收一个errors参数，
#表示如果遇到编码错误后如何处理。最简单的方式是直接忽略：
 f = open('/Users/michael/gbk.txt', 'r', encoding='gbk', errors='ignore')
