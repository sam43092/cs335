#!/usr/bin/python -tt


for i in [11,9,0,7,2]:
    try:
        print 100/i
    except ZeroDivisionError:
        print "You can not divide by zero!!!"
    