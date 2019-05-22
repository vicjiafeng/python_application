# 队列
___
### 1. 定义
   
           简单的队列实现可以通过有尾端指针的单链表，其中尾端加入元素是O(1)时间操作，用作队列入队操作enqueue，首端的访问与删除也都是O(1)时间操作,分别看作队列的peek和dequeue
           
### 2. 循环顺序表

  * 基本框架
  
           class SQueue():
               def __init__(self,init_len=8):
                   self._len = init_len                         #_len存储区长度
                   self._elems = [0]*init_len                   #_elems属性引用队列的存储区，是list对象
                   self._head = 0                               #_head是队列首元素
                   self._num = 0                                #_num记录元素个数
                   
               def is_empty(self):
                   return self._elems == 0
               
               def peek(self):
                   if self._num == 0:
                       raise QueueUnderflow
                   return self._elems[self._head]
                   
               def dequeue(self):
                   if self.num == 0:
                       raise QueueUnderflow 
                   e = self._elems[self._head]                                   #队列首元素self._head
                   self._head = (self._head+1) % self._len         
                   self._num -= 1
                   return e
                   
               def enqueue(self,e):
                   if self._num == self._len:
                       self.__extend()
                   self._elems[(self._head + self._num)%self._len] = e           #入队新元素存入下一个空位
                   self._num += 1
                   
               def __extend(self):
                   old_len = self._len
                   self._len *= 2
                   new._elems = [0]*self._len
                   for i in range(old_len):
                       new_elems[i] = self._elems[(self._head + i) % old_len]
                   self._elems, self._head = new_elems, 0
                   
               
