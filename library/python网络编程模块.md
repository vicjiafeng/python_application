# python网络编程模块
___
### urllib模块

* urllib.request：打开和读取 URL 的各种函数
* urllib.error: 包含urllib.request子模块所引发的各自异常
* urllib.parse: 解析url
* urllib.robotparse: 解析robots.txt文件

#### urllib.parse子模块

* urllib.parse.urlparse：用于解析 URL 字符串，返回result对象，获取解析出的数据
* urllib.parse.urlunparse：反向操作，将解析结果反向拼接成 URL 地址
* urllib.parse.parse_qs：用于解析查询字符串，并以dict形式返回
* urllib.parse.parse_qsl：用于解析查询字符串，并以list形式返回
* urllib.parse.urlencode：将字典形式或列表形式的请求参数恢复成请求字符串，相当于parse_qs/parse_qsl逆函数
* urllib.parse.urljoin：用于将一个 base_URL 和另一个资源 URL 连接成代表绝对地址的 URL

#### urllib.request子模块

* urllib.request.urlopen(url, data=None)：用于打开 url 指定的资源，并从中读取数据
> 两种打开方式 
```python
#1
result = urlopen('....')
data = result.read()
print(data.decode('utf-8'))

#2
with urlopen('...') as f:
    data = f.read()
    print(data.decode('utf-8'))    
```

* GET请求

`程序在发送 GET 请求参数时,无须使用 data 属性，直接把请求参数附加在 URL 之后即可`

* POST请求

`如果要向指定地址发送 POST 请求，可以通过data属性指定请求参数`
```python
with urlopen('...', data=params) as f:
    ...
```
* PUT/DELETE/PATCH请求

`利用request构造请求参数`

```python
req = Request(url='...', data=params, method = 'PUT')           #指定put方法
#req.add_header(...)       可以使用request对象添加请求头

with urloopen(req) as f:
    f.status()
    f.read()
    ...
```

