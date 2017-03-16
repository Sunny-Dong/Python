# -*- coding: utf-8 -*-
"""
Created on Thu Mar 16 13:25:46 2017

@author: sunnyday
"""

#要把str写入StringIO，我们需要先创建一个StringIO，
#然后，像文件一样写入即可：
from io import StringIO
f = StringIO()
f.write('hello')
f.write(' ')
f.write('world!')
f.getvalue()  ##显示写入后的值

          
#要读取StringIO，可以用一个str初始化StringIO，然后，像读文件一样读取：
from io import StringIO
f = StringIO('Hello!\nHi!\nGoodbye!')
while True:
    s=f.readline()
    if s=='':  ##''之间没有空格
       break
    print(s.strip())
    
from io import BytesIO
f=BytesIO('中文'.encode('utf-8'))  ##写入
f.getvalue()
f.read()
    
a=StringIO()
a.write('Hell0')
a.seek(0)
a.readline()
b=StringIO('Hello')
b.readline()