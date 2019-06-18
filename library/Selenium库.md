# Selenium库
___
### 简介

* Selenium是一个用于测试网站的自动化测试工具，以及基于web的任务管理自动化，支持各种浏览器包括Chrome、Firefox、Safari等主流界面浏览器，同时也支持phantomJS无界面浏览器

### 特点

* 支持录制和回放(Selenium IDE)

* 能够分布式运行在不同机器和异构环境中

* 通过WebDriver，直接控制浏览器，而不是通过拦截HTTP请求，实现真正模仿了用户的操作

### 安装
 1. `pip/pip3 install selenium`
 
 2. 下载对应[浏览器的驱动](https://selenium-python.readthedocs.io/installation.html#drivers)
 
 3. 安装目标浏览器，并把可执行程序所在的目录添加到PATH环境变量中，以便Selenium能找到该浏览器

#### -Python 程序即可使用 Selenium 来启动浏览器，并驱动浏览器浏览目标网站

### 提高稳定性和执行速度

(1)页面加载内容太多--设置超时时间，中断页面加载

(2)网络原因--设置等待时间

(3)优化代码，减少冲突函数

(4)尽可能少用sleep，优化等待时间

### 定位方式

 |定位方式              |对应定位方法                        |
 |--------------------|-----------------------------------|
 |id                  |find_element_by_id()               |
 |name                |find_element_by_name()             |
 |class name          |find_element_by_class_name()       |
 |tag name            |find_element_by_tag_name()         |
 |link text           |find_element_by_link_text()        |
 |partial link text   |find_element_by_partial_link_text()|
 |xpath               |find_element_by_xpath()            |
 |css selector        |find_element_by_css_selector()     |
 
* 注：如果是定位多个元素，则把对应方法的`element`变为`elements`即可

### Selenium库下webdriver模块常用方法的使用
#### 控制浏览器操作

|方法          	         |说明              |
|-----------------------|------------------|
|set_window_size()      |设置浏览器的大小     |
|back()                 |控制浏览器后退       |
|forward() 	            |控制浏览器前进       | 
|refresh()	             |刷新当前页面         |
|clear()	               |清除文本            |
|send_keys (value)	     |模拟按键输入         |
|click()	               |单击元素            |
|submit()	              |用于提交表单         |
|get_attribute(name)	   |获取元素属性值        |
|is_displayed()	        |设置该元素是否用户可见 |
|size	                  |返回元素的尺寸        |
|text	                  |获取元素的文本        |

### webdriver模块中其他一些操作，[参考](https://blog.csdn.net/weixin_36279318/article/details/79475388)

### 利用scrapy创建项目,使用selenium调用浏览器登陆要爬取的网站
 * [参考实例](http://c.biancheng.net/view/2764.html)
 
### 测试网站实例

* 步骤

`安装对应webdriver；利用driver打开测试网页；在网页上f12打开弹出调试工具；利用上文定位方法定位对应id，文本等元素，编写循环等测试用例；基于验证码的问题解决`

* 总结

`自动化测试的优点是测试很快，很广泛的查找缺陷，无需人工重复操作，提高效率，但同时并不能完全发现细微错误，容易受到网速，方法复杂度，等待时间的影响；总之制定稳定高效的测试才是关键`
