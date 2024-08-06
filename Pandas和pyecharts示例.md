1.导入相关的库

```python
import pandas as pd
from pyecharts.charts import Bar
from pyecharts import options as opts
```

2.读取数据

```python
data = pd.read_csv("../data/buick_dealer.csv")
data
```

```python
#  查询省份为湖南并且城市为长沙的
data[(data['provinceName'] == '湖南省') & (data['cityName'] == '长沙市')]
```

```python
# 查询省份为湖南的数据
data[(data['provinceName'] == '湖南省')]
```

```python
# 查询城市为长沙或者衡阳市的数据
data[(data['cityName'] == '长沙市') | (data['cityName'] == '衡阳市')]
```

```python
# 统计每个省的门店数量
x = data.groupby('provinceName').agg({'provinceName': 'count'}).nlargest(10, 'provinceName')
x
```

```python
# 获取分组后的key
x1 = x.get('provinceName').keys().tolist()
x1
```

```py
# 获取分组的value
y1 = x.get('provinceName').values.tolist()
y
```

```python
# 生成柱状图
c = (
    Bar()
    .add_xaxis(x1)
    .add_yaxis("Buick门店数量", y1)
    .set_global_opts(
        title_opts=opts.TitleOpts(title="Buick门店数量"),
        xaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(rotate=-30)),
    )
)
c.render_notebook()
```

```python
# 生成一个新的DF，保存为湖南的门店数据
new_df = data[(data['provinceName'] == '湖南省')]
```

```python
# 统计每个市的门店数量
x = new_df.groupby('cityName').agg({'cityName': 'count'}).nlargest(14, 'cityName')
x
```

```python
# 获取分组后的key
x2 = x.get('cityName').keys().tolist()

```

```py
# 获取分组的value
y2 = x.get('cityName').values.tolist()
y2
```

```py
# 生成柱状图
c = (
    Bar()
    .add_xaxis(x2)
    .add_yaxis("Buick门店数量", y2)
    .set_global_opts(
        title_opts=opts.TitleOpts(title="Buick门店数量", subtitle="各市Buick门店数量"),
        legend_opts=opts.LegendOpts(is_show=False),
        xaxis_opts=opts.AxisOpts(splitline_opts=opts.SplitLineOpts(is_show=False)),
        yaxis_opts=opts.AxisOpts(splitline_opts=opts.SplitLineOpts(is_show=False)),
        visualmap_opts=opts.VisualMapOpts(is_show=False, ),
    )
)
c.render_notebook()
```
