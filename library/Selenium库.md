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

