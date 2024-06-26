## 一、DataFrame 日期数据转换

`pandas.to_datetime(arg, errors='ignore', dayfirst=False, yearfirst=False, utc=None, box=True,format=None, exact=True, unit=None,infer_datetime_format=False, origin='unix', cache=False)`

**参数说明**

`arg: 字符串、日期时间、字符串数组
errors：忽略错误（igonre），引发异常（raise），设置无效解析为 NaT（coerce）。
dayfirst: 默认为 False。如果为 True，解析第一个为天，例如：01/05/2022，解析为 2022-05-01
yearfirst: 默认为 False。如果为 True，解析第一个为年，例如：22-05-01，解析为 2022-05-01
utc: 默认为 None，返回协调世界时间（UTC）。
box: 默认为 True，返回 DatetimeIndex；如果为 False，返回值的 ndarray。
format: 格式化显示时间的格式。字符串，默认值为 None。
exact: 默认为 False。如果为 True，则要求格式完全匹配；如果为 False，则允许格式与目标字符串中的任意位置匹配。
infer_datetime_format: 默认为 False。没有格式时，尝试根据第一个日期推断出格式。
origin: 默认为 ‘unix’。定义参考日期。数值将解析为单位数。
cache: 默认值为 False。设置为 True 启用缓存加速。`

## 二、使用步骤

#### 1.各种日期格式转换示例：

```python
import pandas as pd
pd.set_option('display.unicode.east_asian_width', True) # 设置对齐
df = pd.DataFrame({'原日期': ['01-Mar-22', '05/01/2022', '2022.05.01', '2022/05/01', '20220501']})
df['日期'] = pd.to_datetime(df['原日期'])
print(df)
```

![在这里插入图片描述](https://img-blog.csdnimg.cn/4649742721624ae2a26e8d53c15c3180.png)

#### 2.将数组组合起来转换为日期数据（示例）：

```python
df1 = pd.DataFrame({
'year':[2022, 2021, 2020],
'month': [5, 4, 3],
'day': [6, 7, 8],
'hour': [12, 13, 2],
'minute': [22, 2, 10],
'second': [3, 34, 17]})
df1['组合日期'] = pd.to_datetime(df1)
print(df1)
```

![在这里插入图片描述](https://img-blog.csdnimg.cn/0b7d730f038b4a6999d5b07aa8ad3377.png)

#### 3.日期属性访问器对象（dt）

`Series.dt() # 返回 dt 对象`

dt 对象是 Series 对象中用于获取日期属性的访问器对象，使用它可以获取日期中的年、月、日、星期数和季度等，还可以判断日期是否属于年底。

**dt 对象的属性方法：**

- dt.year
- dt.month
- dt.day
- dt.dayofweek
- dt.dayofyear
- dt.is_leap_year
- dt.quarter
- dt.weekday_name

**获取年、月、日，具体代码如下：**

```python
df['年'] = df['日期'].dt.year
df['月'] = df['日期'].dt.month
df['日'] = df['日期'].dt.day
```

**获取日期所处的星期数：**

```python
df['星期几'] = df['日期'].dt.day_name()
```

**判断日期是否在年底最后一天：**

```py
df['是否年底'] = df['日期'].dt.is_year_end
```

**获取日期所属的季度：**

```python
df['季度'] = df['日期'].dt.quarter
```

![在这里插入图片描述](https://img-blog.csdnimg.cn/eb0e4a3f0ae44a2ea0961639cfeee1db.png)

#### 4.获取日期区间

当 DataFrame 对象使用日期为索引时，可以输入日期或日期区间获取数据。

**设置日期为索引：**

```python
df1.set_index(df1['组合日期'], inplace=True)
```

**获取 2021 年的数据**

```python
df1.loc['2021']
```

![在这里插入图片描述](https://img-blog.csdnimg.cn/7c0cba7e6f614e02ad654f6418b21ab5.png)

**获取 2022 年至 2020 年的数据**

```python
df1.loc['2022':'2020']
```

**获取具体某一天的数据（如 2022 年 5 月 6 日）**

```python
df1.loc['2022-5-06':'2022-05-06']
```

## 五、其他常用日期操作

#### 1. 计算日期差

要计算两个日期之间的差值，可以直接相减：

```python
delta = df1['组合日期'].max() - df1['组合日期'].min()
print(delta)
```

#### 2. 日期偏移

要在日期上进行加减操作，可以使用 `pd.DateOffset` 对象。例如，给定一个日期，我们想要找到它之后的 30 天：

```python
from pandas.tseries.offsets import DateOffset

date = pd.to_datetime('2022-05-01')
new_date = date + DateOffset(days=30)
print(new_date)
```

#### 3. 日期筛选

在处理日期时，我们可能需要根据日期进行筛选。例如，我们想要筛选出 DataFrame 中 2021 年的数据：

```python
mask = (df1['组合日期'] >= '2021-01-01') & (df1['组合日期'] <= '2021-12-31')
filtered_df = df1[mask]
print(filtered_df)
```

#### 4. 日期分组统计

在数据分析过程中，我们可能需要对日期进行分组统计。例如，我们想要按年份统计某个 DataFrame 的数据

```python
df1['年份'] = df1['组合日期'].dt.year
grouped_df = df1.groupby('年份').count()
print(grouped_df)
```
