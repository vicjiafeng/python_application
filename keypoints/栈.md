# 栈
___
### 1. 定义

 * 栈是后进先出的关系结构，对于顺序表，后端插入和删除是O(1),对于链接表，前端插入和删除是O(1)
         
```python     
   
         class SStack():                    #基于顺序表技术实现栈类,链接表与之相似      
       
             def __init__(self):                         
             
                 self._elems = []
                 
             def is_empty(self):
             
                 return self._elems == []
             def top(self):
                 if self._elems == []:
                     raise StackUnderflow("in SStack.top()")
                 return self._elems[-1]
             def push(self,elem):
                 self._elems.append(elem)
             def pop(self):
                 if self._elems == []:
                     raise StackUnderflow("in SStack.pop()") 
                 return self._elems.pop()
```
                 
### 2. 应用

#### 2.1 表达式的表示

  * 中缀表达式
  
            （3-5)*(6+17*4)/3
 
  * 前缀表达式
  
             / * - 3 5 + 6 * 17 4 3
  
  * 后缀表达式
  
             3 5 - 6 17 4 * + * 3 /

#### 2.2 核心框架
  
  * 后缀表达式求值
  
  ```python
             def suf_exp_evalutor(exp):        #exp是一个项的表
                 operators = "+-*/"
                 st = ESStack()                #检查栈的元素个数（class ESStack(SStack):def depth（self）： return len(self._elems))
                 
                 for x in exp:
                     if x not in operators:
                         st.push(float(x))
                         contiue
                     if st.depth() < 2:
                         raise SyntaxError("short of operands.")
                     a = st.pop()              #取得第二个运算对象
                     b = st.pop()              #取得第一个运算对象
                     
                     if x == "+":
                         c = b + a
                     elif x == "-":
                         c = b - a
                     elif x == "*":
                         c = b * a
                     elif x == "/":
                         c = b / a
                     else:
                         break
                         
                     st.push(c)
                 if st.depth() == 1:
                     return st.pop()
                 raise SyntacError("Extra operand.")
```

  * 中缀表达式转换后缀表达式   
  
  ```python
  
                 def trans_infix_suffix(line):
                     opertor_rank = {"(":1, "+":3, "-":3, "*":5, "/":5}       #各运算符优先级
                     infix_operators = "+-*/()"                               #涉及到的运算符
                     st = SStack()
                     exp = []
                     
                     for x in tokens(line):                       #token是一个生成器
                         if x not in infix_operators:             #运算对象直接送出
                             exp.append(x)
                         elif st.is_empty(): or x == '(':         #左括号进栈
                             st.push(x)
                         elif x == ')':                           #处理右括号
                             while not st.is_empty() and st.top() != '(':
                                 exp.append(st.pop())
                             if st.is_empty():                    #没有找到左括号
                                 raise SyntaxError("Missing '('.")
                             st.pop()                             #弹出左括号，右括号也不进栈
                         else:                                    #处理运算符
                             while (not st.is_empty() and operator_rank[st.pop()] >= operator_rank[x]):
                                 exp.append(st.pop())
                             st.push                               #运算符进栈
                             
                     while not st.is_empty():                      #弹出栈里剩余运算符
                         if st.top() == '(':                       #出现左括号，则不匹配
                             raise SyntaxError("Extra '('.")
                         exp.append(st.pop())
                     return exp                                    #返回记录表
                     
                 def tokens(line):                                 #生成器函数，逐一生成line中的一个个项(运算对象运算符）
                     i, llen = 0, len(line)
                     while i < llen:
                         while line[i].isspace():
                             i += 1
                         if i >= llen:
                             break 
                         if line[i] in infix_operators:            #运算符情况
                             yield line[i]
                             i += 1
                             continue
                         
                         j = i + 1                                 #处理运算对象
                         while (j<llen and not line[j].isspace() and line[j] not in infix_operators):
                             if ((line[j] == 'e' or line[j] == 'E') and j+1 < llen and line[j+1] == '-'):       #处理负指数
                                 j += 1
                             j += 1
                         yield line [i:j]                           #生成运算对象子串
                         i = j
```

### 3. 递归
      
  * 阶乘的递归计算
  
  ```python 
                def fact(n):
                    if n==0:
                        return 1
                    else:
                        return n * fact(n-1)
  ```
                        
  * 阶乘的非递归计算
  
  ```python               
                def non_fact(n):
                    res = 1
                    st = SStack()
                    while n > 0:
                        st.push(n)
                        n -= 1
                    while not st.is_empty():
                        res *= st.pop()
                    return res
 ```
 * 总结
        
             任何一个递归定义的函数都可以通过引用一个栈保存中间结果的方式，翻译成一个非递归的过程。但针对不同问题，递归与非递归复杂度不同（背包问题）
                        
                         
                
                 
                 
      
