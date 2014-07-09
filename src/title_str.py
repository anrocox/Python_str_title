#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on Jul 9, 2014

@author: anroco

How to convert strings title case in python?

Como convertir en mayuscula el primer caracter y el resto en minuscula de
cada palabra en un str python?
'''

#create a str
s = 'many years later, as he faced the firing squad'
print(s)

#the title() method generates copy of the string where words start with an
#uppercase character and the remaining characters are lowercase.
s_title = s.title()
print(s_title)
