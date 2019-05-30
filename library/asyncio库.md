# python-asyncio库-异步IO支持
___
### 原理
`asyncio的编程模型就是一个消息循环。从asyncio模块中直接获取一个EventLoop的引用，然后把需要执行的协程扔到EventLoop中执行，就实现了异步IO`
#### 实现
```python
import asyncio

@asyncio.coroutinne
def hello():
   print("hello world!")
   r=yield from asyncio.sleep(1)
   print("hello again!")

loop = asyncio.get_event_loop()                             #获取eventloop
tasks = [hello(),hello()]
loop.run_until_complete(asyncio.wait(tasks))                #执行协程coroutine
loop.close()

```
#### 解析
 `yield from`语法可以让我们方便地调用另一个generator,遇到时直接中断并执行下一个消息循环。当`asyncio.sleep(1)`(这里等待1s的时间操作里，主线程并未等待，而是执行eventloop中其他可执行的部分)返回时，线程就可以从`yield from`拿到返回值（此处是`None`），然后接着执行下一行语句, 且可以用`task`封装要执行的线程

### 
 

