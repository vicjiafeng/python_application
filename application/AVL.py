#!/usr/bin/python
# coding:utf-8
''' AVL '''
class DicAVL(DictBinTree):    #除去插入，删除，其他方法都可以继承
    '''
        AVL复杂度-logn
        四种AVL插入操作：
        1.LL型（a的左子树较高，新结点插入左子树的左子树）
        2.LR型（a的左子树较高，新结点插入左子树的右子树)
        3.RR型（a的右子树较高，新结点插入右子树的右子树）
        4.RL型（a的右子树较高，新结点插入右子树的左子树）
    '''
    @staticmethod
    def LL(a,b):
        a.left = b.right
        b.right = a
        a.bf = b.bf = 0     #bf代表平衡因子（-1，0，1）
        return b
    
    @staticmethod
    def RR(a,b):
        a.right = b.left
        b.left = a
        a.bf = b.bf = 0
        return b
    
    @staticmethod
    def LR(a,b):
        c = b.right
        a.left, b.right = c.right, c.left
        c.left, c.right = b, a
        if c.bf == 0:
            a.bf = b.bf = 0
        elif c.bf == 1:
            a.bf = -1
            b.bf = 0
        else:
            a.bf = 0
            b.bf = 1
        c.bf = 0
        return c
    
    @staticmethod
    def RL(a,b):
        c = b.left
        a.right, b.left = c.left, c.right
        c.left, c.right = a, b
        if c.bf == 0:
            a.bf = 0
            b.bf = 0
        elif c.bf == 1:
            a.bf = 0
            b.bf = -1
        else:
            a.bf = 1
            b.bf = 0
        c.bf = 0
        return c
    
    def insert(self,key,value):
        a=p=self._root          #变量a记录距插入位置最近的平衡因子非0的结点，p为扫描变量，pa记录a的父节点
        if a is None:
            self._root = AVLNode(Assoc(key,value))
            return
        pa = p = None
        while p is not None:
            if key == p.data.key:
                p.data.value = value
                return
            if p.bf != 0:
                pa, a = q, p          #最小平衡子树
            q=p
            if key < p.data.key:
                p=p.left
            else:
                p=p.right
        #q是插入点的父节点，pa，a记录最小非平衡子树
        node=AVLNode(Assoc(key,value))
        if key < q.data.key:
            q.left = node                #左子节点
        else:
            q.right = node               #右子节点
        #插入新结点，a是最小不平衡子树
        if key < a.data.key:             #新结点在左子树
            p = b = a.left
            d = 1                        #d记录结点在a的哪棵树
        else:
            p = b = a.right              #新结点在右子树
            d = -1
        #修改b到新结点路径上各结点的bf值，b为a的子节点
        while p != node:
            if key < p.data.key:         #p的左子树增高
                p.bf = 1
                p = p.left
            else:
                p.bf = -1                #p的右子树增高
                p = p.right
        if a.bf == 0:                 #a之前bf为0，不会失衡
            a.bf = d
            return
        if a.bf == -d:                # 新结点在较低子树里
            a.bf = 0
            return
        #新结点在较高子树里，会失衡
        if d==1:                         #新结点在a的左子树
            if b.bf==1:
                b=DictAVL.LL(a,b)
            else:
                b=DictAVL.LR(a,b)
        else:                            #新结点在a的右子树
            if b.bf==-1:
                b=DictAVL.RR(a,b)
            else:
                b=DictAVL.RL(a,b)
            
        if pa is None:                   #原a为树根，修改_root
            self._root = b
        else:                            #a为非树根
            if pa.left == a:
                pa.left = b
            else:
                pa.right = b


                   
