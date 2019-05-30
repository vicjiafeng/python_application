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


