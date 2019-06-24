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
      
#### 4.实例
```python
import poplib, os.path, mimetypes
from email.parser import BytesParser, Parser
from email.policy import default

email='542904969@qq.com'
password='123456'
pop3_server = 'pop.qq.com'
#连接pop3服务器
conn = poplib.POP3_SSL(pop3_server, 995)
conn.set_debuglevel(1)
#print(conn.getwelcome().decode('utf-8'))           #打印欢迎文字

conn.user(email)
conn.pass_(password)
#获取邮件统计信息，相当于发送POP 3的stat命令
message_num, total_size = conn.stat()
print('邮件数: %s. 总大小: %s' % (message_num, total_size))
#获取服务器上的邮件列表，相当于发送POP 3的list命令
resp, mails, octets = conn.list()                   #resp保存服务器的响应码,mails列表保存每封邮件的编号、大小
print(resp, mails)
#获取指定邮件的内容（此处传入总长度，也就是获取最后一封邮件）
resp, data, octets  = conn.retr(len(mails))         #data保存该邮件的内容
#将data的所有数据（原本是一个字节列表）拼接在一起
msg_data = b'\r\n'.join(data)
#将字符串内容解析成邮件，此处一定要指定policy=default
msg = BytesParser(policy=default).parsebytes(msg_data)

print(type(msg))
print('发件人:'+ msg['from'])
print('收件人:'+ msg['to'])
print('主题:'+ msg['subject'])
print('第一个收件人名字:' + msg['to'].addresses[0].username)
print('第一个发件人名字:' + msg['from'].addresses[0].username)

for part in msg.walk():          #walk() 方法，该方法返回一个可迭代对象，程序使用 for 循环遍历 walk() 方法的返回值，对邮件内容进行逐项处理
    counter = 1
    #如果maintype是multipart，说明是容器（用于包含正文、附件等）
    if part.get_content_maintype() = 'multipart':
        continue
    elif part.get_content_maintype() == 'text':              #如果maintype是text，说明是邮件正文部分,程序直接将其输出到控制台中
        print(part.get_content())
    else:
        filename = part.get_filename()
        if not filename:
            ext = mimetypes.guess_extension(part.get_content_type())             #根据附件的contnet_type来推测它的后缀名
            if not ext:                     #如果推测不出后缀名
                ext = '.bin'                #使用.bin作为后缀名
            filename = 'part-%03d%s' % (counter, ext)             #程序为附件来生成文件名
        counter += 1
        #将附件写入的本地文件
        with open(os.path.join('.', filename), 'wb') as f:
            fp.write(part.get_payload(deconde=True))
conn.quit()                  #退出服务器        
```
