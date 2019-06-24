# python实现发送邮件和收取邮件
___

### 发送邮件

#### 1. 工具

* 用python实现发邮件，需要用到的库有email和smtplib

         smtplib库主要是用于负责和邮件服务器进行通讯
         
         email库则主要用于规定编写邮件的头、主体、内容、附件等

#### 2. 步骤

##### 2.1 获得发送权限
    
       登陆smtp服务器(手动开启)
 
##### 2.2 邮箱设置，开启授权
   
   * 可参考[qq邮箱](https://jingyan.baidu.com/article/fedf0737af2b4035ac8977ea.html)设置

##### 2.3 实例

```python 
import smtplib,email.utils
from email.message import EmailMessage                  #EmailMessage是Python 3.x 对邮件处理
#定义SMTP服务器地址
smtp_server = 'smtp.qq.com'
#定义发件人地址
from_addr = '542904969@qq.com'
#定义登录邮箱的密码
password = '123456'
#定义收件人地址
to_addr = 'vicjiafeng@163.com'

#创建SMTP连接
conn = smtplib.SMTP_SSL(smtp_server,465)            #基于 SSL 的 SMTP 服务器的默认端口是 465
conn = set_debuglevel(1)                            #debuglevel设置为1，可以看到 SMTP 发送邮件的详细过程
conn.login(from_addr, password)                     #登陆邮箱
msg = EmailMessage()                                #创建邮件对象
first_id, second_id = email.utils.make_msgid(), email.utils.make_msgid()      #随机生成两个图片id
#设置邮件内容，指定邮件内容为HTML
msg.set_content('<h1>邮件内容</h1>'+'<p>这是一封邮件'+'<img src="cid:'+second[1:-1]+'"</p> + '来自<a href="https://....">这是网址</a>','html','utf-8')
msg['subject'] = '一封邮件'
msg['from'] = 'user1 <%s>' % from_addr
msg['to'] = 'user2 <%s>' % to_addr

with open('/path/1.jpg', 'rb') as f:
    msg.add_attachment(f.read(), maintype='image', subtype='jpeg', filename='test.png', cid = first_id)       #添加第一个附件
with open('/path/2.gif', 'rb') as f:
    msg.add_attachment(f.read(), maintype='image', subtype='gif', filename='test.gif', cid = second_id)       #添加第二个附件
...

conn.sendmail(from_addr, [to_addr], msg.as_string())          #发送邮件
conn.quit()                                                   #退出连接

```
### 收取邮件

#### 1.工具

* poplib 模块收取邮件，该模块提供了 poplib.POP3 和 poplib.POP3_SSL 两个类，分别用于连接普通的 POP 服务器和基于 SSL 的 POP 服务器

#### 2.POP3协议

`POP3 协议也属于请求，响应式交互协议，当客户端连接到服务器之后，客户端向 POP 服务器发送请求，而 POP 服务器则对客户端生成响应数据，客户端可通过响应数据下载得到邮件内容。当下载完成后，邮件客户端可以删除或修改任意邮件，而无须与电子邮件服务器进行进一步交互`

#### 3.步骤
* 使用 poplib.POP3 或 poplib.POP3_SSL 按 POP3 协议从服务器端下载邮件
* 使用 email.parser.Parser 或 email.parser.BytesParser 解析邮件内容，得到 EmailMessage 对象，从 EmailMessage 对象中读取邮件内容
      
