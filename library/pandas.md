# python_[pandas库](http://pandas.pydata.org/pandas-docs/stable/getting_started/10min.html)
___

## pandas数据处理

#### 1. 导入库

```python
         import numpy as np
         import pandas as pd
         import matplotlib.pyplot as plt
```
#### 2. 导入json文件

   * pandas的read_json方法将其转化为[DataFrame](http://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.html)格式
    
         df = pd.read_json('/Users/xxx/Python_全国JSON.json')
   
#### 3. 查看当前表信息

         df.index                       #查看行索引信息
         
         df.columns                     #查看列信息
         
         df.head()                      #默认查看前5行元素，括号内可任意指定数字。
 
         df.tail()                      #默认指定最后5行元素，同样可指定数字。

         df.info()                      #查看表整体信息
         
         df[['x1','x2']].head()         #查看df表中'x1'和'x2'两列前5个元素
         
#### 4. 数据规整

         替换索引：     df.index=df['x1']                 #自动添加索引替换为列'x1'

         删除某一列：   del(df['x1'])
         
         排序：        df1 = df.sort_index()             #直接df.sort_index()可返回索引的结果，但之后df还是原来的结构
         
         
#### 5. 一些常见函数

   * unique()
         
         df['Names'].unique()  >>>>>  array(['Mary', 'Jessica', 'Bob', 'John', 'Mel'], dtype=object)
         
   * value_counts()
   
         df['Names'].value_counts            #统计各个名字出现的次数
   
         
   * describe()
   
         df['Names'].describe()              #描述整体情况
   
   * zip()
   
         BabyDataSet = list(zip(names,births))          
         
         BabyDataSet  >>>>>     .....
         
   * groupby()
   
         ...

#### 6. 两种数据结构

* series
```python
s = pd.Series([1, 3, 5, np.nan, 6, 8])
```
* DataFrame 
```python
dates = pd.date_range('20130101', periods=6)
```

