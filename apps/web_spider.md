# python爬虫招聘网站
___
### python 代码
```python
# coding:utf-8
import re
import urllib.request
import xlwt               #用来创建excel文档并写入数据的库

def get_content(page):
    url = 'https://search.51job.com/list/040000,000000,0000,00,9,99,%2B,2,'+str(page)+'.html'       #爬取的网站网址
    a = urllib.request.urlopen(url)               #打开网址
    html = a.read().decode('gbk')               #读取代码并转换为unicode
    return html
def get(html):
      # f12解析source，正则匹配
    reg = re.compile(r'class="t1 ">.*? <a target="_blank" title="(.*?)".*? <span class="t2"><a target="_blank" title="(.*?)".*?<span class ="t3">(.*?)</span>.*?<span class="t4">(.*?)</span>.*?<span class"t5">(.*?)</span>',re.S)
    items=re.findall(reg,html)                 #进行匹配
    items_length = len(items)
    return items,items_length
def excel_write(items,index):                  #爬取到的内容写入excel表格
    for item in items:             
        for i in range(0,5):
            ws.write(index,i,item[i])
        print(index)
        index += 1
newTable="test.xls"                                #表格名称
wb = xlwt.Workbook(encoding='utf-8')
ws = wb.add_sheet('sheet1')                        #创建excel表格
headData = ['招聘职位','公司','地址','薪资','日期']    #表头信息
for column in range(0,5):
    ws.write(0,column,headData[column],xlwt.easyxf('font: bold on'))
for each in range(1,5):                #循环读取页面
    index=(each-1)*50+1
    excel_write(get(get_content(each)),index)
wb.save(newTable)
```
