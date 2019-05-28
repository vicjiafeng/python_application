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
      import smtplib
      from email import encoders
      from email.mime.text import MIMEText
      from email.mime.base import MIMEBase
      from email.mime.multipart import MIMEMultipart
      sender = 'xxx@163.com'
      passWord = 'xxx'
      mail_host = 'smtp.163.com'                                      #服务器地址
      receivers = ['542904969@qq.com', 'vicfeng@outlook.com',]        #邮件接收人，可添加任意多个
      
      msg = MIMEMultipart()                                           #设置email信息
      msg['Subject'] = input(u'请输入邮件主题：')
      msg['From'] = sender
      msg_content = input(u'请输入邮件主内容:')                          #邮件正文是MIMEText
      msg.attach(MIMEText(msg_content, 'plain', 'utf-8'))
      with open(u'/Users/xxx/1.jpg', 'rb') as f:                      #可读取本地图片
      mime = MIMEBase('image', 'jpg', filename='name.png')            #jpg/png可以切换
      
      #添加头文件
      mime.add_header('Content-Disposition', 'attachment', filename='Lyon.png')
      mime.add_header('Content-ID', '<0>')
      mime.add_header('X-Attachment-Id', '0')
      mime.set_payload(f.read())                                      #读取附件内容
      encoders.encode_base64(mime)                                    #用Base64编码
      msg.attach(mime)
      
      #登陆发送邮件
      try:
          s = smtplib.SMTP_SSL("smtp.163.com", 465)                   #163邮箱的端口号为465或994
          s.set_debuglevel(1)
          s.login(sender,passWord)
          for item in receivers:                                      #给列表中的人逐个发送邮件
              msg['To'] = to = item
              s.sendemail(sender,to,msg.as_string())
              print('success!')
          s.quit()
          print('job done')
      except smtplib.SMTPException as e:
          print ("Falied,%s",e)
```
      
