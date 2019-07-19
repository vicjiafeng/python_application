#!/usr/bin/python
# coding:utf-8
'''  midNum '''

def midNum(L):
    L = sorted(L)
    l = len(data)
    if l%2 == 0:
        m = (L[int((l//2)-1)]+L[int(l//2)]) / 2
        print("%.1f" % m)
    else:
        m = L[int((l-1)//2)]
        print(m)
              
L=[3,2,4,5,1,6]
midNum(L)
                   
