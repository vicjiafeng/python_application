# python单元测试框架unittest
___
### [unittest](https://www.cnblogs.com/hackerain/p/3682019.html)四个核心概念：
     
   * test case
     
   * test suite
     
   * test runner
     
   * test fixture
   
### unittest 静态类图
 
  ![](https://github.com/vicjiafeng/python_application/blob/master/apps/images/01.png)

* `一个TestCase的实例就是一个测试用例。什么是测试用例呢？就是一个完整的测试流程，包括测试前准备环境的搭建(setUp)，执行测试代码(run)，以及测试后环境的还原(tearDown)。元测试(unit test)的本质也就在这里，一个测试用例是一个完整的测试单元，通过运行这个测试单元，可以对某一个问题进行验证。`

* `而多个测试用例集合在一起，就是TestSuite，而且TestSuite也可以嵌套TestSuite。`

* `TestLoader是用来加载TestCase到TestSuite中的，其中有几个loadTestsFrom__()方法，就是从各个地方寻找TestCase，创建它们的实例，然后add到TestSuite中，再返回一个TestSuite实例。`

* `TextTestRunner是来执行测试用例的，其中的run(test)会执行TestSuite/TestCase中的run(result)方法。 测试的结果会保存到TextTestResult实例中，包括运行了多少测试用例，成功了多少，失败了多少等信息。`

* `而对一个测试用例环境的搭建和销毁，是一个fixture。`

### unittest 实例

#### 待测方法文件 mathfunc.py

```python
def add(a,b):
    return a+b
def minus(a,b):
    return a-b
def multi(a,b):
    return a*b
def divide(a,b):
    return a/b
```
#### 测试文件 test_mathfunc.py

```python
import unittest
from mathfunc import *

class TestMathFunc(unittest.TestCase):
    
    def test_add(self):
        self.assertEqual(3, add(1, 2))
        self.assertNotEqual(3, add(1, 2))
    def test_minus(self):
        self.assertEqual(1, minus(3, 2))
    def test_multi(self):
        self.assertEqual(6, multi(3, 2))
    def test_divide(self):
        self.assertEqual(3, divide(6, 2))
        self.assertEqual(2.5, divide(5, 2))
if __name__=='__main__':
    unittest.main()
```
#### 简单说明

  * `每个测试方法要以test开头，才能被unittest识别`
  * `用例执行的结果的标识，成功是 . ，失败是 F，出错是 E，跳过是 S, 且不是按方法的顺序执行测试的`
  * `在unittest.main()中加 verbosity 参数可以控制输出的错误报告的详细程度，默认是 1，如果设为 0，则不输出每一用例的执行结果，即没有上面的结果中的第1行；如果设为 2，则输出详细的执行结果`
  
### 组织TestSuite()
 ##### 1. 使添加到TestSuite的case按顺序执行
 ##### 2. 一次执行多个case
#### 创建test_suite.py
```python
import unittest
from test_mathfunc import TestMathFunc

if __name__ == '__main__':
    suite = unittest.TestSuite()
    tests = [TestMathFunc("test_add"), TestMathFunc("test_minus"), TestMathFunc("test_divide")]
    
    suite.addTests(tests)                    
    #suite.addTest(TestMathFunc("test_multi"))  可以直接添加单个case
    #suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestMathFunc))  用addTests + TestLoader，传入TestCase         
    #suite.addTests(unittest.TestLoader().loadTestsFromName('test_mathfunc.TestMathFunc'))     传入'模块名.TestCase名
    #用TestLoader的方法是无法对case进行排序的，同时，suite中也可以套suite
    
    with open('unittestTestReport.txt', 'a') as f:             #同目录下生成了UnittestTextReport.txt, 测试报告显示在txt文件中
        runner = unittest.TextTestRunner(stream=f, verbosity=2)   
        runner.run(suite)
```
#### test fixture的使用，帮助搭建测试环境和清理环境


