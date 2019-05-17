#!/usr/bin/python
# coding:utf-8
''' the number of one in binary '''

def theone(n):
    count=0
    for i in range(0,32):
        if n&1:
            count += 1
        n=n>>1
    return count

n=input("Please input an integer:")
print(theone(n))

                   
