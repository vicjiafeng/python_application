# python装饰器的作用、原理和实现
___
### 原理
   `python中的装饰器利用函数特性的闭包实现的`
### 闭包的实现
   `闭包就是引用了外部变量的内部函数, 其实现用到函数如下特性：`
   
   * 函数作为变量传递
   * 函数作为参数传递
   * 函数作为返回值
   * 函数的嵌套及跨域访问
   
#### 实例
```python
def func():
    return 'function'
def outer(x):
    def inner():
        return 'it is good' + x()      #引用外部变量x
    return inner

closure = outer(func)
print(closure())                       #执行闭包

#结果：>>>it is good  function 
```
#### 解析：
 `closure实际上是outer(func)，func作为参数传进outer，outer的子函数inner对func返回的结果进行了一番装饰，返回了一个装饰后的结果，最后outer返回inner，可以说inner就是装饰后的func，这就是一个函数被装饰的过程，重点在于执行 outer(func) 这个步骤`
 
### 构造装饰器@
```python
def outer(x):
    def inner():
        return 'it is good' + x()     
    return inner

@outer
def func():
    return 'function'

print(func())

#结果：>>>it is good  function 

```
#### 解析：
`拿来把被装饰的函数作为参数传递到装饰器函数里面加工的，最后执行被装饰的函数`

### 扩展
  * 如果有两个装饰器
  
  `先用第二个装饰器进行装饰，接着再用第一个装饰器进行装饰，而在调用过程中，先执行第一个装饰器，接着再执行第二个装饰器`
  
  * 带参数的装饰器
  
  `带参数的装饰器就是在原闭包的基础上又加了一层闭包`
