Dataframe示例代码

```python
# coding=utf-8
"""
@IDE：PyCharm
@project: Streamlit_Demo
@Author：Sam Lau
@file： example_dataframe.py
@date：2024/7/3 下午4:54
 """
import random
from datetime import datetime, date, time

import streamlit as st
import pandas as pd
import numpy as np

df = pd.DataFrame(
    np.random.randn(50, 20),
    columns=('col %d' % i for i in range(20)))

st.dataframe(df)
st.divider()
st.dataframe(df.style.highlight_max(axis=0))

st.divider()

df = pd.DataFrame(
    {
        "name": ["Roadmap", "Extras", "Issues"],
        "url": ["https://roadmap.streamlit.app", "https://extras.streamlit.app", "https://issues.streamlit.app"],
        "stars": [random.randint(0, 1000) for _ in range(3)],
        "views_history": [[random.randint(0, 5000) for _ in range(30)] for _ in range(3)],
    }
)

# - "name" 列被重命名为 "App name"；
# - "stars" 列被定义成了一个 st.column_config.NumberColumn 对象，可以显示带有 GitHub
# 星数的标题，并指定了格式为整数 "%d ⭐"；
# - "url" 列被定义成了一个 st.column_config.LinkColumn 对象，将单元格的内容作为链接展示；
# - "views_history" 列被定义成了一个 st.column_config.LineChartColumn对象，生成了一个折线图，显示过去 30 天的访问历史，并指定了 Y 轴的最小值和最大值。
# hide_index=True，将索引隐藏起来。

st.dataframe(
    df,
    column_config={
        "name": "App name",
        "stars": st.column_config.NumberColumn(
            "Github Stars",
            help="Number of stars on GitHub",
            format="%d ⭐",
        ),
        "url": st.column_config.LinkColumn("App URL"),
        "views_history": st.column_config.LineChartColumn(
            "Views (past 30 days)", y_min=0, y_max=5000
        ),
    },
    hide_index=True,
)

st.divider()


# 使用缓存加载数据框，这样只会加载一次
@st.cache_data
def load_data():
    return pd.DataFrame(
        {
            "第一列": [1, 2, 3, 4],
            "第二列": [10, 20, 30, 40],
        }
    )


# 使用会话状态变量存储用于调整数据框尺寸的布尔值
st.checkbox("使用容器宽度", value=False, key="use_container_width")

df = load_data()

# 根据复选框的值，显示数据框并允许用户根据容器宽度调整数据框尺寸
st.dataframe(df, use_container_width=st.session_state.use_container_width)

st.divider()

df = pd.DataFrame(
    [
        {"command": "st.selectbox", "rating": 4, "is_widget": True},
        {"command": "st.balloons", "rating": 5, "is_widget": False},
        {"command": "st.time_input", "rating": 3, "is_widget": True},
    ]
)
edited_df = st.data_editor(df)

favorite_command = edited_df.loc[edited_df["rating"].idxmax()]["command"]
st.markdown(f"Your favorite command is **{favorite_command}** 🎈")

st.divider()

df = pd.DataFrame(
    [
        {"command": "st.selectbox", "rating": 4, "is_widget": True},
        {"command": "st.balloons", "rating": 5, "is_widget": False},
        {"command": "st.time_input", "rating": 3, "is_widget": True},
    ]
)
# num_rows 设置为 "dynamic"，让用户添加和删除行
edited_df = st.data_editor(df, num_rows="dynamic")

favorite_command = edited_df.loc[edited_df["rating"].idxmax()]["command"]
st.markdown(f"Your favorite command is **{favorite_command}** 🎈")

st.divider()

# - column_config：通过指定新的列名和自定义控件的方式，我们将 "command" 列的名称改为 "Streamlit
# Command"，将 "rating" 列的控件类型改为数字输入框，并添加帮助文本、最小值、最大值、步长和格式化选项。
# - disabled：我们禁用了 "command" 和 "is_widget" 列的编辑功能，使它们成为只读。
# - hide_index：我们隐藏了索引列，只展示了数据内容。


df = pd.DataFrame(
    [
        {"command": "st.selectbox", "rating": 4, "is_widget": True},
        {"command": "st.balloons", "rating": 5, "is_widget": False},
        {"command": "st.time_input", "rating": 3, "is_widget": True},
    ]
)
edited_df = st.data_editor(
    df,
    column_config={
        "command": "Streamlit Command",
        "rating": st.column_config.NumberColumn(
            "Your rating",
            help="How much do you like this command (1-5)?",
            min_value=1,
            max_value=5,
            step=1,
            format="%d ⭐",
        ),
        "is_widget": "Widget ?",
    },
    disabled=["command", "is_widget"],
    hide_index=True,
)

favorite_command = edited_df.loc[edited_df["rating"].idxmax()]["command"]
st.markdown(f"Your favorite command is **{favorite_command}** 🎈")

st.divider()

# 使用 st.column_config.Column 定制数据编辑器的列

# title：设置列的标题为 "Streamlit Widgets"。
# help：提供帮助文本，以解释该列是关于 Streamlit 小部件命令的。
# width：指定列的宽度为 "medium"，对于长文本或宽列，可以使用不同的宽度选项。
# required：将该列标记为必填项，使用户必须填写该列的值。

data_df = pd.DataFrame(
    {
        "widgets": ["st.selectbox", "st.number_input", "st.text_area", "st.button"],
    }
)

st.data_editor(
    data_df,
    column_config={
        "widgets": st.column_config.Column(
            "Streamlit Widgets",
            help="Streamlit **widget** commands 🎈",
            width="medium",
            required=True,
        )
    },
    hide_index=True,
    num_rows="dynamic",
)

# 使用 st.column_config.TextColumn 定制数据编辑器的文本列

# title：设置列的标题为 "Widgets"。
# help：提供帮助文本，以解释该列是关于 Streamlit 小部件命令的。
# default：设置默认值为 "st."。
# max_chars：限制输入文本的最大字符数为 50。
# validate：使用正则表达式进行验证，确保值符合 "st." 以及小写字母和下划线的规则。

st.divider()

data_df = pd.DataFrame(
    {
        "widgets": ["st.selectbox", "st.number_input", "st.text_area", "st.button"],
    }
)

st.data_editor(
    data_df,
    column_config={
        "widgets": st.column_config.TextColumn(
            "Widgets",
            help="Streamlit **widget** commands 🎈",
            default="st.",
            max_chars=50,
            validate="^st\.[a-z_]+$",
        )
    },
    hide_index=True,
)
st.divider()

# 使用 st.column_config.NumberColumn 定制数据编辑器的数字列

# title：设置列的标题为 "Price (in USD)"。
# help：提供帮助文本，说明该列存储的是产品的美元价格。
# min_value：设置最小值为 0，限制输入值不能小于 0。
# max_value：设置最大值为 1000，限制输入值不能大于 1000。
# step：设置步长为 1，控制数字输入的增减间隔。
# format：我们使用 "$%d" 的格式来显示价格，让输入值自动前面添加美元符号。


data_df = pd.DataFrame(
    {
        "price": [20, 950, 250, 500],
    }
)

st.data_editor(
    data_df,
    column_config={
        "price": st.column_config.NumberColumn(
            "Price (in USD)",
            help="The price of the product in USD",
            min_value=0,
            max_value=1000,
            step=1,
            format="$%d",
        )
    },
    hide_index=True,
)

st.divider()

# 使用 st.column_config.CheckboxColumn 定制数据编辑器的复选框列

# title：设置列的标题为 "Your favorite?"。
# help：提供帮助文本，以解释该列是关于用户对小部件的喜好情况的选择复选框。
# default：设置默认值为 False，即未选中复选框。
# widgets" 列添加到 disabled 参数中来禁用了该列的编辑

data_df = pd.DataFrame(
    {
        "widgets": ["st.selectbox", "st.number_input", "st.text_area", "st.button"],
        "favorite": [True, False, False, True],
    }
)

st.data_editor(
    data_df,
    column_config={
        "favorite": st.column_config.CheckboxColumn(
            "Your favorite?",
            help="Select your **favorite** widgets",
            default=False,
        )
    },
    disabled=["widgets"],
    hide_index=True,
)

st.divider()

# 使用 st.column_config.SelectboxColumn 定制数据编辑器的下拉框列

# title：设置列的标题为 "App Category"。
# help：提供帮助文本，解释该列是关于应用分类的下拉框。
# width：设置下拉框的宽度为 "medium"，使其具有中等宽度。
# options：设置下拉框的选项为 ["📊 Data Exploration", "📈 Data Visualization","🤖 LLM"]，即用户可以从这些选项中选择。


data_df = pd.DataFrame(
    {
        "category": [
            "📊 Data Exploration",
            "📈 Data Visualization",
            "🤖 LLM",
            "📊 Data Exploration",
        ],
    }
)

st.data_editor(
    data_df,
    column_config={
        "category": st.column_config.SelectboxColumn(
            "App Category",
            help="The category of the app",
            width="medium",
            options=[
                "📊 Data Exploration",
                "📈 Data Visualization",
                "🤖 LLM",
            ],
        )
    },
    hide_index=True,
)

st.divider()

# 使用 st.column_config.DatetimeColumn 定制数据编辑器的日期时间列

# title：设置列的标题为 "Appointment"。
# min_value：设置最小日期时间为 datetime(2023, 6, 1)，即2023年6月1日之后的日期时间可选择。
# max_value：设置最大日期时间为 datetime(2025, 1, 1)，即2025年1月1日之前的日期时间可选择。
# format：设置日期时间的显示格式为 "D MMM YYYY, h:mm a"，例如 "5 Feb 2024, 12:30 PM"。
# step：设置步长为 60 分钟，即每次改变日期时间时以 60 分钟为单位递增或递减。


data_df = pd.DataFrame(
    {
        "appointment": [
            datetime(2024, 2, 5, 12, 30),
            datetime(2023, 11, 10, 18, 0),
            datetime(2024, 3, 11, 20, 10),
            datetime(2023, 9, 12, 3, 0),
        ]
    }
)

st.data_editor(
    data_df,
    column_config={
        "appointment": st.column_config.DatetimeColumn(
            "Appointment",
            min_value=datetime(2023, 6, 1),
            max_value=datetime(2025, 1, 1),
            format="D MMM YYYY, h:mm a",
            step=60,
        ),
    },
    hide_index=True,
)
st.divider()

# 使用 st.column_config.DateColumn 定制数据编辑器的日期列

# title：设置列的标题为 "Birthday"。
# min_value：设置最小日期为 date(1900, 1, 1)，即1900年1月1日之后的日期可选择。
# max_value：设置最大日期为 date(2005, 1, 1)，即2005年1月1日之前的日期可选择。
# format：设置日期的显示格式为 "DD.MM.YYYY"，例如 "01.01.1980"。
# step：设置步长为 1 天，即每次改变日期时以 1 天为单位递增或递减。


data_df = pd.DataFrame(
    {
        "birthday": [
            date(1980, 1, 1),
            date(1990, 5, 3),
            date(1974, 5, 19),
            date(2001, 8, 17),
        ]
    }
)

st.data_editor(
    data_df,
    column_config={
        "birthday": st.column_config.DateColumn(
            "Birthday",
            min_value=date(1900, 1, 1),
            max_value=date(2005, 1, 1),
            format="DD.MM.YYYY",
            step=1,
        ),
    },
    hide_index=True,
)
st.divider()

# 使用 st.column_config.TimeColumn 定制数据编辑器的时间列

# title：设置列的标题为 "Appointment"。
# min_value：设置最小时间为 time(8, 0, 0)，即每天从早上8点之后的时间可选择。
# max_value：设置最大时间为 time(19, 0, 0)，即每天到晚上7点之前的时间可选择。
# format：设置时间的显示格式为 "hh:mm a"，例如 "12:30 PM"。
# step：设置步长为 60 分钟，即每次改变时间时以 60 分钟为单位递增或递减。


data_df = pd.DataFrame(
    {
        "appointment": [
            time(12, 30),
            time(18, 0),
            time(9, 10),
            time(16, 25),
        ]
    }
)

st.data_editor(
    data_df,
    column_config={
        "appointment": st.column_config.TimeColumn(
            "Appointment",
            min_value=time(8, 0, 0),
            max_value=time(19, 0, 0),
            format="hh:mm a",
            step=60,
        ),
    },
    hide_index=True,
)
st.divider()

# 使用 st.column_config.ListColumn 定制数据编辑器的列表列
#
# title：设置列的标题为 "Sales (last 6 months)"。
# help：提供对该列的帮助信息，为 "The sales volume in the last 6 months"。
# width：设置列的宽度为 "medium"。

data_df = pd.DataFrame(
    {
        "sales": [
            [0, 4, 26, 80, 100, 40],
            [80, 20, 80, 35, 40, 100],
            [10, 20, 80, 80, 70, 0],
            [10, 100, 20, 100, 30, 100],
        ],
    }
)

st.data_editor(
    data_df,
    column_config={
        "sales": st.column_config.ListColumn(
            "Sales (last 6 months)",
            help="The sales volume in the last 6 months",
            width="medium",
        ),
    },
    hide_index=True,
)

st.divider()

# 使用 st.column_config.LinkColumn 定制数据编辑器的链接列

# title：设置列的标题为 "Trending apps"。
# help：提供对该列的帮助信息，为 "The top trending Streamlit apps"。
# validate：设置正则表达式模式，用于验证链接的格式，该模式为
# "^https://[a-z]+.streamlit.app$"，表示链接必须以 "https://" 开头，以
# ".streamlit.app" 结尾，并且中间部分只能包含小写字母。
# max_chars：设置链接显示的最大字符数为 100。


data_df = pd.DataFrame(
    {
        "apps": [
            "https://roadmap.streamlit.app",
            "https://extras.streamlit.app",
            "https://issues.streamlit.app",
            "https://30days.streamlit.app",
        ],
    }
)

st.data_editor(
    data_df,
    column_config={
        "apps": st.column_config.LinkColumn(
            "Trending apps",
            help="The top trending Streamlit apps",
            validate="^https://[a-z]+\.streamlit\.app$",
            max_chars=100,
        )
    },
    hide_index=True,
)
st.divider()

#  使用 st.column_config.ImageColumn 定制数据编辑器的图片列

# title：设置列的标题为 "Preview Image"。
# help：提供对该列的帮助信息，为 "Streamlit app preview screenshots"。

data_df = pd.DataFrame(
    {
        "apps": [
            "https://storage.googleapis.com/s4a-prod-share-preview/default/st_app_screenshot_image/5435b8cb-6c6c-490b"
            "-9608-799b543655d3/Home_Page.png",
            "https://storage.googleapis.com/s4a-prod-share-preview/default/st_app_screenshot_image/ef9a7627-13f2-47e5"
            "-8f65-3f69bb38a5c2/Home_Page.png",
            "https://storage.googleapis.com/s4a-prod-share-preview/default/st_app_screenshot_image/31b99099-8eae-4ff8"
            "-aa89-042895ed3843/Home_Page.png",
            "https://storage.googleapis.com/s4a-prod-share-preview/default/st_app_screenshot_image/6a399b09-241e-4ae7"
            "-a31f-7640dc1d181e/Home_Page.png",
        ],
    }
)

st.data_editor(
    data_df,
    column_config={
        "apps": st.column_config.ImageColumn(
            "Preview Image", help="Streamlit app preview screenshots"
        )
    },
    hide_index=True,
)
st.divider()

# 使用 st.column_config.LineChartColumn 定制数据编辑器的折线图列

# title：设置列的标题为 "Sales (last 6 months)"。
# width：设置折线图的宽度为 "medium"，可以根据需求设置合适的宽度。
# help：提供对该列的帮助信息，为 "The sales volume in the last 6 months"。
# y_min：设置折线图的 Y 轴最小值为 0。
# y_max：设置折线图的 Y 轴最大值为 100


data_df = pd.DataFrame(
    {
        "sales": [
            [0, 4, 26, 80, 100, 40],
            [80, 20, 80, 35, 40, 100],
            [10, 20, 80, 80, 70, 0],
            [10, 100, 20, 100, 30, 100],
        ],
    }
)

st.data_editor(
    data_df,
    column_config={
        "sales": st.column_config.LineChartColumn(
            "Sales (last 6 months)",
            width="medium",
            help="The sales volume in the last 6 months",
            y_min=0,
            y_max=100,
        ),
    },
    hide_index=True,
)
st.divider()
# 使用 st.column_config.BarChartColumn 定制数据编辑器的柱状图列

# title：设置列的标题为 "Sales (last 6 months)"。
# help：提供对该列的帮助信息，为 "The sales volume in the last 6 months"。
# y_min：设置柱状图的 Y 轴最小值为 0。
# y_max：设置柱状图的 Y 轴最大值为 100。


data_df = pd.DataFrame(
    {
        "sales": [
            [0, 4, 26, 80, 100, 40],
            [80, 20, 80, 35, 40, 100],
            [10, 20, 80, 80, 70, 0],
            [10, 100, 20, 100, 30, 100],
        ],
    }
)

st.data_editor(
    data_df,
    column_config={
        "sales": st.column_config.BarChartColumn(
            "Sales (last 6 months)",
            help="The sales volume in the last 6 months",
            y_min=0,
            y_max=100,
        ),
    },
    hide_index=True,
)

# 使用 st.column_config.ProgressColumn 定制数据编辑器的进度条列

# title：设置列的标题为 "Sales volume"。
# help：提供对该列的帮助信息，为 "The sales volume in USD"。
# format：设置数值的格式为 "$%f"，这样数值会以美元符号开头并保留两位小数。
# min_value：设置进度条的最小值为 0。
# max_value：设置进度条的最大值为 1000。


data_df = pd.DataFrame(
    {
        "sales": [200, 550, 1000, 80],
    }
)

st.data_editor(
    data_df,
    column_config={
        "sales": st.column_config.ProgressColumn(
            "Sales volume",
            help="The sales volume in USD",
            format="$%f",
            min_value=0,
            max_value=1000,
        ),
    },
    hide_index=True,
)
st.divider()

# 使用 st.table 展示数据框.

df = pd.DataFrame(
    np.random.randn(10, 5),
    columns=('col %d' % i for i in range(5)))

st.table(df)

st.divider()

# 使用 st.columns 和 st.metric 创建单个指标数据显示

# label：表示指标的名称或标签，例如 "Temperature"。
# value：表示指标的值，例如 "70 °F"。
# delta：表示指标的增量或变化量，例如 "1.2 °F"。

st.metric(label="Temperature", value="70 °F", delta="1.2 °F")

st.divider()

# 使用 st.columns 和 st.metric 创建多个指标数据显示

# label：指标的名称或标签，例如 "Temperature"、"Wind" 和 "Humidity"。
# value：指标的值，例如 "70 °F"、"9 mph" 和 "86%"。
# delta：指标的增量或变化量，例如 "1.2 °F"、"-8%" 和 "4%"。


col1, col2, col3 = st.columns(3)
col1.metric("Temperature", "70 °F", "1.2 °F")
col2.metric("Wind", "9 mph", "-8%")
col3.metric("Humidity", "86%", "4%")

st.divider()
#  控制增量指示器的颜色和显示

st.metric(label="Gas price", value=4, delta=-0.5,
          delta_color="inverse")

st.metric(label="Active developers", value=123, delta=123,
          delta_color="off")

# 使用 st.json 展示 JSON 数据


st.json({
    'foo': 'bar',
    'baz': 'boz',
    'stuff': [
        'stuff 1',
        'stuff 2',
        'stuff 3',
        'stuff 5',
    ],
})
```
