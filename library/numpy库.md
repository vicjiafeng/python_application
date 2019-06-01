# [Numpy](https://docs.scipy.org/doc/numpy/user/quickstart.html)库
___
## [Numpy](https://cloud.tencent.com/developer/article/1333316)是一个由多维数组对象和用于处理数组的例程集合组成的库，用于数据生成和一些计算。

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
=
`narray.ndim: 维度`

`narray.shape: 行数和列数`

`narray.reshape: 调整数组大小,不对原数据修改`

`narray.size: 元素的个数`

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




