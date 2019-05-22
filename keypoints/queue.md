# 队列
___
### 1. 定义
   
           简单的队列实现可以通过有尾端指针的单链表，其中尾端加入元素是O(1)时间操作，用作队列入队操作enqueue，首端的访问与删除也都是O(1)时间操作,分别看作队列的peek和dequeue
           
### 2. 循环顺序表

#### 2.1 基本框架
  
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
                   
#### 2.2 应用(迷宫，八皇后..)

              def mark(maze, pos):                                   #给迷宫maze的位置pos标记2，表示已经到过
                  maze[pos[0]][pos[1]] = 2
              def passable(maze, pos):                               #检查迷宫位置pos是否可行
                  return maze[pos[o]][pos[1]] == 0
              dirs = [(0,1), (1,0), (0,-1), (-1,0)]                  #四个相邻位置
                  

  * 递归
              def find_path(maze,pos,end):                           #pos表示搜索的当前位置
                  mark(maze,pos)        
                  if pos == end:                                     #已到达出口
                      print(pos, end=" ")
                      return True
                  for i in range(4):                                 #按四个方向顺查
                      nextp = pos[0]+dirs[i][0], pos[1]+dirs[i][1]
                      if passable(maze,nextp):
                          if find_path(maze,nextp,end):
                              print(pos, end=" ")
                              return True
                  return False
                  
  * 利用栈
  
              def maze_solver(maze, start, end):
                  if start == end:
                      print(start)
                      return
                  st = SStack()
                  mark(maze,start)
                  st.push((start,0))                                   #入口和方向0的序对入栈
                  while not st.is_empty():                             #回退
                      pos, nxt = st.pop()                              #取栈顶及探查方向
                      for in in range(nxt,4):                          #依次探查
                          nextp = (pos[0] + dirs[i][0], pos[1] + dirs[i][1])     #算出下一个位置
                          if nextp == end:
                              print_path(end, pos, st)
                              return
                          if passable(maze, nextp):                     #遇到未探查的新位置
                              st.push((pos,i+1))                        #原位置和下一个方向入栈
                              mark(maze, nextp)
                              st.push((nextp,0))                        #新位置入栈
                              break                                     #退出内层循环，下次迭代以新栈顶为当前位置继续
                  print("No Path Found")
                  
   * 利用队列
   
              '''队列搜索没有记录完整路径，可能需要dict帮助记录'''
              def maze_solver_queue(maze,start,end):
                  if start == end:
                      print("path found.")
                      return
                  qu = squeue()
                  mark(maze,start)
                  qu.enquue(start)                                              #入队
                  while not qu.is_empty():
                      pos = qu.dequeue()                                        #取下一个位置
                      for i in range(4):
                          nextp = (pos[0]+dirs[i][0], pos[1]+dirs[i][1])        #列举各个位置
                          if passable(maze,nextp):                              #找到新探查方向
                              if nextp == end:                              
                                  print("path found.")
                                  return
                              mark(maze, nextp)
                              qu.enqueue(nextp)                                 #新位置入队
                  print("no path found.")
  
                   
               
