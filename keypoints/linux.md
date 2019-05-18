#  -.-   Linux

It is just talking about some basic Linux instructions
___
### 常用指令
* ls命令

         ls -a 列出目录所有文件，包含以.开始的隐藏文件

         ls -A 列出除.及..的其它文件

         ls -r 反序排列

         ls -t 以文件修改时间排序

         ls -S 以文件大小排序

         ls -h 以易读大小显示

         ls -l 除了文件名之外，还将文件的权限、所有者、文件大小等信息详细列出来
* cd命令

         cd /   进入目录
         
         cd ~   进入家(home)
         
         cd -   进入上次工作路径
         
         cd !$  把上个命令参数作为cd参数使用
* pwd命令

         pwd       查看当前路径
         
         pwd -p    查看软链接实际路径
* mkdir命令

         mkdir t    创建名为t的文件夹
         
         mkdir -p /tmp/test1/file1/t    在tmp目录下创建路径为/test1/file1/t 的目录，若不存在则创建     
         
* rm命令--删除一个目录中的一个或多个文件或目录，rm后面没有-r选项，则不会删除目录，rm删除文件仍可恢复


         rm [选项] 文件
         
         rm -i *.log          删除log文件，删除前逐一询问确认
         
         rm -- -f*            删除f开头的文件
       
* mv命令

         mv test.log test1.txt         将第一个文件test.log重命名为test.txt
         
         mv test.log /test1            将test.log移动到test1目录下
         
         mv *../                       移动当前文件夹下的所有文件到上一级目录
         
* cp命令--将原文件复制到目标文件/目标目录
         
         cp a.txt test               将a.txt文件复制到test目录
         
         cp a.txt link_a.txt         将a.txt文件建立一个链接
         
* cat命令(more/less 看文件)

         cat filename                显示整个文件
         
         cat >file                   创建新文件
         
         cat file1 file2 >file       将几个文件合为一个文件
         
* head命令

         head test.txt -n 20         显示文件text.txt的前20行（-n表示显示行数，20表示多少行，如果为负数则表示从最后往前）
         
* tail命令

         tail -f file.log            查看日志
         
* which命令

         which ls/cd                 查看ls/cd命令是否存在，及存在的路径
         
* whereis命令

 > 常用参数：

  -b   定位可执行文件。

  -m   定位帮助文件。

  -s   定位源代码文件。

  -u   搜索默认路径下除可执行文件、源代码文件、帮助文件以外的其它文件。
         
         whereis <参数> filename
         
* locate命令-通过搜寻系统内建文档数据库达到快速找到档案

         locate -i /etc/sh              搜寻etc目录下所有以sh开头的文件,-i表示忽略大小写
         
* find命令

         find <指定目录> <指定条件> <指定动作>
         
         find . -name 'my*'             搜寻当前目录中文件名以my开头的文件
         
         find . -mmin 10                搜寻当前目录中，过去10mins更新过的所有文件和目录
         
* chmod命令

  >权限范围
  
    u ：目录或者文件的当前的用户

    g ：目录或者文件的当前的群组

    o ：除了目录或者文件的当前用户或群组之外的用户或者群组

    a ：所有的用户及群组
    
   >权限代号
   
     r ：读权限，用数字4表示

     w ：写权限，用数字2表示

     x ：执行权限，用数字1表示

     - ：删除权限，用数字0表示

     s ：特殊权限

         chmod a+x test.txt           增加文件test.txt所有用户可执行权限
         
* tar命令

         
         
  
          
         

         
         
