# Django搭建blog 
___
### 步骤
* 安装`virtualenv`,然后激活`activate`虚拟环境
* 安装`django`,创建django项目`django-admin startproject blogproject`
* 可以在项目名文件下编辑`settings.py`文件，修改时区和语言
* 在项目目录下创建blog应用`python manage.py startapp blog`,并在settings文件中注册该应用
* 开发应用文件，首先在app目录下编辑模型类文件model.py,要注意每个模型要继承`models.Model`类(都是基于python进行编辑)
* 迁移数据库，在项目目录下分别运行`python manage.py makemigrations`和`python manage.py migrate`
* 进入交互模式`python manage.py shell`可进行'增删改查'的数据库操作
* 使用命令`python manage.py createsuperuser`创建用户
* 编写视图函数`view.py`
* 绑定URL与视图函数,即在应用文件目录下创建`urls.py`文件并规定命名空间，在文件中导入`views`模块，从`django.conf.urls`导入url函数,然后把网址和处理函数的关系写在了`urlpatterns`列表里
* 在项目目录下，编辑`urls.py`文件,把应用目录下的`urls.py`文件添加进来
* `python manage.py runserver`用于启动web服务器
* 创建模版系统，在项目根目录下创建templates文件夹，然后里面创建与应用名相同的文件夹，模版html文件就可以放到对应应用目录下，然后在`settings.py`文件中设置模版的路径`'DIRS': [os.path.join(BASE_DIR, 'templates')]`
* 修改视图文件，将http响应HttpResponse改为`render`函数
* 添加模版静态文件，在应用目录下创建static文件夹，然后再创建与应用同名的文件夹，将css/js文件夹添加到当前目录下，之后进行修改模版index文件

### Django后台搭建
* 创建超级用户
* 在应用目录下的`admin.py`文件中注册模型`admin.site.register()`
* 激活虚拟环境，运行开发服务器

### markdown语法
* 安装markdown-`pip install markdown`
* `markdown.markdowm()`可以传递额外的参数`extensions`对语法进行扩展,分别包含`markdown.extensions.extra`；`markdown.extensions.codehilite`表示语法高亮扩展; `markdown.extensions.toc`表示允许自动生成目录
* 安装Pygments-`pip install Pygments`

### 评论
* 在项目目录下新创comments应用，这是因为评论功能比较独立最好新创一个，然后在`settings`里注册
* 依照应用编辑步骤，首先编辑模型文件，然后迁移数据库
* 应用目录下新创表单`forms.py`文件，表单是用来收集并向服务器提交用户输入的数据的，要实现表单功能，要导入forms模块，然后必须继承`forms.ModelForm`类
* 编辑视图函数，绑定URL，包括应用目录下创建`urls.py`并规定命名空间，添加目录到项目url文件
* 更新文章详情页的视图文件(类似于关联comments与blog)
* 修改html模版
