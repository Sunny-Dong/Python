# -*- coding: utf-8 -*-
"""
Created on Thu Mar 16 13:56:16 2017

@author: sunnyday
"""

import os
os.name #操作系统
os.environ #环境变量

#操作文件和目录的函数一部分放在os模块中，一部分放在os.path模块中
# 查看当前目录的绝对路径:
os.path.abspath('.')
'/Users/michael'
# 在某个目录下创建一个新目录，首先把新目录的完整路径表示出来: 即文件夹
os.path.join('/Users/sunnyday/Documents/GitHub/Python', 'testdir')
'/Users/michael/testdir'
# 然后创建一个目录:
os.mkdir('/Users/sunnyday/Documents/GitHub/Python/testdir')
# 删掉一个目录:
os.rmdir('/Users/sunnyday/Documents/GitHub/Python/testdir')

#把两个路径合成一个时，不要直接拼字符串，而要通过os.path.join()函数，
#这样可以正确处理不同操作系统的路径分隔符。
#要拆分路径时，也不要直接去拆字符串，而要通过os.path.split()函数，
#这样可以把一个路径拆分为两部分，后一部分总是最后级别的目录或文件名：
os.path.splitext('/path/to/file.txt') #直接得到文件扩展名

#这些合并、拆分路径的函数并不要求目录和文件要真实存在，
#它们只对字符串进行操作。
os.rename('test.txt', 'test.py')
os.remove('test.py')


#shutil模块提供了copyfile()的函数

#列出当前目录下的所有目录，只需要一行代码：
[x for x in os.listdir('.') if os.path.isdir(x)]

#要列出所有的.py文件
[x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1]=='.py']


                    
