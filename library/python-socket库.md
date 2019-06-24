# socket库
___
### 创建
`socket.socket(family=AF_INET, type=SOCK_STREAM, proto=0, fileno=None)`

* family 参数用于指定网络类型。该参数支持 socket.AF_UNIX（UNIX 网络）、socket.AF_INET（基于 IPv4 协议的网络）和 socket.AF_INET6（基于 IPv6 协议的网络）这三个常量

* type 参数用于指定网络 Sock 类型。该参数可支持 SOCK_STREAM（默认值，创建基于 TCP 协议的 socket）、SOCK_DGRAM（创建基于 UDP 协议的 socket）和 SOCK_RAW（创建原始 socket）。一般常用的是 SOCK_STREAM 和 SOCK_DGRAM

* proto 参数用于指定协议号，如果没有特殊要求，该参数默认为 0 ，并可以忽略

### 流程

#### TCP通信的服务器端编程的基本步骤

* 服务器端先创建一个 socket 对象
* 服务器端 socket 将自己绑定到指定 IP 地址和端口
* 服务器端 socket 调用 listen() 方法监听网络
* 程序采用循环不断调用 socket 的 accept() 方法接收来自客户端的连接
```python
s=socket.socket()                     #创建socket对象
s.bind(('192.168.1.10', 30000))       #将socket绑定到本机IP地址和端口, 尽量使用1024以上的端口，避免与其他通用端口发生冲突
s.listen()                            #监听客户端连接
while True:
    c, addr = s.accept()              #每当接收到客户端socket的请求时，该方法就返回对应的socket和远程地址
    ...
```
#### TCP通信的客户端编程步骤

* 客户端先创建一个 socket 对象
* 客户端 socket 调用 connect() 方法连接远程服务器
```python
s = socket.socket()                    #创建socket对象
s.connect(('192.168.1.10', 30000))     #连接远程服务器，服务器端 socket 的 accept() 方法向下执行，于是服务器端和客户端就产生一对互相连接的 socket
#进行通信
...           
```
#### 收发数据
* 发生数据:
`使用socket.send() 方法。注意，sendto() 方法用于 UDP 协议的通信`
* 接收数据:
`使用socket.recv()/socket.recv_xxx方法`
