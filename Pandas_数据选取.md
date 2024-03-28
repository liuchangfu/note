### 选择列

```python
# 查看指定列
df['Q1']
df.Q1 # 同上，如果列名符合 python 变量名要求，可使用

# 选择多列
df[['team', 'Q1']] # 只看这两列，注意括号
df.loc[:, ['team', 'Q1']] # 和上边效果一样
```

### 选择行

```python
# 用人工索引选取
df[df.index == 'Liver'] # 指定索引

# 用自然索引选择，类似列表的切片
df[0:3] # 取前三行,
df[0:10:2] # 前10个，每两个取一个
df.iloc[:10,:] # 前10个
```

### 指定行列

```python
df.loc['Ben', 'Q1':'Q4'] # 只看 Ben 的四个季度成绩
df.loc['Eorge':'Alexander', 'team':'Q4'] # 指定行区间
```

### 条件选择

```python
# 单一条件
df[df.Q1 > 90] # Q1 列大于90的
df[df.team == 'C'] # team 列为 'C' 的
df[df.index == 'Oscar'] # 指定索引即原数据中的 name

# 组合条件
df[(df['Q1'] > 90) & (df['team'] == 'C')] # and 关系
df[df['team'] == 'C'].loc[df.Q1>90] # 多重筛选
```

例子说明

```py
import pandas as pd

# 创建一个数据集
data = {
    "Name": ["Alice", "Bob", "Charlie", "David", "Eve"],
    "Age": [25, 32, 18, 47, 22],
    "City": ["New York", "Los Angeles", "London", "Tokyo", "Shanghai"]
} 


df = pd.DataFrame(data, index=['a', 'b', 'c', 'd', 'e']) # 设置索引
df.loc['a'] # 选择行索引为 'a' 的数据 
df.loc[['a', 'b']] # 会选择行索引为 'a' 和 'b' 的数据。 
df.loc[:, 'Name'] # 选择 'Name' 列的所有数据。冒号 : 表示选择所有行。 
df['Name'] # 效果与上面相同 
df.loc['a':'c'] # 输出索引从 'a' 到 'c' 的所有行的所有值 
df.loc['b':'d', 'Name'] # 输出索引从 'b' 到 'd' 的行，'Name' 列的所有值  
df.loc['a':'c', ['Name', 'City']] # 输出索引从 'a' 到 'c' 的行，'Name' 和 'City' 列的所有值。
df.loc[df['Age'] > 30, 'Name'] #  选Name列，age大于30的列
df.loc[df['Age'] > 30] # 输出 'Age' 大于30的所有行的所有值 
df.loc[lambda df: df['Age'] == 25] # 输出 'Age' 等于25的所有行的所有值


data = {
    "Name": ["Alice", "Bob", "Charlie", "David"],
    "Age": [25, 32, 18, 47],
    "City": ["New York", "Los Angeles", "London", "Tokyo"]
} 


df.iloc[0] # 输出第0行（在Python中，索引是从0开始的）的所有值 
df.iloc[[0, 2]] # 输出第0行和第2行的所有值 

```


