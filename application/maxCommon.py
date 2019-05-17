#!/usr/bin/python
# coding:utf-8
'''  maxCommon '''

def maxCommon(a,b):
    if a>b:
        value=b
    else:
        value=a
    for i in range(1,value+1）：
        if ((a%i==0) and (b%i==0)):
                   maxCommon=i
    return maxCommon

a=int(input('Please enter an integer:'))
b=int(input('Please enter an integer:'))
print(maxCommon(a,b))

                   
