# -*- coding: utf-8 -*-
"""
Created on Thu Mar 16 14:24:58 2017

@author: sunnyday
"""

import pickle
d=dict(name='Kawhi Leonard',age=25,height=2.01)
pickle.dumps(d)

f=open('dump.txt','wb')  ##自动创建dump.txt
pickle.dump(d,f)
f.close()

f=open('dump.txt','rb')
d=pickle.load(f)
f.close()
d    # {'age': 25, 'height': 2.01, 'name': 'Kawhi Leonard'}