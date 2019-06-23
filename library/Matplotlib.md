# Matplotlib库
___

       python中常用的可视化绘图库，可以通过简单的几行代码生成直方图，功率谱，条形图，错误图，散点图等。
       它和Ipython结合的很好，提供了一种非常好用的交互式数据绘图环境。绘制的图表也是交互式的，
       你可以利用绘图窗口中的工具栏放大图表中的某个区域或对整个图表进行平移浏览

### 简单举例
```python
import matplotlib.pyplot as plt

x_data=['2010','2011','2012','2013','2014','2015']
y_data1=[45,48,53,56,58,60]
y_data2=[47,49,52,58,62,64]
plt.plot(x_data,y_data1,color='red',linewidth=2.0,linestyle='--',label='曲线1',alpha=0.8)        #alpha表示透明度
plt.plot(x_data,y_data2,color='green',linewidth=3.0,linestyle='-.',label='曲线2',alpha=0.8)

#import matplotlib.font_manager as fm
#my_font=fm.FontProperties(fname="/path")       使用 FontProperties 类来加载 C:Windows\Fonts\simkai.ttf 文件所对应的中文字体
#plt.legend(handles=[l1,l2],labels=['曲线1','曲线2'],loc='lower right',prop=my_font)      prop指定选择的字体
#handles参数用于引用折线图上的每条折线；labels代表为每条折线所添加的图例,其中handle参数可以省略，则labels将顺序为折线添加图例；也可以handles，labels全部省略，直接传入label参数；loc参数指定图例的添加位置

#设置x轴,y轴名称
plt.xlabel("年份")
plt.ylabel("价格")

#设置图表标题
plt.title("食用油价格")
#设置y轴刻度值
plt.yticks([50,58],[r'正常',r'贵'])

#如果要对 X 轴、Y 轴进行更细致的控制，则可调用 gca() 函数来获取坐标轴信息对象，然后对坐标轴进行控制 => ax=plt.gca()

#创建子图用subplot()函数，subplot(nrows, ncols, index, **kwargs) 函数的 nrows 参数指定将数据图区域分成多少行；ncols 参数指定将数据图区域分成多少列；index 参数指定获取第几个区域

#调用show()显示图形
plt.show()

```

### 饼图

```python
import matplotlib.pyplot as plt

data=[...]
labels=[...]
explode=[...]
colors=[...]
#控制X轴和Y轴的范围（用于控制饼图的圆心，半径）
plt.xlim(0,8)
plt.ylim(0,8)
#将横、纵坐标轴标准化处理，保证饼图是一个正圆，否则为椭圆
plt.axes(aspect='equal')

#绘制饼图
plt.pie(x=data,labels=labels,explode=explode,colors=colors, ...)

plt.title=("...")

plt.show()
```

### 柱状图

```python
import matplotlib.pyplot as plt
import numpy as np

x_data=[...]
y_data1=[...]
y_data2=[...]
bar_width=0.5              #设定bar_width使不同柱状图依次显示

plt.bar(x=range(len(x_data)), height=y_data1, width=bar_width, ...)
plt.bar(x=np.arange(len(x_data))+bar_width, height=y_data2, width=bar_width, ...)

# 在柱状图上显示具体数值, ha参数控制水平对齐方式, va控制垂直对齐方式
for x, y in enumerate(y_data):
    #在使用 text() 函数输出文字时，该函数的前两个参数控制输出文字的 X、Y 坐标，第三个参数则控制输出的内容。其中 va 参数控制文字的垂直对齐方式，ha 参数控制文字的水平对齐方式
    plt.text(x, y + 100, '%s' % y, ha='center', va='bottom')
for x, y in enumerate(y_data2):
    plt.text(x, y + 100, '%s' % y, ha='center', va='top')
plt.title()    
plt.xlabel()
plt.ylabel()

plt.show()

#水平柱状图，和bar()用法一致，只是在调用 barh() 函数时使用 y参数传入 Y 轴数据，使用 width 参数传入代表条柱宽度的数据
plt.barh()    

```
### 散点图

```python
import matplotlib.pyplot as plt
import numpy as np

x_data=[...]
y_data1=[...]
y_data2=[...]

#绘制散点图，其中s表示指定散点的大小，c表示颜色，alpha表示透明度，edgecolors表示边框颜色,marker表示图形样式
plt.scatter(x=x_data,y=y_data1,s=5,c='red',alpha=0.8,edgecolors='blue',marker='p',linewidths=1)

plt.title()

plt.show()
```

### 绘制等高线
```python
import matplotlib.pyplot as plt
import numpy as np

delta=0.25
#生成x轴数据
x=np.arange(-3.0,3.0,delta)
#生成y轴数据
y=np.arange(-2.0,2.0,delta)
#对x、y数据执行网格化
X, Y = np.meshgrid(x, y)
Z1 = np.exp(-X**2 - Y**2)
Z2 = np.exp(-(X - 1)**2 - (Y - 1)**2)
#计算z轴数据
Z=(Z1-Z2)*2
#绘制等高线
c=plt.contour(x,y,Z,16,colors='black',linewidth=0.5)
#等高线填充颜色
plt.contourf(x,y,Z,16,cmap='rainbow')
#绘制等高线数据
plt.clabel(c,inline=True, fontsize = 10)
#去除坐标轴
plt.xticks(())
plt.yticks(())

plt.title()
plt.xlabel()
plt.ylabel()

plt.show()
```
### 绘制3D图形
```python
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure(figsize=(12, 8))
ax = Axes3D(fig)

delta=0.25
#生成x轴数据
x=np.arange(-3.0,3.0,delta)
#生成y轴数据
y=np.arange(-2.0,2.0,delta)
#对x、y数据执行网格化
X, Y = np.meshgrid(x, y)
Z1 = np.exp(-X**2 - Y**2)
Z2 = np.exp(-(X - 1)**2 - (Y - 1)**2)
#计算z轴数据(高度)
Z=(Z1-Z2)*2

#绘制3D图形
ax.plot.surface(X, Y, Z, rstride=1, cstride=1,cmap=plt.get_cmap('rainbow'))    #rstride（row）指定行的跨度, cstride(column)指定列的跨度

#设置z轴范围
ax.set_zlim(-2,2)

plt.title()

plt.show()
```


