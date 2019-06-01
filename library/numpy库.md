# [Numpy](https://docs.scipy.org/doc/numpy/user/quickstart.html)库
___
## [Numpy](https://blog.csdn.net/xjl271314/article/details/80409034)是一个由多维数组对象和用于处理数组的例程集合组成的库，用于数据生成和一些计算。

### 1. 安装

 * python下安装
 
  `pip install numpy`
  
 * 引入
```python
import numpy as np
```

### 2. 特性

         1. 快速高效的多维数组对象ndarray。
         2. 用于对数组执行元素级计算以及直接对数组执行数学运算的函数。
         3. 用于读写硬盘上基于数组的数据集的工具。
         4. 线性代数运算、傅里叶变换，以及随机数生成。
         5. 用于将C、C++、Fortran代码集成到Python的工具。

### 3. 属性指令 

* numpy中数组array命名为narray

`narray.ndim: 维度`

`narray.shape: 行数和列数`

`narray.reshape: 调整数组大小,不对原数据修改`

`narray.size: 元素的个数`

`numpy.resize: 返回指定大小的新数组,如果新数组大小大于原始大小，则包含原始数组中的元素的重复副本`

`narray.dtype: 数组数据类型`

`narray.itemsize: 数组中每个元素的字节单位长度`

### 4. 创建numpy数组

`np.array(object, dtype=None)：使用Python的list或者tuple创建数据`

`np.zeors(shape, dtype=float)：创建全为0的数据`

`np.ones(shape, dtype=None)：创建全为1的数据`

`np.empty(shape, dtype=float)：创建没有初始化的数据,生成随机值`

`np.arange([start, ]stop, [step, ]dtype=None)：创建固定间隔的数据段`

`np.linspace(start, stop, num=50, dtype=None)：在给定的范围，均匀的创建数据`

* 从已有的数据创建数组

`numpy.asarray(a, dtype=None, order=None)  a表示输入的参数(元组,列表)，dtype表示数组类型，order表示数组风格`

`numpy.fromiter(iterable, dtype=, count=-1)  a表示可迭代对象，dtype表示数组类型，count表示读取的数据数量，默认为-1全部读取`

### Numpy广播-在算术运算期间处理不同形状的数组的能力

* 例如在numpy中可以实现一个一维数组与二维数组相加

#### 如果满足以下规则，可以进行广播
* ndim(维度)较小的数组会在前面追加一个长度为 1 的维度。
* 输出数组的每个维度的大小是输入数组该维度大小的最大值。
* 如果输入在每个维度中的大小与输出大小匹配，或其值正好为 1，则在计算中可它。
* 如果输入的某个维度大小为 1，则该维度中的第一个数据元素将用于该维度的所有计算。

### 常用数组操作

|方法           	|描述                       |
|---------------|---------------------------|
|flat           |数组上的一维迭代器            |
|flatten        |返回折叠为一维的数组副本       |
|ravel	         |返回展开的一维数组            |
|transpose	     |翻转数组的维度               |
|ndarray.T	     |和self.transpose()相同      |
|rollaxis	      |向后滚动指定的轴             |
|swapaxes	      |互换数组的两个轴             |

### 数组的连接

* numpy.concatenate沿指定轴连接相同形状的两个或多个数组

`numpy.concatenate((a1, a2, ...), axis)`

* numpy.stack沿新轴连接数组序列

`numpy.stack(arrays, axis)`

* numpy.hstack水平堆叠序列中的数组(列方向)

`numpy.hstack((a,b))`

* numpy.vstack竖直堆叠序列中的数组(行方向)

`numpy.vstack((a,b))`

### 数组分割

* numpy.split分割

`np.split(ary, indices_or_sections, axis)   ary表示被分割的输入数组，indices_or_sections，如果是整数表明要分割的子数组数量，如果是数组，则表明要创建新子数组开始的点，axis默认为0`

* numpy.hsplit分割

`np.hsplit(a,2)    其中轴为 1 表示水平分割,不考虑维度`

* numpy.vsplit分割

`np.vsplit(a,2)    其中轴为 0 表示竖直分割,不考虑维度`







