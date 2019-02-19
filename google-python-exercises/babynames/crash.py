#!/usr/bin/python -tt

import os

files = ['baby1990.html', 'bab1992.html'];

for file in files:
        f = open(file, 'rU')
        print f.name
        