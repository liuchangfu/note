[官网API帮助说明](https://docs.streamlit.io/)

[streamlit中文开发手册（详细版）-CSDN博客](https://blog.csdn.net/weixin_44458771/article/details/135495928)

Demo示例

> ```python
> # coding=utf-8
> """
> @IDE：PyCharm
> @project: Streamlit_Demo
> @Author：Sam Lau
> @file： market_sales.py
> @date：2024/7/5 下午4:21
>  """
> import streamlit as st
> import pandas as pd
> import numpy as np
> import plotly.express as px
> 
> # # 设置网页信息,须要在顶部
> st.set_page_config(page_title='超市销售明细', page_icon=':bar_chart:', layout='centered')
> 
> 
> def get_data_from_csv():
>     df = pd.read_csv('2024年超市销售明细.csv', encoding='gbk')
>     # 添加小时列数据
>     df["小时"] = pd.to_datetime(df["时间"], format="%H:%M").dt.hour
>     return df
> 
> 
> df = get_data_from_csv()
> st.dataframe(df)
> 
> # 侧边栏
> st.sidebar.header('请在这里筛选:')
> city = st.sidebar.multiselect(
>     '选择城市:',
>     options=df['城市'].unique(),
>     default=df['城市'].unique()
> )
> 
> customer_type = st.sidebar.multiselect(
>     '选择客户类型:',
>     options=df['客户类型'].unique(),
>     default=df['客户类型'].unique()
> )
> 
> gender = st.sidebar.multiselect(
>     '选择性别:',
>     options=df['性别'].unique(),
>     default=df['性别'].unique()
> )
> 
> df_selected = df.query("城市 == @city & 客户类型 == @customer_type & 性别 == @gender")
> 
> # 主页面
> st.title(':bar_chart:超市销售明细')
> st.markdown('##')
> 
> # 核心指标, 销售总额、平均评分、星级、平均销售额数据
> total_sales = int(df_selected['总价'].sum())
> average_rating = round(df_selected['评分'].mean(), 1)
> star_rating = ":star:" * int(round(average_rating, 0))
> average_sale_by_transaction = round(df_selected["总价"].mean(), 2)
> 
> # 3列布局
> left_column, middle_column, right_column = st.columns(3)
> 
> with left_column:
>     st.subheader('销售总额')
>     st.subheader(f'RMB:{total_sales:,}')
> 
> with middle_column:
>     st.subheader('平均评分')
>     st.subheader(f'{average_rating} {star_rating}')
> 
> with right_column:
>     st.subheader('平均销售额')
>     st.subheader(f'RMB:{average_sale_by_transaction}')
> 
> # 分隔符
> st.markdown("""---""")
> 
> # 各类商品销售情况(柱状图)
> sales_by_product_line = (
>     df_selected.groupby(by=["商品类型"]).sum()[["总价"]].sort_values(by="总价")
> )
> fig_product_sales = px.bar(
>     sales_by_product_line,
>     x="总价",
>     y=sales_by_product_line.index,
>     orientation="h",
>     title="<b>每种商品销售总额</b>",
>     color_discrete_sequence=["#0083B8"] * len(sales_by_product_line),
>     template="plotly_white",
> )
> fig_product_sales.update_layout(
>     plot_bgcolor="rgba(0,0,0,0)",
>     xaxis=(dict(showgrid=False))
> )
> 
> # 每小时销售情况(柱状图)
> sales_by_hour = df_selected.groupby(by=["小时"]).sum()[["总价"]]
> print(sales_by_hour.index)
> fig_hourly_sales = px.bar(
>     sales_by_hour,
>     x=sales_by_hour.index,
>     y="总价",
>     title="<b>每小时销售总额</b>",
>     color_discrete_sequence=["#0083B8"] * len(sales_by_hour),
>     template="plotly_white",
> )
> fig_hourly_sales.update_layout(
>     xaxis=dict(tickmode="linear"),
>     plot_bgcolor="rgba(0,0,0,0)",
>     yaxis=(dict(showgrid=False)),
> )
> 
> # 2列布局
> left_column, right_column = st.columns(2)
> left_column.plotly_chart(fig_hourly_sales, use_container_width=True)
> right_column.plotly_chart(fig_product_sales, use_container_width=True)
> 
> # 隐藏streamlit默认格式信息
> hide_st_style = """
>             <style>
>             #MainMenu {visibility: hidden;}
>             footer {visibility: hidden;}
>             header {visibility: hidden;}
>             <![]()yle>
>             """
> 
> st.markdown(hide_st_style, unsafe_allow_html=True)
> ```

运行代码：`streamlit run 文件名.py`

 多页面Demo

`Home.py`

```python
# coding=utf-8
"""
@IDE：PyCharm
@project: Streamlit_Demo
@Author：Sam Lau
@file： Home.py
@date：2024/7/3 下午3:15
 """
# https://juejin.cn/column/7265946243196436520 教程
import streamlit as st

st.set_page_config(
    page_title="你好",
    page_icon="👋",
)

st.write("# 欢迎使用 Streamlit! 👋")

st.sidebar.success("在上方选择一个演示。")

st.markdown(
    """
    Streamlit 是一个专为机器学习和数据科学项目而构建的开源应用框架。
    **👈 从侧边栏选择一个演示**，看看 Streamlit 能做什么吧！
    ### 想了解更多吗？
    - 查看 [streamlit.io](https://streamlit.io)
    - 阅读我们的 [文档](https://docs.streamlit.io)
    - 在我们的 [社区论坛](https://discuss.streamlit.io) 提问
    ### 查看更复杂的示例
    - 使用神经网络来 [分析 Udacity 自动驾驶汽车图像数据集](https://github.com/streamlit/demo-self-driving)
    - 探索一个 [纽约市乘车数据集](https://github.com/streamlit/demo-uber-nyc-pickups)
"""
)
```

`1_📈_Plotting_Demo.py`

```python
# coding=utf-8
"""
@IDE：PyCharm
@project: Streamlit_Demo
@Author：Sam Lau
@file： 1_📈_Plotting_Demo.py
@date：2024/7/3 下午3:16
 """
import streamlit as st
import time
import numpy as np

st.set_page_config(page_title="绘图演示", page_icon="📈")

st.markdown("# 绘图演示")
st.sidebar.header("绘图演示")
st.write(
    """这个演示展示了 Streamlit 的绘图和动画组合。我们在一个循环中生成一些随机数大约5秒钟。希望你喜欢！"""
)

progress_bar = st.sidebar.progress(0)
status_text = st.sidebar.empty()
last_rows = np.random.randn(1, 1)
chart = st.line_chart(last_rows)

for i in range(1, 101):
    new_rows = last_rows[-1, :] + np.random.randn(5, 1).cumsum(axis=0)
    status_text.text("完成%i%%" % i)
    chart.add_rows(new_rows)
    progress_bar.progress(i)
    last_rows = new_rows
    time.sleep(0.05)

progress_bar.empty()

# Streamlit 的部件会自动按顺序运行脚本。由于此按钮与任何其他逻辑都没有连接，因此它只会引起简单的重新运行。
st.button("重新运行")
```

`2_🌍_Mapping_Demo.py`

```python
# coding=utf-8
"""
@IDE：PyCharm
@project: Streamlit_Demo
@Author：Sam Lau
@file： 2_🌍_Mapping_Demo.py
@date：2024/7/3 下午3:16
 """
import streamlit as st
import pandas as pd
import pydeck as pdk
from urllib.error import URLError

st.set_page_config(page_title="Mapping Demo", page_icon="🌍")

st.markdown("# Mapping Demo")
st.sidebar.header("Mapping Demo")
st.write(
    """This demo shows how to use
[`st.pydeck_chart`](https://docs.streamlit.io/library/api-reference/charts/st.pydeck_chart)
to display geospatial data."""
)


@st.cache_data
def from_data_file(filename):
    url = (
            "http://raw.githubusercontent.com/streamlit/"
            "example-data/master/hello/v1/%s" % filename
    )
    return pd.read_json(url)


try:
    ALL_LAYERS = {
        "Bike Rentals": pdk.Layer(
            "HexagonLayer",
            data=from_data_file("bike_rental_stats.json"),
            get_position=["lon", "lat"],
            radius=200,
            elevation_scale=4,
            elevation_range=[0, 1000],
            extruded=True,
        ),
        "Bart Stop Exits": pdk.Layer(
            "ScatterplotLayer",
            data=from_data_file("bart_stop_stats.json"),
            get_position=["lon", "lat"],
            get_color=[200, 30, 0, 160],
            get_radius="[exits]",
            radius_scale=0.05,
        ),
        "Bart Stop Names": pdk.Layer(
            "TextLayer",
            data=from_data_file("bart_stop_stats.json"),
            get_position=["lon", "lat"],
            get_text="name",
            get_color=[0, 0, 0, 200],
            get_size=15,
            get_alignment_baseline="'bottom'",
        ),
        "Outbound Flow": pdk.Layer(
            "ArcLayer",
            data=from_data_file("bart_path_stats.json"),
            get_source_position=["lon", "lat"],
            get_target_position=["lon2", "lat2"],
            get_source_color=[200, 30, 0, 160],
            get_target_color=[200, 30, 0, 160],
            auto_highlight=True,
            width_scale=0.0001,
            get_width="outbound",
            width_min_pixels=3,
            width_max_pixels=30,
        ),
    }
    st.sidebar.markdown("### Map Layers")
    selected_layers = [
        layer
        for layer_name, layer in ALL_LAYERS.items()
        if st.sidebar.checkbox(layer_name, True)
    ]
    if selected_layers:
        st.pydeck_chart(
            pdk.Deck(
                map_style="mapbox://styles/mapbox/light-v9",
                initial_view_state={
                    "latitude": 37.76,
                    "longitude": -122.4,
                    "zoom": 11,
                    "pitch": 50,
                },
                layers=selected_layers,
            )
        )
    else:
        st.error("Please choose at least one layer above.")
except URLError as e:
    st.error(
        """
        **This demo requires internet access.**
        Connection error: %s
    """
        % e.reason
    )
```

3_📊_DataFrame_Demo.py

```python
# coding=utf-8
"""
@IDE：PyCharm
@project: Streamlit_Demo
@Author：Sam Lau
@file： 3_📊_DataFrame_Demo.py
@date：2024/7/3 下午3:16
 """

import streamlit as st
import pandas as pd
import altair as alt
from urllib.error import URLError

st.set_page_config(page_title="DataFrame Demo", page_icon="📊")

st.markdown("# DataFrame Demo")
st.sidebar.header("DataFrame Demo")
st.write(
    """This demo shows how to use `st.write` to visualize Pandas DataFrames.
(Data courtesy of the [UN Data Explorer](http://data.un.org/Explorer.aspx).)"""
)


@st.cache_data
def get_UN_data():
    AWS_BUCKET_URL = "http://streamlit-demo-data.s3-us-west-2.amazonaws.com"
    df = pd.read_csv(AWS_BUCKET_URL + "/agri.csv.gz")
    return df.set_index("Region")


try:
    df = get_UN_data()
    countries = st.multiselect(
        "Choose countries", list(df.index), ["China", "United States of America"]
    )
    if not countries:
        st.error("Please select at least one country.")
    else:
        data = df.loc[countries]
        data /= 1000000.0
        st.write("### Gross Agricultural Production ($B)", data.sort_index())

        data = data.T.reset_index()
        data = pd.melt(data, id_vars=["index"]).rename(
            columns={"index": "year", "value": "Gross Agricultural Product ($B)"}
        )
        chart = (
            alt.Chart(data)
            .mark_area(opacity=0.3)
            .encode(
                x="year:T",
                y=alt.Y("Gross Agricultural Product ($B):Q", stack=None),
                color="Region:N",
            )
        )
        st.altair_chart(chart, use_container_width=True)
except URLError as e:
    st.error(
        """
        **This demo requires internet access.**
        Connection error: %s
    """
        % e.reason
    )
```

#### 配置文件

配置文件的位置是 ~/.streamlit/config.toml（windows系统中为：C:\Users\Administrator\.streamlit）

以下是一个config.toml示例：

```toml
[server]
port = 8501
enableCORS = false

[browser]
serverAddress = "localhost"
gatherUsageStats = false

[runner]
magicEnabled = false
```

注意：在config.toml文件中，大小写是敏感的，确保配置文件中的各个部分和参数名的大小写一致。

参数：

1、port：Streamlit应用的端口号，默认为 8501。

2、enableCORS：是否启用跨域资源共享，默认为false。如果需要开放Streamlit应用，在非本机电脑也行访问，则需要设置为true。

3、serverAddress：Streamlit服务器的地址，默认为 "localhost"。

4、gatherUsageStats参数默认是true，表示允许streamlit收集使用统计信息。一般禁用就行。

5、magicEnabled参数的默认值是true，表示启用Streamlit的魔法命令功能。即：任何时候如果Streamlit看到一个变量或常量值， 它就会自动将其使用st.write写入应用。所以可能容易导致网页速度变慢、重复加载数据等等情况。

命令行查看streamlit配置信息：

`streamlit config show`

# 常用组件

1. 标题和文本：
   
   - `st.title('标题')`：添加一个大标题。
   - `st.header('标题')`：添加一个较大的标题。
   - `st.subheader('标题')`：添加一个较小的标题。
   - `st.text('文本')`：添加一段文本。

2. 输入组件：
   
   - `st.button('按钮')`：添加一个按钮。
   
   - `st.checkbox('复选框', value=False)`：添加一个复选框。
   
   - `st.radio('单选框', options, index=0)`：添加一个单选框。
   
   - `st.selectbox('下拉框', options, index=0)`：添加一个下拉框。
   
   - `st.multiselect('多选框', options, default=None)`：添加一个多选框。
   
   - `st.slider('滑块', min_value, max_value, value=None, step=None)`：添加一个滑块。
   
   - `st.text_input('文本输入框', value='', max_chars=None)`：添加一个文本输入框。
   
   - `st.number_input('数字输入框', min_value=None, max_value=None,value=None, step=None)`：添加一个数字输入框。
   
   - `st.text_area('多行文本输入框', value='', max_chars=None)`：添加一个多行文本输入框。
   
   - `st.date_input('日期输入框', value=None, min_value=None, max_value=None)`：添加一个日期输入框。
   
   - `st.time_input('时间输入框', value=None)`：添加一个时间输入框。
   
   - `st.file_uploader('文件上传',type=None,accept_multiple_files=False)`：添加一个文件上传组件。
   
   3.输出组件
   
   - `st.write('文本或对象')`：输出文本或对象。
   
   - `st.markdown('Markdown 格式文本')`：支持 Markdown 格式的文本输出。
   
   - `st.latex('LaTeX 格式文本')`：支持 LaTeX 格式的文本输出。
   
   - `st.code('代码块')`：显示代码块。
   
   - `st.json('JSON 数据')`：显示 JSON 数据。
   
   - `st.dataframe(data)`：显示 Pandas 数据帧。
   
   - `st.table(data)`：显示表格数据。
   
   - `st.image(image, caption=None, use_column_width=False)`：显示图像.
   
   - `st.audio(audio, format='audio/wav')`：播放音频文件。
   
   - `st.video(video, format='video/mp4')`：播放视频文件。
   
   4.绘图组件
   
   - `st.pyplot(fig)`：显示 Matplotlib 图形。
   - `st.plotly_chart(fig)`：显示 Plotly 图形。
   - `st.bokeh_chart(fig)`：显示 Bokeh 图形。
   - `st.altair_chart(fig)`：显示 Altair 图形。

5.布局组件

- `st.sidebar`：创建一个侧边栏。

- `st.expander('标题')`：创建一个可展开的区域。

- 缓存数据：使用 `st.cache` 装饰器可以缓存函数的输出，以提高应用程序的性能。

- 进度条：使用 `st.progress` 组件可以显示任务的进度

- 状态管理：使用 `st.session_state` 可以跨会话管理状态。

- 异步更新：使用 `st.experimental_asyncio` 可以实现异步更新应用程序的功能。
