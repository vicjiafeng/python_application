# pydoc模块
___
### 借助于 Python 自带的 pydoc 模块，可以非常方便地查看、生成帮助文档

1. 利用控制台查看文档

`python -m pydoc 模块名        # -m 是 python 命令的一个选项，表示运行指定模块`

2. 生成html文档

`python -m pydoc -w 模块名     #-w 选项，该选项代表 write，表明输出 HTML 文档`

3. 生成html目录

`python3 -m pydoc -w 目录名`

4. 启动本地服务器查看文档

`python3 -m pydoc -p 端口号       #在指定端口启动http服务器查看文档`

`python3 -m pydoc -b             #在任意未占用的端口启动http服务器查看文档`

5. 查找模块

`python -m pydoc -k 被搜索模块的部分内容        #-k 选项，该选项用于查找模块`

