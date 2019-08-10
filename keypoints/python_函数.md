# python_函数
___
### 1.round()函数
* 返回浮点数x的四舍五入值
```python
round(x,n)  --->  round(29.1102, 2): 29.11
```
### 2.strftime()函数
```python
time.strftime('format')         #按format格式输出时间
```
### 3.zip()函数
* zip函数将可迭代对象作为参数，将对象中对应元素打包成一个元组，返回这些元组的列表
* zip函数对象前加`*`操作符,返回对象中每个元素对应位置打包成的一个元组，且是最短对象
```python
nums=['vic','victory','victoria']
for i in zip(*nums):
  print(i)

>> ('v','v','v')
   ('i','i','i')
   ('c','c','c')
```
