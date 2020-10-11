# -*- coding: utf-8 -*-
"""
Created on Fri Sep 18 12:25:03 2020

@author: SOPHIE
"""
from file import File

ma_file = File([11,22,33,44,55])
ma_file.printFile()
ma_file.enfiler(66)
print(ma_file.premier(),ma_file.dernier(),ma_file.getNb_elements())
long_ma_file = ma_file.getNb_elements()
for i in range(long_ma_file):
    print(ma_file.defiler())
print(ma_file.defiler())
ma_file2 = File()
print(ma_file2.premier(),ma_file2.dernier(),ma_file2.getNb_elements())