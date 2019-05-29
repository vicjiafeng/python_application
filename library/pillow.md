# 处理图像的pillow库
___

### 1. 安装

         pip install pillow      #pip3 install pillow

### 2. 终端操作

```python
   >>>from PIL import Image
   >>>image=Image.open('/Users/feng/xxx.jpg')
   >>>image.format, image.size, image.mode
   >>> ....
   >>>image.show()
   
     ...咚咚咚，图片自动显示出来拉！
   >>>rect = 100,100,100,100           #剪裁图片，数据表示尺寸
   >>>image.crop(rect).show()          #显示剪裁后的图片
   
   >>>size = 128,128                   #生成缩略图，数据表示size
   >>>image.thumbnail(size)
   >>>image.show()                     #显示缩略图
   
   >>>image.rotate(180).show()                       #旋转图片
   >>>image.transpose(Image.FLIP_LEFT_RIGHT).show()  #翻转图片
   
   >>>xx_head = image2.crop(rect)
   >>>width, height = xx_head.size
   >>>image1.paste(xx_head.resize((int(width/1.2),int(height/1.2))),(xx,xx))   #缩放/粘贴图像
   
   from PIL import ImageFilter
   >>>image.filter(ImageFilter.CONTOUR).show()        #增添滤镜效果
```
