# -*- coding: utf-8 -*-
"""
Created on Fri Feb 18 15:37:15 2022

@author: Sckom
"""

from datetime import datetime

h = datetime.today().hour
m = datetime.today().minute
wd = datetime.today().isoweekday()
print(h,":",m,"\n День недели сегодня:",wd)