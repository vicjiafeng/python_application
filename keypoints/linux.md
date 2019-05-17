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
         
* rm命令---删除一个目录中的一个或多个文件或目录，rm后面没有-r选项，则不会删除目录，rm删除文件仍可恢复
         
