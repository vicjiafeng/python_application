# scrapy框架
___
### 组件
* ENGINE：引擎，是scrapy框架的核心；内部组件
* SCHEDULER：调度器，负责对SPIDER提交的下载请求进行调度；内部组件
* DOWNLOADER：下载器，负责下载页面，即发送HTTP请求和接受HTTP响应；内部组件
* SPIDER：爬虫，负责从页面解析和提取数据，以及生成新的HTTP请求，用户组件
* MIDDLEWARE：中间件，负责对HTTP请求和接受HTTP响应进行处理；可选组件
* ITEM PIPELINE:数据管道，负责对爬取的数据进行处理，如去重、写入数据库等

### 流程框架图
  
   >![](https://github.com/vicjiafeng/python_application/blob/master/library/images/01.png)
 
### 解析框架图
step1: Spider将要爬取页面的URL构造Request对象，提交给Engine

step2: Request由Engine进入Scheduler

step3: SCHEDULER( url调度器)，生成request交给ENGIN

step4: 由Engine经由Middleware(存在某种算法设置)提交给Downloader

step5: Downloader根据Request中的URL地址发送一次HTTP请求到目标网站服务器，接受服务器返回的HTTP响应并构建一个Response对象,经由Middleware发给Engine

step6: Engine将接收到的Response数据返回给Spider，SPIDERS的parse()方法对获取到的response数据进行处理

step7: 其中Spider解析出的item对象，发给Engine提交给Item pipeline

step8: 其中解析出的requests或新的链接构造出Request对象，则经由Engine提交给Scheduler

---这个过程反复进行，直到爬完所有的数据


