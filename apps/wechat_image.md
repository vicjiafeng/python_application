# 提取微信用户头像
————————
### 1. 下载好友的头像

* 自定义python文件名，如getheadimgs.py

```python
      #!/usr/bin/env python3
      #_*_ coding:utf-8 _*_
      #__author__='username'
      #__date__ = '20xx-xx-xx'  
      
      import itchat
      itchat.auto_login()                              #电脑端扫描二维码登陆wechat
      for friend in itchat.get_friends(update=True)[0:]:
           #可以用此句print查看好友的微信名、备注名、性别、省份、个性签名（1：男 2：女 0：性别不详）
          print(friend['NickName'],friend['RemarkName'],friend['Sex'],friend['Province'],friend['Signature'])
          img = itchat.get_head_img(userName=friend["UserName"])
          path = "/Users/xxx/HeadImages/"+friend['NickName']+"("+friend['RemarkName']+").jpg"
          try:
              with open(path,'wb') as f:
                  f.write(img)
          except Exception as e:
              print(repr(e))
      itchat.run()
```

### 2. 拼接好友头像

* 自定义python文件名，如jointheadimgs.py

```python
      #!/usr/bin/env python3
      #_*_ coding:utf-8 _*_
      #__author__='username'
      #__date__ = '20xx-xx-xx'
      import os
      from math import sqrt
      from PIL import Image
      path = '/Users/xxx/HeadImages/'        #path是存放好友头像图的文件夹的路径
      pathList = []
      for item in os.listdir(path):
          imgPath = os.path.join(path,item)
          pathList.append(imgPath)
      total = len(pathList)                  #total是好友头像图片总数
      line = int(sqrt(total))                #line是拼接图片的行数（即每一行包含的图片数量）
      NewImage = Image.new('RGB', (128*line,128*line))
      x = y = 0
      for item in pathList:
          try:
              img = Image.open(item)
              img = img.resize((128,128),Image.ANTIALIAS)
              NewImage.paste(img, (x * 128 , y * 128))
              x += 1
          except IOError:
              print("第%d行,%d列文件读取失败！IOError:%s" % (y,x,item))
              x -= 1
          if x == line:
              x = 0
              y += 1
          if (x+line*y) == line*line:
              break
      NewImage.save(path+"final.jpg")

