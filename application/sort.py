#!/usr/bin/python
# coding:utf-8
''' insert_sort '''
def insert_sort(lst):                #插入排序
    for i in range(1,len(lst)):
        x = lst[i]
        j = i
        for j > 0 and lst[j].key > x.key:
            lst[j] = lst[j-1]            #逐个后移元素
            j -= 1
    lst[j] = x

''' select_sort '''
def select_sort(lst):                 #选择排序
    for i in range(len(lst)-1):
        k = i
        for j in range(i,len(lst)):
            if lst[j].key < lst[k].key:
                k = j
        if i != k:                      lst[k]是确定最小元素，检查是否交换
            lst[i], lst[k] = lst[k], lst[i]

''' bubble_sort '''
def bubble_sort(lst):                         #交换排序（冒泡排序）
    for i in range(len(lst)):
        for j in range(1,len(lst)-i):
            if lst[j-1].key > lst[j].key:
                lst[j], lst[j-1] = lst[j-1], lst[j]

''' quick_sort '''
#快速排序, 时间复杂度O(nlogn), 空间复杂度O(n)，不稳定不适应
def quick_sort(lst,l,r):
    if l >= r:
        return
    i = l
    j = r
    pos = lst[i]                    #lst[i]是初始位置
    while i < j:
        while i < j and lst[j].key > pos.key:
            j -= 1                  #向左扫描小于pos的记录
        if i < j:
            lst[i] = lst[j]
            i += 1                  #小记录向左移
        while i < j and lst[i].key <= pos.key:
            i += 1                  #i向右扫描大于pos的记录
        if i < j:
            lst[j] = lst[i]
            j -= 1                  #大记录移到右边
    lst[i] = pos                     #存入pos
    quick_sort(lst,l,i-1)           #递归左半区
    quick_sort(lst,i+1,r)           #递归右半区

def quick_sort1(lst,begin,end):
    if begin > end:
        return
    pos = lst[begin].key
    i = begin
    for j in range(begin+1, end+1):
        if lst[j].key < pos:
            i += 1
            lst[i], lst[j] = lst[j], lst[i]            #小元素换位
    lst[begin], lst[i] = lst[i], lst[begin]
    quick_sort1(lst,begin,i-1)
    quick_sort1(lst,i+1,end)

''' merge-sort '''
#稳定性，无适应性
#归并排序，表lfrom表示被归并的有序段，表lto保存归并结果
def merge(lfrom,lto,low,mid,high):
    i,j,k=low,mid,low
    while i < mid and j < high:
        if lfrom[i].key <= lfrom[j].key:
            lto[k] = lfrom[i]
            i += 1
        else:
            lto[k] = lfrom[j]
            j += 1
        k += 1
    while i < mid:                           #复制第一段剩余记录
        lto[k] = lfrom[i]
        i += 1
        k += 1
    while j < high:                          #复制第2段剩余记录
        lto[k] = lfrom[j]
        j += 1
        k += 1
#merge_paa实现一对对分段的一遍归并，llen表示表长度,slen表示分段长度
def merge_pass(lfrom,lto,llen,slen):
    i = 0
    while i + 2*slen < llen:
        merge(lfrom,lto,i,i+slen,i+2*slen)
        i += 2*slen
    if i + slen < llen:
        merge(lfrom,lto,i,i+slen,llen)         #剩下两段，后一段长度小于slen
    else:
        for i in range(i,llen):                #只剩下一段，复制到表lto
            lto[j] = lfrom[j]

def merge_sort(lst):
    slen,llen = 1,len(lst)
    templst = [None]*llen
    while slen < llen:
        merge_pass(lst,templst,llen,slen)
        slen *= 2
        merge_pass(templst,lst,llen,slen)        #由于结果可能在templst表中，所以在复制一次lst表
        slen *= 2




