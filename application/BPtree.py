#!/usr/bin/python
# coding:utf-8
'''  B+Tree '''
'''
* the difference between b_tree and b+_tree
b+树改进了叶子节点和内节点数据结构设计，查询效率更高，都要查找到叶子节点（有序链表），储存元素更多
特点：
1.有k个子树的中间节点包含k个元素（b树中是k-1），每个元素不保存数据，只用来索引，数据保存在叶子节点
2.所有叶子节点中包含全部元素信息，及指向含这些元素记录的指针，且从小到大顺序链接
3.所有中间节点元素都y同时存在子节点元素中（最大或最小）
'''
from collections import deque
'''
* insert data
'''
def bisect_right(a,x,l=0,h=None):
    if l<0:
        raise ValueError('l must be non-negative')
    if h is None:
        h = len(a)
    while l<h:
        mid = (l+h)//2
        if x < a[mid]:
            h = mid
        else:
            l = mid + 1
    return l
def bisect_left(a,x,l=0,h=None):
    if l<0:
        raise ValueError('l must be non-negative')
    if h is None:
        h = len(a)
    while l<h:
        mid = (l+h)//2
        if x > a[mid]:
            l = mid + 1
        else:
            h = mid
    return l

class InitError(Exception):
    pass
class ParaErrot(Exception):
    pass
class KeyValue(object):
    __slots__=('key','value')
    def __init__(self,key,value):
        self.key = key
        self.value = value
    def __str__(self):
        return str((self.key,self.value))
    def __cmp__(self,key):
        if self.key > key:
            return 1
        elif self.key == key:
            return 0
        else:
            return -1
class BPTree_InterNode(object):
    def __init__(self,M):
        if not isinstance(M,int):
            raise InitError, 'm must be int'
        if M <= 3:
            raise InitError, 'm must be great than 3'
        else:
            self.__M = M
            self.clist=[]        #
            self.ilist=[]        #索引节点信息
        self.par = None
    def isleaf(self):
        return False
    def isfull(self):
        return len(self.ilist) >= self.M - 1
    def isempty(self):
        return len(self.ilist) <= (self.M + 1) / 2 - 1
    @property
    def M(self):
        return self.__M
class BPTree_Leaf(object):
    def __init__(self,L):
        if L > M:
            raise InitError, 'L must be less or equal than M'
        else:
            self.__M = M
            self.__L = L
            self.__root = BPTree_Leaf(L)
            self.__leaf = self.__root

    @property
        def M(self):
            return self.__M
    @property
        def L(self):
            return self.__L
    def insert(self,key_value):
        node = self.__root
        def split_node(n1):
            mid = self.M / 2
            newnode = BPTree_InterNode(self.M)
            newnode.ilist = n1.ilist[mid:]
            newnode.clist = n1.clist[mid:]
            newnode.par = n1.par

            for c in newnode.clist:
                c.par = newnode
            if n1.par is None:
                newroot = BPTree_InterNode(self,M)
                newroot.ilist = [n1.ilist[mid-1]]
                newroot.clist = [n1, newnode]
                n1.par = newnode.par = newroot
                self.__root = newroot
            else:
                i = n1.par.clist.index(n1)
                n1.par.ilist.insert(i,n1.ilist[mid-1])
                n1.par.clist.insert(i+1,newnode)
            n1.ilist = n1.ilist[:mid-1]
            n1.clist = n1.clist[:mid]
            return n1.par
        def split_leaf(n2):
            mid = (self.L+1)/2
            newleaf=BPTree_Leaf(self,L)
            newleaf.vlist=n2.vlist[mid:]
            if n2.par==None:
                newroot=BPTree_InterNode(self.M)
                newroot.ilist=[n2.vlist[mid].key]
                newroot.clist=[n2,newleaf]
                n2.par=newleaf.apr=newroot
                self.__root=newroot
            else:
                i=n2.par.clist.index(n2)
                n2.par.ilist.insert(i,n2,vlist[mid],key)
                n2.par.clist.insert(i+1,newleaf)
                newleaf.par=n2.par
            n2.vlist=n2.vlist[:mid]
            n2.bro=newleaf
        def insert_node(n):
            if not n.isleaf():
                if n.isfull():
                    insert_node(split_node(n))
                else:
                    p=bisect_right(n.list,key-value)
                    insert_node(n.clist[p])
            else:
                p=bisect_right(n.vlist,key_value)
                n.vlist.insert(p,key_value)
                if n.isfull():
                    split_leaf(n)
                else:
                    return
        insert_node(node)
    def search(self,mi=None,ma=None):

