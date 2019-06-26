# python数据库编程
___
### 创建数据库
`conn = sqlite3.connect('first.db')        #如果first.db文件存在,则打开的就是一个数据库；如果该文件不存在，则会在当前目录下创建相应的文件（即对应于数据库）`

### 创建游标
`c = conn.cursor()`

### 执行sql语句
`c.execute() / c.executemany             #执行查询`

### 
