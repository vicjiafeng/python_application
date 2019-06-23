# Pygal模块
___

`Pygal 是另一个简单易用的数据图库，它以面向对象的方式来创建各种数据图，而且使用 Pygal 可以非常方便地生成各种格式的数据图，包括 PNG、SVG 等。使用 Pygal 也可以生成 XML etree、HTML 表格`

### 安装

`pip install pygal`

`python -m pydoc -b`

### 实例

```python
#pygal.Pie()-饼图, pygal.Line()-线图, pygal.Bar()-柱状图, pygal.Dot()-点图, pygal.Gauge()-仪表图, pygal.Radar()-雷达图
#add() 方法添加数据
#调用 Config 对象的属性配置数据图
#用数据图对象的 render_to_xxx() 方法将数据图渲染到指定的输出节点

import pygal

x_data=[...]
y_data1=[...]
y_data2=[...]
#创建bar图
bar=pygal.Bar()

#stacked_bar = pygal.StackedBar()              创建pygal.StackedBar对象(叠加柱状图)

#添加两组代表条柱的数据
bar.add('曲线1',y_data1)
bar.add('曲线2',y_data2)

bar.x_labels = x_data

bar.title='...'
#设置X、Y轴的标题
bar.x_title='...'
bar.y_title='...'
#指定将数据图输出到SVG文件中
bar.render_to_file('fk_books.svg')
```
### 饼图
```python
import pygal

data=[...]
labels=[...]
#创建饼图
pie=pygal.Pie()
#采用循环为饼图添加数据
for i, per in enumerate(data):
    pie.add(labels[i], per)

pie.title='...'
#设置将图例放在底部
pie.legend_at_bottom = True

#pie.inner_radius = 0.4         #设置内圈的半径长度
#pie.half_pie=True              #创建半圆数据图

#指定将数据图输出到SVG文件中
pie.render_to_file('xxx.svg')
```
### 仪表图
```python
#仪表图创建与饼图类似，只是多了一个range属性，规定范围，指定仪表图的最小值和最大值
import pygal

...

gauge.range = [0, 1]

...
```
### 雷达图-雷达图适合用于分析各对象在不同维度的优势和劣势，通过雷达图可对比每个对象在不同维度的得分
```python
import pygal

data=[[1.2,1.3,1.1],[1.3,1.4.1.6],[1.3,1.5,1.3]]
labels=['java','python','c#']
#创建雷达图
rader=pygal.Radar()
#采用循环为雷达图添加数据
for i, per in enumerate(labels):
    rader.add(labels[i], data[i])
rader.x_labels = ['特性1','特性2','特性3']
rader.title='...'
#控制各数据点的大小
rader.dots_size=4
rader.legend_at_bottom = True

rader.render_to_file=('xxx.svg')
```

