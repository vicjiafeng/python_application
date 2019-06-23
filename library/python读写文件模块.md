# python读写文件模块
___
### 读取csv文件
`csv 文件格式的本质是一种以文本存储的表格数据（使用 Excel 工具即可读写 csv 文件）。csv 文件的每行代表一行数据，每行数据中每个单元格内的数据以逗号隔开。`

* 创建 csv 模块的读取器
* 循环调用 csv 读取器的 next() 方法逐行读取 csv 文件内容即可。next() 方法返回一个 list 列表代表一行数据，list 列表的每个元素代表一个单元格数据

```python
import csv

filename = 'xxx.csv'

with open(filename) as f:
    #创建cvs文件读取器
    reader = csv.reader(f)
    #读取第一行，这是表头标题数据
    header_row = next(reader)
    print(header_row)
    #读取第二行，这行是真正的数据
    first_row = next(reader)
    print(first_row)
```

### 读取JSON文件
`SON 格式的数据通常会被转换为 Python 的 list 列表或 dict 字典`

* 使用 Python 的`json`模块读取 JSON 数据非常简单，只要使用 `load()`函数加载 JSON 数据即可

```python
import json

filename='xxx.json'

with open(filename) as f:
    read_list = json.load(f)
#遍历列表的每个元素，每个元素是一个GDP数据项
for read_dict in read_list:
    ...    
```
### 读取网络数据
`Python的网络支持库 urllib下的request模块可以非常方便地向远程发送 HTTP 请求,获取服务器响应,所以可以使用 urllib.request 向网站发起请求获取相应，然后通过python的re模块来解析服务器响应，提取数据`

* 实例
```python
import re
from datetime import datetime
from datetime import timedelta
from matplotlib import pyplot as plt
from urllib.request import *

#定义函数读取数据
def get_html(city,year,month):
    url = 'http://lishi.tianqi.com/' + city + '/' + str(year) + str(month) + '.html'
    #创建请求
    request = Request(url)
    #添加请求头, 本机浏览器user-agent可以在浏览器输入about:version获取
    request.add_header('User-agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.90 Safari/537.36')
    response = urlopen(request)
    #获取服务器响应
    return response.read().decode('utf-8')
    
#读取数据，利用正则匹配或xpath提取网页信息
...

#利用matplotlib或pygal将读取的数据转换到图表上
...

```

