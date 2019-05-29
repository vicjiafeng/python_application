# python实现发邮件功能
___

### 1. 工具

* 用python实现发邮件，需要用到的库有email和smtplib

         smtplib库主要是用于负责和邮件服务器进行通讯
         
         email库则主要用于规定编写邮件的头、主体、内容、附件等

### 2. 步骤

#### 2.1 获得发送权限
    
       登陆smtp服务器(手动开启)
 
#### 2.2 邮箱设置，开启授权
   
   * 可参考[qq邮箱](https://jingyan.baidu.com/article/fedf0737af2b4035ac8977ea.html)设置

#### 2.3 代码

```python 
  import urllib
  from smtplib import SMTP
  from email.header import Header
  from email.mime.text import MIMEText
  from email.mime.image import MIMEImage
  from email.mime.multipart import MIMEMultipart
  
  def main():
      message = MIMEMultipart()                                        #带附件的消息对象
      text_content = MIMEText(msg_content, 'plain', 'utf-8')
      
      message['From'] = Header('xx', 'utf-8')
      message['To'] = Header('xxx', 'utf-8')
      message['Subject'] = Header('email_content_blablabla', 'utf-8')  #创建文本内容
      message.attach(text_content)                                     #将文本内容添加到邮件消息对象中
         
      # 读取文件并将文件作为附件添加到邮件消息对象中
      with open('/Users/xxx/hello.txt', 'rb') as f:
          txt = MIMEText(f.read(), 'base64', 'utf-8')
          txt['Content-Type'] = 'text/plain'
          txt['Content-Disposition'] = 'attachment; filename=hello.txt'
          message.attach(txt)
          
         #with open('/Users/xxx/1.jpg', 'rb') as f:                      可读取本地图片
         #mime = MIMEBase('image', 'jpg', filename='name.png')           jpg/png可以切换，图片名称注意对应
     
      sender = 'xxx@163.com'
      passWord = 'xxx'
      smtper = SMTP('smtp.163.com')                                   #服务器地址
      receivers = ['542904969@qq.com', 'vicfeng@outlook.com',]        #邮件接收人，可添加任意多个
      smtper.login(sender, 'secret_pass')                             #注意此处不是使用密码而是邮件客户端授权码进行登录
      smtper.sendmail(sender, receivers, message.as_string())
      smtper.quit()
      print('邮件发送完成!')
  if __name__ == '__main__':
      main()
```

      
