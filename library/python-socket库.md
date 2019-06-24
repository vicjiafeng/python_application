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

#### [selectors模块](http://c.biancheng.net/view/2660.html)
`selectors模块允许socket以非阻塞方式通信，selectors 相当于一个事件注册中心，程序只要将 socket 的所有事件注册给 selectors 管理，当 selectors 检测到 socket 中的特定事件之后，程序就调用相应的监听方法进行处理`

* 分为两种事件

`1.selectors.EVENT_READ: 当 socket 有数据可读时触发该事件。当有客户端连接进来时也会触发该事件`

`2.selectors.EVENT_WRITE：当 socket 将要写数据时触发该事件`

* 程序避免了采用死循环不断地调用 socket 的 accept() 方法来接受客户端连接，也避免了采用死循环不断地调用 socket 的 recv() 方法来接收数据

### UDP通信
`通过type参数指定该socket的类型,当参数指定为SOCK_DGRAM，则意味着创建基于 UDP 协议的 socket`
* 在创建了基于UDP 协议的 socket 之后，程序可以通过如下两个方法来发送和接收数据

`1.socket.sendto(bytes, address)：将 bytes 数据发送到 address 地址`

`2.socket.recvfrom(bufsize[, flags])：接收数据。该方法可以同时返回 socket 中的数据和数据来源地址`

* 使用 UDP 协议的 socket 在发送数据时必须使用 sendto() 方法，这是因为程序必须指定发送数据的目标地址（通过 address 参数指定）；使用 UDP 协议的 socket 在接收数据时，既可使用普通的 recv() 方法，也可使用 recvfrom() 方法。如果程序需要得到数据报的来源，则应该使用 recvfrom()方法

* 服务器端 socket 的 IP 地址和端口应该是固定的，因此客户端程序可以直接向服务器端 socket 发送数据，但服务器端无法预先知道各客户端 socket 的 IP 地址和端口，因此必须调用 recvfrom() 方法来获取客户端 socket 的 IP 地址和端口

#### 简易c/s通信
```python
#服务器端
import socket

DATA_LEN = 2048
#定义一个发送的数组
cars=("audi","toyato","bmw")
#通过type属性指定创建基于UDP协议的socket
s=socket.socket(type=socket.SOCK_DGRAM)
s.bind(('192.168.1.10', 3000))
#循环接收数据
for i in range(1000):
    data, addr = s.recvfrom(DATA_LEN)
    print(data.decode('utf-8'))
    send_data = cars[i % 3].encode('utf-8')            #从字符串数组中取出一个元素作为发送数据
    s.sendto(send_data, addr)                          #将数据报发送给addr地址
s.close()

#客户端
import socket

DATA_LEN = 2048
DEST_IP = "192.168.1.10"
#通过type属性指定创建基于UDP协议的socket
s = socket.socket(type=socket.SOCK_DGRAM)
#键盘输入信息
while True:
    line = input('')
    if line is None or line == 'exit':
        break
    data = line.encode('utf-8')
    s.sendto(data, (DEST_IP, 3000))          #发送数据包
    data = s.recv(DATA_LEN)                  #读取socket中的数据
    print(data.decode('utf-8'))
s.close()
```
#### UDP多点广播
`在服务器端使用 list 列表来保存多个的客户端信息，可以实现多处送达数据报，每当接收一个客户端的数据报时，检查list中是否存在来源地址，不在则添加到list中，但当此客户端不再通信时，这里存入list的来源地址就没用了反而占据内存，所以需要一个定时器定期检查list中的地址；然而更好的办法是利用UDP协议的多点广播，即将数据报发送到一个组目标地址，当数据报发出后，整个组的所有主机都能接收到该数据报，实现了将单一信息发送给多个接收者的广播，其思想是设置一组特殊的网络地址作为多点广播地址，每一个多点广播地址都被看作一个组，当客户端需要发送和接收广播信息时，加入该组即可`

* IP 协议为多点广播提供了特殊的 IP 地址，这些IP地址的范围是`224.0.0.0~239.255.255.255`

* 广播多人聊天室
```python
import socket,time,threading,os
#定义本机IP地址
SENDERIP='192.168.1.10'
#定义本地端口
SENDERPORT = 3000
#定义本程序的多点广播IP地址
MYGROUP = '230.0.0.1'
#通过type属性指定创建基于UDP协议的socket
s = socket.socket(type=socket.SOCK_DGRAM)
#将socket绑定到ip
s.bind(('x.x.x.x', SENDERPORT))
#设置广播消息的TTL
s.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, 64)
#设置允许多点广播使用相同的端口
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
#将socket进入广播组
status = s.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, socket.inet_aton(MYGROUP) + socket.inet_aton(SENDERIP))
#定义从socket读取数据的方法
def read_socket(sock):
    while True:
        data = sock.recv(2048)
        print(data.decode('utf-8'))
threading.Thread(target=read_socket, args=(s, )).start()            #启动多线程
#循环读取键盘输入，并输出到socket中
while True:
    line = input('')
    if line is None or line == 'exit':
        break
        os.exit()
    s.sendto(line.encode('utf-8'), (MYGROUP, SENDERPORT))
```
