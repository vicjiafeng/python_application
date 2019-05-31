# Selenium库
___
### 简介

* Selenium是一个用于测试网站的自动化测试工具，支持各种浏览器包括Chrome、Firefox、Safari等主流界面浏览器，同时也支持phantomJS无界面浏览器

### 安装
 1. `pip/pip3 install selenium`
 
 2. 下载对应[浏览器的驱动](https://selenium-python.readthedocs.io/installation.html#drivers)
 
 3. 安装目标浏览器，并把可执行程序所在的目录添加到PATH环境变量中，以便Selenium能找到该浏览器

#### Python 程序即可使用 Selenium 来启动浏览器，并驱动浏览器浏览目标网站

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
