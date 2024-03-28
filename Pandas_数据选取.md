df.loc: 语法格式是df.loc[<行表达式>, <列表达式>]，如果列不传将返回所有的行，loc操作通过索引和列的条件筛选出数据

1. 选择行：df.loc[row_index] 会选择指定行索引的数据。

2. 选择多行：df.loc[[row_index1, row_index2]] 会选择多个行索引的数据。

3. 选择行的范围（切片）：df.loc[start_row_index:end_row_index] 会选择从开始到结束行索引的数据

4. 选择列：df.loc[:, column_index] 会选择指定列索引的数据。

5. 选择多列：df.loc[:, [column_index1, column_index2]] 会选择多个列索引的数据。

6. 选择行和列：df.loc[row_index, column_index] 会选择指定行索引和列索引的数据。

7. 布尔索引：df.loc[boolean_series] 会选择布尔序列为 True 的行。

df.iloc: 语法格式是df.iloc[<行表达式>, <列表达式>],格式可以使用数字索引（行和列的0~n索引）进行筛选数据，意味着iloc[]的表达式只支持数据切片的形式.

1. 单个整数：返回该位置对应的行

2. 整数列表：返回位置列表中所有位置对应的行

3. 整数切片：返回位置范围内的行

4. 

| 操作       | 语法              | 返回结果      | 操作逻辑         |
| -------- | --------------- | --------- | ------------ |
| 选择列      | `df[col]`       | Series    | 支持标签、位置（0开始） |
| 按索引选择行   | `df.loc[label]` | Series    | 仅标签          |
| 按数字索引选择行 | `df.iloc[loc]`  | Series    | 仅位置          |
| 使用切片选择行  | `df[5:10]`      | DataFrame | 支持标签、位置（0开始） |
| 用表达式筛选行  | `df[bool_vec]`  | DataFrame | 对应索引位上真值     |

注：标签包含右则、位置（0开始）如同 Python 切片，不包含右则

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
