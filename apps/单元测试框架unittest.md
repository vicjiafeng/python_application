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

     
