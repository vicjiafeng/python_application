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

>`1.被拼接的 URL 只是一个相对路径 path（不以斜线开头），那么该 URL 将会被拼接到 base 之后，如果 base 本身包含 path 部分，则用被拼接的 URL替换 base 所包含的 path 部分`

>`2.被拼接的 URL 是一个根路径 path（以单斜线开头），那么该 URL 将会被拼接到 base 的域名之后`

>`3.被拼接的 URL 是一个绝对路径 path（以双斜线开头），那么该 URL将会被拼接到 base 的 scheme 之后`

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

with urlopen(req) as f:
    f.status()
    f.read()
    ...
```
### http.cookiejar模块

* 有效管理session，使得之后的访问可以通过`session ID`识别客户端

* 使用`OpenerDirector`对象来发送请求

* 实例

```python
cookie_jar = http.cookiejar.MozillaCookieJar(a.txt)      #指定文件创建CookieJar对象，对象将可以把cookie保存在文件中
cookie_processor = HTTPCookieProcessor(cookie_jar)       #创建HTTPCookieProcessor对象,该对象负责调用 CookieJar 来管理 cookie
opener = build_opener(cookie_processor)                  #创建 OpenerDirector 对象

#定义浏览器user-agent,定义登陆请求参数params，向页面发送request请求
user-agent=...
headers=...
response = opener.open(request)    #使用OpenerDirector发送POST请求,该对象将会通过HTTPCookieProcessor调用CookieJar来管理cookie
response.read()

cookie_jar.save(ignore_discard=True, ignore_expires=True)    #将cookie信息写入磁盘文件
#程序就会把 cookie 信息写入 a.txt 文件中。这意味着该程序将会把服务器响应的 session id 等 cookie 持久化保存在 a.txt 文件中，后面程序可以读取该 cookie文件信息，这样程序就可以模拟前面登录过的客户端，从而直接访问被保护页面了

#发送GET请求的Request
request = Request(url,headers)
response = opener.open(request)
response.read()

#------当再次访问页面时，使用load（）加载a.txt中的Cookie信息,读取保存过的用户信息---------
cookie_jar = http.cookiejar.MozillaCookieJar('a.txt')
cookie_jar.load('a.txt',ignore_discard=True,ignore_expires=True)

for item in cookie_jar:                      #遍历a.txt中保存的cookie信息
    print('Name ='+ item.name)
    print('Value ='+ item.value)
cookie_processor = HTTPCookieProcessor(cookie_jar) 
opener = build_opener(cookie_processor) 

#定义浏览器user-agent,定义登陆请求参数params
user-agent=...
headers=...

#无需创建页面post请求，因为之前的登陆session ID信息已经保存到a.txt中，并通过load完成读取，服务器通过session ID认定两次登陆是同一客户端

#发送GET请求的Request
request = Request(url,headers)
response = opener.open(request)
response.read()
```

