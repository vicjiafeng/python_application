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
 * 使添加到TestSuite的case按顺序执行
 * 一次执行多个case
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
### 使用test fixture，帮助搭建测试环境和清理环境
  * 修改前面的test_mathfunc.py文件，添加setUp()和tearDown()两个方法，即每次执行各个测试case时，前后分别执行setUp()和tearDown()方法，setUp用来为测试准备环境，tearDown用来清理环境

```python
class TestMathFunc(unittest.TestCase):

    def setUp(self):
        print "do something before test.Prepare environment."
    def tearDown(self):
        print "do something after test.Clean up."
    def test_add(self):
        print "add"
        self.assertEqual(3, add(1, 2))
        self.assertNotEqual(3, add(2, 2))
    def test_minus(self):
        ...
        ...
        ...
    pass
```
  * 如果想要在所有case执行之前准备一次环境，并在所有case执行结束之后再清理环境，我们可以把 setUpClass() 与 tearDownClass()编辑在类方法下
```python
class TestMathFunc(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        print "This setUpClass() method only called once."
        
        ...
        
    @classmethod
    def tearDown(cls):
        print "This tearDownClass() method only called once too."
```
### 跳过某个case
#### skip装饰器
```python
class TestMathFunc(unittest.TestCase):

    @unittest.skip("I don't want to run this case.")
    def test_minus(self):
        print "minus"
        self.assertEqual(1, minus(3, 2))
```
* skip装饰器一共有三个 `unittest.skip(reason)`、`unittest.skipIf(condition, reason)`、`unittest.skipUnless(condition, reason)`，skip无条件跳过，skipIf当condition为True时跳过，skipUnless当condition为False时跳过。

#### 另外也可以不用装饰器的方法，而是在对应方法定义下加`self.skipTest('Do not run this.')`即可
```python
class TestMathFunc(unittest.TestCase):
    
    def test_minus(self):
        self.skipTest('Do not run this.')
        print "minus"
        self.assertEqual(1, minus(3, 2))
```
### 扩展-使用HTMLTestRunner输出漂亮的HTML报告
 #### 需要下载第三方的unittest HTML报告库[python文件](http://tungwaiyip.info/software/HTMLTestRunner.html)，参考[这里](https://blog.csdn.net/huilan_same/article/details/52944782)
  
### 总结
* unittest是Python自带的单元测试框架，我们可以用其来作为我们自动化测试框架的用例组织执行框架
* unittest的流程：写好TestCase，然后由TestLoader加载TestCase到TestSuite，然后由TextTestRunner来运行TestSuite，运行的结果保存在TextTestResult中，我们通过命令行或者unittest.main()执行时，main会调用TextTestRunner中的run来执行，或者我们可以直接通过TextTestRunner来执行用例
* 一个class继承unittest.TestCase即是一个TestCase，其中以 test 开头的方法在load时被加载为一个真正的TestCase
* verbosity参数可以控制执行结果的输出，0 是简单报告、1 是一般报告、2 是详细报告
* 可以通过addTest和addTests向suite中添加case或suite，可以用TestLoader的loadTestsFrom__()方法
* 用 setUp()、tearDown()、setUpClass()以及 tearDownClass()可以在用例执行前布置环境，以及在用例执行后清理环境
* 我们可以通过skip，skipIf，skipUnless装饰器跳过某个case，或者用TestCase.skipTest方法
* 参数中加stream，可以将报告输出到文件：可以用TextTestRunner输出txt报告，以及可以用HTMLTestRunner输出html报告
