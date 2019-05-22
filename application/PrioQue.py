#!/usr/bin/python
# coding:utf-8
''' PrioQue 优先队列  '''

class PrioQue:
    def __init__(self, elist=[]):                  #引入空表参数
        self._elems = list(elist)                  #用list转换的作用是对实参表做一个拷贝，反正资源共享，且避免以可变对象作为默认值的python编程陷阱
        self._elems.sort(reverse=True)
    def enqueue(self, e):
        i = len(self._elems)-1
        while i >= 0:
            if self._elems[i] <= e:
                i -= 1
            else:
                break
        self._elems.insert(i+1,e)
    def is_empty(self):
        return not self._elems
    def peek(self):
        if self.is_empty():
            raise PrioQueueError("in top")
        return self._elems[-1]
    def dequeue(self):
        if self.is_empty():
            raise PrioQueueError("in pop")
        return self._elems.pop()

'''
    改善前一种方法的o(n)复杂度，利用堆heaps，关键操作是解决堆的插入和删除-筛选，其中插入进行向上筛选，删除进行向下筛选
'''
class PrioQueue:
    def __init__(self, elist=[]):
        self._elems = list(elist)
        if elist:
            self.buildheap()
    def is_empty(self):
        return not self._elems
    def peek(self):
        if self.is_empty():
            raise PrioQueueError("in peek")
        return self._elems[0]

    def enqueue(self, e):
        self._elems.append(None)
        self.siftup(e, len(self._elems)-1)
    #向上筛选
    def siftup(self, e, last):
        elems, i, j = self._elems, last, (last-1)/2         #父结点序号(i-1)/2
        while i > 0 and e < elems[j]:                       #与父结点做比较
            elems[i] = elems[j]                             #向上继续筛选
            i , j = j, (j-1)//2
        elems[i] = e                                        #插入位置

    def dequeue(self):
        if self.is_empty()
            raise PrioQueueError("in dequeue")
        elems = self._elems
        e0 = elems[0]
        e = elems.pop()
        if len(elems) > 0:
            self.siftdown(e,0,len(elems))
        return e0
    #弹出堆顶元素后，取最后一个元素进行向下筛选
    def siftdown(self,e,begin,end):
        elems, i, j = self._elems, begin, begin*2+1         #begin*2+1是左子结点序号
        while j < end:
            if j + 1 < end and elems[j+1] < elems[j]:       #elems[j]不大于其兄弟结点的数据
                j += 1
            if e < elems[j]:                                #e在三者中最小，找到位置
                break
            elems[i] = elems[j]                             #elems[j]在三者中最小，上移
            i, j = j, j*2+1
        elems[i] = e

    '''
       把初始的表看作完全二叉树，从下标end//2开始，后面的表元素都是二叉树的叶结点，则他们中每一个已是一个堆，
       开始向前做，从完全二叉树最下最右分支结点开始，不断向左向上一层建堆，构建整个表
    '''
    def buildheap(self):
        end = len(self._elems)
        for i in range(end//2, -1, -1):
            self.siftdown(self._elems[i], i, end)
   '''
       堆排序-将堆中元素逐个弹出，堆元素越来越少，表就会出现空位，这样正好可以用表后部出现的空位存放弹出的元素
   '''
    def head_sort(elems):
        def siftdown(elems, e, begin, end):
            i, j = begin, begin*2+1
            while j < end:
                if j+1 < end and elems[j+1] < elems[j]:
                    j += 1
                if e < elems[j]:
                    break
                elems[i] = elems[j]
                i, j = j, j*2+1
            elems[i] = e
        end = len(elems)
        for i in range(end//2, -1, -1):                       #循环建堆
            siftdown(elems,elems[i],i,end)
        for i in range((end-1), 0, -1):                       #循环逐个取出最小元素
            e = elems[i]
            elems[i] = elems[0]                               #将取出的元素积累的表后，放一个退一步
            siftdown(elems, e, 0, i)



    
