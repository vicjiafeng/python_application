# MySQL数据库
___

### 1. 基本语法

 * 创建数据表
 
          CREATE TABLE NAME
 
 * 删除数据表
 
          DROP TABLE NAME
 
 * 修改数据表
 
          ALTER TABLE NAME ADD/DROP/CHANGE
          
          ALTER TABLE name1 RENAME TO name2
          
 * 增数据
 
          INSERT INTO table_name ...
          
 * 删数据
 
          DELETE FROM table_name where...
 
 * 改数据
 
          UPDATE table_name SET ...
 
 * 查数据
 
          SELECT ... FROM table_name WHERE...
                                             [ORDER BY]/[GROUP BY]             #使用 ASC 或 DESC 关键字来设置查询结果是按升序或降序排列
                                             [INNER/LEFT/RIGHT JOIN]
                                             [LIKE(%)]                         #使用百分号 %字符来表示任意字符
                                             [UNION(ALL)]                      #UNION 操作符用于连接两个以上的 SELECT 语句的结果组合到一个结果集合中
  
