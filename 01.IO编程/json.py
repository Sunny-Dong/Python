# -*- coding: utf-8 -*-
"""
Created on Thu Mar 16 14:40:32 2017

@author: sunnyday
"""

import json
d=dict(name='Kawhi Leonard',age=25,height=2.01)
json.dumps(d)
a='{"age": 25, "name": "Kawhi Leonard", "height": 2.01}'
json.loads(a)