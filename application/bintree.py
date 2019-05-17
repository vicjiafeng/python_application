#!/usr/bin/python
# coding:utf-8
''' BinTree '''
class DictBinTree:                 #二叉排序树
    def __init__(self):
        self._root = None
    def is_empty(self):
        return self._root is None
    def search(self,key):
        bt = self._root
        while bt is not None:
            entry = bt.data
            if key < entry.key:
                bt = bt.left
            elif key > entry.key:
                bt = bt.right
            else:
                return entry.value
        return None
    def insert(self,key,value):    #插入数据
        bt = self._root
        if bt is None:
            self._root = BinTNode(Assoc(key,value))   #关联
            return
        while True:
            entry = bt.data
            if key < entry.key:
                if bt.left is None:
                    bt.left = BinTNode(Assoc(key,value))
                    return
                bt = bt.left
            elif key > entry.key:
                if bt.right is None:
                    bt.right = BinTNode(Assoc(key,value))
                    return
                bt=bt.right
            else:
                bt.data.value = value
                return
    def value(self):         #迭代器生成值的序列
        t,s = self._root, SStack()
        while t is not None or not is_empty():
            while t is not None:            #中序遍历
                s.push(t)
                t = t.left
            t = s.pop()
            yield t.data.key, t.data.value
        t = t.right
#删除项，若待删除的点q是叶节点，直接删除，设置父节点p到删除节点的引用为None即可；若待删除q不是叶节点，
#且q没有左子节点，则把q的右子树改为父节点p的左子树，若q有左子树，先找到左子树最右节点，设为r，
#把q的左子节点改为父节点p的左子节点，把q的右子树作为r的右子树
    def delete(self,key):
        p,q = None,self._root
        while q is not None and q.data.key != key:
            p=q
            if key < q.data.key:
                q = q.left
            else:
                q = q.right
            if q is None:
                return
        
            if q.left is None:             #q没有左子节点
                if p is None:              #q是根节点
                    self._root = q.right
                elif q is p.left:
                    p.left = q.left
                else:
                    p.right = q.right
                return
            
            r = q.left
            while r.right is not None:
                r = r.right

            r.right = q.right
            if p is None:                  #q是根节点
                self._root = q.left
            elif p.left is q:
                p.left = q.left
            else:
                p.right = q.left

    def buildBinTree(entries):
        dic = DictBinTree()
        for k, v in entries:
            dic.insert(k,v)
        return dic


                   
