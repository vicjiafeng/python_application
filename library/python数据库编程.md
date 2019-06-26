# python数据库编程
___
### 创建数据库
`conn = sqlite3.connect('first.db')        #如果first.db文件存在,则打开的就是一个数据库；如果该文件不存在，则会在当前目录下创建相应的文件（即对应于数据库）`

### 创建游标
`c = conn.cursor()`

### 执行sql语句
`c.execute() / c.executemany             #执行查询`

### 获取查询结果
`c.fetchone() / c.fetchmany(n) / c.fetchall()`

### 其他

`c.description                     #description：该只读属性可获取最后一次查询返回的所有列的信息`

`c.rowcount                        #该属性返回受 SQL 语句影响的行数`

`c.executescript()                 #执行复杂sql脚本`

`注册自定义函数: create_function(name, num_params, func)         #name:自定义函数名字，num_params:函数参数个数，func：自定义函数` 

`自定义聚集函数: create_aggregate(name, num_params, aggregate_class)          #aggregate_class:聚集函数的实现类,必须实现step(),finalize()方法`

`自定义比较函数: create_collation(name, callable)          #callable函数包含两个参数，并对这两个参数进行大小比较，如果该方法返回正整数，系统认为第一个参数更大；如果返回负整数，系统认为第二个参数更大；如果返回0，系统认为两个参数相等`

### 实例
```python
import sqlite3

conn = sqlite3.connect('first.db')              #打开数据库
c = conn.cursor()                               #获取游标

#执行DDL语句创建数据表
#对应name/pass等后面的text/real代表数据类型，text(文本),real(浮点数),integer,null,BLOB(大二进制对象)
c.execute('''create table user_tb(_id integer primary key autoincrement, name text, pass text, gender text)''')
c.execute('''create table order_tb(_id integer primary key autoincrement, item_name text, item_price real, item_number real, user_id integer, foreign key(user_id) references user_tb(_id))''')

#执行DML的insert、update、delete语句
c.execute('insert into user_db values(null, ?, ?, ?)',('vic','12345','male'))     #向user_tb表添加内容，可使用executemany()添加多条
c.commit()                 #提交事物

#执行select查询语句
c.execute('select * from user_tb where id>?', (2,))
print('查询返回的记录数:', c.rowcount)
while True:
    row = c.fetchone()               #获取一行记录，每行数据都是一个元组,也可以fetchmany(3)获取3行数据元组
    if not row:
        break
    print(row)
    print(row[1] + '-->' + row[2])
    
'''c.execute('select * from user_tb order by pass collate sub_cmp')      #在SQL语句中使用sub_cmp自定义的比较函数'''

c.close()                              #关闭游标
conn.close()                           #关闭数据库
``` 
### MySQL数据库
* 使用MySQL数据库，首先要安装MySQL

* 连接数据库 `conn=conn=mysql.connector.connect(user='root',password='12345',host='localhost',port='3306',dababase='python',use_unicode=True)                   #如果不指定服务器 IP 地址和端口，则使用默认的服务器 IP 地址 localhost 和默认端口 3306` 

* 执行DML语句的占位符为`%s`

* 可以设置`conn.autocommit = True`实现完成执行语句后自动提交事务

* 调用存储过程使用`callproc(self, procname, args=())`方法，其中`procname`参数代表存储过程的名字，而`args()`参数则用于为存储过程传入参数
