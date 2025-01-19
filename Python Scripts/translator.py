# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 09:32:12 2024

@author: Cultivatewill
"""
import pathlib
from translate import Translator

translator = Translator(to_lang='ja')
p = pathlib.PurePath(r"C:\Users\Cultivatewill\Desktop\intro.txt")
with open(p,'r') as file:
    contents = file.read()
    
translation = translator.translate(contents)

print(translation)