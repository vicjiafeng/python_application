#!/usr/bin/python
# coding:utf-8
'''  minCommon '''

def minCommon(a,b):
    if a>b:
        value=a
    else:
        value=b
    while True:
        if ((value%a==0) and (value%b==0)):
                   minCommon=value
                   break
        value += 1               
    return minCommon

a=int(input('Please enter an integer:'))
b=int(input('Please enter an integer:'))
print(minCommon(a,b))

                   
