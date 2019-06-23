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
plt.plot(x_data,y_data1,color='red',linewidth=2.0,linestyle='--',label='曲线1')
plt.plot(x_data,y_data2,color='green',linewidth=3.0,linestyle='-.',label='曲线2')

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
