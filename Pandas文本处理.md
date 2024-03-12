# 文本格式

- 转为小写字母：`Series.str.lower()`

- 转为大写字母：`Series.str.upper()`

- 转为标题：`Series.str.title()`将每个单词的首字母转为大写

- 首字母大写：`Series.str.ccapitalize()`

- 大小写互换：`Series.str.swapcase()`

- 转为小写字母(支持其他语言)：`Series.str.casefold()`
  

# 对齐方式

- Series.str.center(10,fillchar='一') #居中对齐，宽度为10，用“一”填充

- Series.str.ljust(10,fillchar='一') #左对齐

- Series.str.rjust(10,fillchar='一') #右对齐

- Series.str.ljust(width=10,size='left',fillchar='一') #指定宽度，填充内容对齐方式，填充内容

- Series.str.zfill(3) # 填充对齐，不足3位的前面加0
  

# 字符拆分

## split()方法

- Series.str.split() # 

- Series.str.split('-').get(1)  / Series.str.split('-').str[1]  # 读取切分后的字

- Series.str.split('-',expand=True) # 将返回的列表展开

- Series.str.split('-',expand=True,n=1) # 限制切分次数

- Series.str.rplit('-',expand=True,n=1) # 从字符串尾部向首部切分9
  

### slice切片

- Series.str.slice(1) #切掉第一个字符，留下剩余字符 

- Series.str.slice(stop=2) # 切掉索引为1之后的元

- Series.str.slice(start=0,stop=5,step=3)

### partition()方法

- Series.str.partition()  # 从右开始划分三部分，默认分隔符为空格，expand默认True

- Series.str.partition('-') 

- Series.str.partition('-',expand=False) # 将划分的结果转为一个元组列的Series
  

# 字符替换

## replace方法

```python
Series.str.replace(pat, repl, n= -1, case= Nne, flags= 0, regex= None)
# pat：匹配模式，可以是正则表达式也可以是re.compile()
# repl：新字符，可以是可迭代数据类型也可以是函数，
# n：替换次数，默认-1，替换全部
# case：确定替换是否区分大小写
# flags：正则表达式模块标志
# regex：确定是否假设passed-in模式是正则表达式
```

### 切片替换

```python
Series.str.slice_replace(start=None, stop=None, repl=None) # 替换为其他字符串
# start：替换次数
# stop：确定替换是否区分大小写
# repl：确定是否假设passed-in模式是正则表达式
```

# 字符拼接

`Series.str.cat(others=None, sep=None, na_rep=None, join='left')`
others：需要拼接的数据，该数据的长度必须跟Series对象相同
sep ：拼接用的分隔符
join ：连接方式，值的范围 {‘left’, ‘right’, ‘outer’, ‘inner’}


## 字符提取

`Series.str.extract(pat, flags= 0, expand= True)`  
pat：正则表达式  
flags：正则库re中的标识，re.IGNORECASE  
expand：是否展开内容返回DataFrame

# 文本查询

## find()方法

`Series.str.find(sub,start,end)`  
sub：要查找字符

start:起始位置

end:结束位置

### findall()方法

`Series.str.findall(pat, flags= 0, expand= True)`  
pat：正则表达式  
flags：正则库re中的标识，re.IGNORECASE  
expand：是否展开内容返回DataFrame

# 文本包含

`Series.str.contains(pat, case=True, flags=0, na=None, regex=True)`
pat: 匹配字符串或正则表达式
case: 是否区分大小写
flags: 正则库re中的标识，re.IGNORECASE
na: 对缺失值填充
regex: 是否支持正则


## 字符统计

`Series.str.count('a') `

`Series.str.count(r'a|b|c')`

 `Series.str.len()`

## 类别判断

`Series.str.isalpha()  # 所有字符是否都是字母
Series.str.isnumeric() #检测字符串是否由数字组成
Series.str.isalnum()  # 所有是否字母或数字组成
Series.str.isdigit() # 所有是否为数字
Series.str.isdecimal() # 检查字符串中是否只含有十进制字符
Series.str.isspace() # 所有是否空格
Series.str.islower() # 所有是否小写
Series.str.isupper() # 所有是否大写
Series.str.istitle() # 所有是否标题格式`

## 文本剔除

`Series.str.strip`


