#!/usr/bin/python
# coding:utf-8
'''  字符串匹配  '''

#第一种低效的方法，时间复杂度O(mxn)
def str_matching(t,p):
    m, n = len(t), len(p)
    i, j = 0, 0
    while i < m and j < n:           #i==m, 说明找到匹配
        if p[i] == t[j]:             #字符相同，考虑下一对
            i, j = i+1, j+1
        else:                        #字符不同，考虑t的下一个位置
            i, j = 0, j-i+1
    if i == m:                       #找到匹配，返回位置下标
        return j-i
    return -1                        #无匹配，返回特殊值

                   


'''
    灵活的kmp方法(不存在回溯)实现字符串匹配，复杂度为O(n)
    对于模式串中每个字符Pi设置对应的P<sub>ki</sub>,用Pki与目标串tj比较，在匹配之前，就可以先安排好模式串中每个字符对应的Pki
'''
def str_kmp_matching(t,p,pnext):    #表pnext记录模式串m每个字符i对应的Ki值
    j, i = 0, 0
    n, m = len(t), len(p)
    while j < n and i < m:            #若i==m，找到匹配
        if i == -1 or t[j] == p[i]:   #考虑p中下一个字符, pnext[0]=-1 表示从头开始匹配，即p0匹配与t(j+1)比较
            j, i = j+1, i+1
        else:                         #失败
            i = pnext[i]              #从表pnext取得p的下一个字符位置
    if i==m:                          #找到匹配，返回下标
        return j-1
    return -1                         #无匹配，返回特殊值

'''
    目标串中子串tj-i...tj-1就是p0...pi-1(tj!=pi),之后比较pk与tj,则模式串子串p0...pk-1与pi-k...pi-1匹配
    确定k的问题变成确定p0...pi-1的相等前后缀长度,当 pi=pk =》pnext[k]=k
'''
def gen_pnext(p):
    i,k,m = 0,-1,len(p)
    pnext = [-1]*m                    #初识时元素都设为1
    while i < m-1:                    #生成下一个pnext元素
        if k == -1 or p[i] == p[k]:
            i,k = i+1,k+1
            pnext[i]= k               #设置pnext元素
        else:
            k=pnext[k]                #退到更短相同前缀
    return pnext

