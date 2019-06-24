# socket库
___
### 创建
`socket.socket(family=AF_INET, type=SOCK_STREAM, proto=0, fileno=None)`

* family 参数用于指定网络类型。该参数支持 socket.AF_UNIX（UNIX 网络）、socket.AF_INET（基于 IPv4 协议的网络）和 socket.AF_INET6（基于 IPv6 协议的网络）这三个常量

* type 参数用于指定网络 Sock 类型。该参数可支持 SOCK_STREAM（默认值，创建基于 TCP 协议的 socket）、SOCK_DGRAM（创建基于 UDP 协议的 socket）和 SOCK_RAW（创建原始 socket）。一般常用的是 SOCK_STREAM 和 SOCK_DGRAM

* proto 参数用于指定协议号，如果没有特殊要求，该参数默认为 0 ，并可以忽略

### 流程

#### TCP通信的服务器端编程步骤

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

### 多线程socket通信
`由于socket的recv()方法成功读取数据后，线程会被阻塞，程序无法继续执行，所以服务器应该为每个socket都单独启动一个线程，每个线程与一个客户端进行通信，并将读取的数据向每个socket发送一次(list保存所有socket)，同样每个客户端也应该单独启动一个线程，负责读取服务器数据`
* 一个简易c/s聊天室实现
```python
#服务器端
import threading
import socket

socket_list=[]                      #保存所有socket列表
ss = socket.socket()
ss.bind(('192.168.1.10', 3000))
ss.listen()

def read_from_clien(s):
    try:
        return s.recv(2048).decode('utf-8')
    #如果捕获到异常，则表明该socket对应的客户端已经关闭
    except:
        socket_list.remove(s)
#server_target()函数作为线程执行的target，负责处理每个 socket 的数据通信
def server_target(s):
    try:
        while True:                       #采用循环不断地从socket中读取客户端发送过来的数据
            content = read_from_client(s)
            print(content)
            if content is None:
                break
            for client_s in socket_list:
                client_s.send(content.encode('utf-8'))         #程序遍历 socket_list 列表，并将该数据向 socket_list 列表中的每个 socket 发送一次
    except e:
        print(e.strerror)
while True:
    s, addr = ss.accept()
    socket_list.append(s)
    threading.Thread(target=server_target, args=(s,)).start()        #每当客户端连接后启动一个线程为该客户端服务

#客户端
import threading
import socket

s = socket.socket()
s.connect(('192.168.1.10', 3000))
def read_from_server(s):
    while True:                              #使用死循环读取 socket 中的数据
        print(s.recv(2048).decode('utf-8'))
#客户端启动线程不断地读取来自服务器的数据
threading.Thread(target=read_from_server, args(s, )).start()
#读取用户输入信息
while True:
    line = input('')
    if line is None or line == 'exit':
        break
    s.send(line.encode('utf-8'))             #将用户的键盘输入内容写入socket
```
#### shutdown()方法
`socket的shutdown(how)关闭方法，该方法可以只关闭socket的输入或输出部分(close()方法是完全关闭socket)，用以表示输出数据已经发送完成,因此不适合保持持久通信状态的交互式应用，只适用于一站式的通信协议，例如 HTTP 协议`

* how参数：

`1.SHUT_RD:关闭 socket 的输入部分，程序还可通过该 socket 输出数据`

`2.SHUT_WR： 关闭该 socket 的输出部分，程序还可通过该 socket 读取数据`

`3.SHUT_RDWR：全关闭。该 socket 既不能读取数据，也不能写入数据`
