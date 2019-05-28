# 利用python从网页下载图片
___

#### 利用多线程，即一个线程在get、post或等数据传输时，不必停止整个程序，而是切换到其他的线程完成接下来的任务，对比于单一线程下载图片，可以有效提升速率

  * python代码
  
  ```python
        import os
        import request
        import time
        from lxml import etree
        from threading import Thread
        
        keyWord = input(f"{'Please input the keywords that you want to download :'}")
        class Spider():
            def __init__(self):
                self.headers = {"User-Agent": "Mozilla/5.0(WindowsNT6.1;rv:2.0.1)Gecko/20100101Firefox/4.0.1",}   #header请求头可以查询
 
            
