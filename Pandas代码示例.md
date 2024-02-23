# 抓取网页当中的数据

```python
import pandas as pd

df1 = pd.read_html(io='https://baike.baidu.com/item/%E4%B8%96%E7%95%8C500%E5%BC%BA/640042', header=0)[1]
# 因为该网页有多个表格，pd.read_html()生成的该网页内所有表格的list属性
# 需要用索引来确定需要提取的表格
content = pd.DataFrame(df1)
print(content)
content.to_csv('../data/世界500强.csv',encoding='utf-8', index=False)


df2 = pd.read_html(io='https://baike.baidu.com/item/%E4%B8%96%E7%95%8C500%E5%BC%BA/640042', header=0)[2]
content = pd.DataFrame(df2)
print(content)
content.to_csv('../data/中国500强.csv',encoding='utf-8', index=False)
```

# 数据保存到数据库

```python
import pandas as pd
import requests
from loguru import logger
import sqlite3


idCardData_list = []

idCardData = requests.get('https://cdn.uukit.com/data/idCardData.json').json()

for key,value in idCardData.items():
    # logger.info(key,value)
    # logger.info(f'编码-->>>{key}')
    # logger.info(f"省级行政区-->>>{value['p']}")
    # logger.info(f'地级行政区-->>>{value["a"]}')
    # logger.info(f'县城行政区->>>>{value["d"]}')
    # logger.info(f'备注-->>>{value["i"]}')
    idCardData_list.append({
        '编码':key,
        '省级行政区':value['p'],
        '地级行政区':value['a'],
        '县城行政区':value['d'],
        '备注':value['i']
    })

content = pd.DataFrame(idCardData_list)
# logger.info('正在写入文件中!!!!')
# content.to_csv('../data/身份证归属地查询表.csv', encoding='utf-8', index=False)
# logger.info('保存成功!!')

logger.info('正在保存到数据库!!')
conn = sqlite3.connect('id-card.db')
content.to_sql('idCardData', conn, if_exists='replace', index=False) # 数据保存到idCardData表中
conn.commit()
conn.close()
logger.info('保存成功')
```

# 数据库各种引擎

```python
# from sqlalchemy import create_engine
#
# engine = create_engine("postgresql://scott:tiger@localhost:5432/mydatabase")
#
# engine = create_engine("mysql+mysqldb://scott:tiger@localhost/foo")
#
# engine = create_engine("oracle://scott:tiger@127.0.0.1:1521/sidname")
#
# engine = create_engine("mssql+pyodbc://mydsn")
#
# # sqlite://<nohostname>/<path>
# # where <path> is relative:
# engine = create_engine("sqlite:///foo.db")
#
# # or absolute, starting with a slash:
# engine = create_engine("sqlite:////absolute/path/to/foo.db")
```

# 保存Json格式数据

```python
from datetime import datetime
import requests
from loguru import logger
import time
import pandas as pd
from tqdm import tqdm
import pendulum as pdl

header = {
    'Cookie': 'JSESSIONID=5B2D61919D548A6F3E0C623DF4A769FD',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0'
}

content_list2 = []


def get_allProvince():
    """
    获取全国所有省份的预售点数量
    :return:
    """
    url1 = 'https://kyfw.12306.cn/otn/userCommon/allProvince'
    rep1 = requests.get(url1).json()
    time.sleep(3)
    content_list1 = pd.json_normalize(rep1['data'], errors='ignore')
    return content_list1



def get_agency_sell_ticket(province):
    """
    获取所有省份的代售点信息
    :param province:
    :return:
    """
    url2 = f'https://kyfw.12306.cn/otn/queryAgencySellTicket/query?province={province}&city=&county='
    rep2 = requests.get(url2).json()
    time.sleep(3)
    df = pd.json_normalize(rep2['data']['datas'], errors='ignore')
    content_list2.append(df)


def get_all_sale_time():
    """
    获取全国所有车站的预售时间
    :return:
    """
    url3 = 'https://kyfw.12306.cn/index/otn/index12306/queryAllCacheSaleTime'
    rep = requests.get(url3, headers=header).json()
    time.sleep(3)
    content_list3 = pd.json_normalize(rep['data'], errors='ignore')
    return content_list3


if __name__ == '__main__':
    curr_time1 = datetime.now().strftime('%Y_%m_%d_%H_%M_%S')
    curr_time2 =pdl.now().format("YYYY_MM_DD_HH_mm_ss")
    # content_list3 = get_all_sale_time()
    # content_list.to_excel(f'全国火车站预售时间_{curr_time1}.xlsx',index=False)
    # logger.info(f'请求得到的表格行数与列数->>>>>{content_list3.shape}')

    # content_list1=get_allProvince()
    # content_list1.to_excel(f'全国售票点信息_{curr_time}.xlsx',index=False)
    # logger.info(f'请求得到的表格行数与列数->>>>>{content_list1.shape}')
    df = pd.read_excel('../src/全国售票点信息_2024_01_23_14_38_17.xlsx')
    logger.info(f'正在获取各个省份代售点的信息')
    tqdm.pandas(desc="获取全国火车票代售进度条")
    # df.apply(lambda x: get_agency_sell_ticket(x['chineseName']), axis=1)
    df.progress_apply(lambda x: get_agency_sell_ticket(x['chineseName']), axis=1)
    df = pd.concat(content_list2)

    df.to_excel(f'全国代售点详细信息_{curr_time}.xlsx', sheet_name='代售点', index=False)
    logger.info('保存成功！！！！')
    logger.info(f'请求得到的表格行数与列数->>>>>{df.shape}')
```

# 解析Json数据

```python
import pandas as pd
import requests

# 解析一般Json对象
a_dict = {
    'school': 'ABC primary school',
    'location': 'London',
    'ranking': 2
}
pd.json_normalize(a_dict) 


# 解析一个有多层数据的Json对象列表
json_obj = {
    'school': 'ABC primary school',
    'location': 'London',
    'ranking': 2,
    'info': {
        'president': 'John Kasich',
        'contacts': {
            'email': {
                'admission': 'admission@abc.com',
                'general': 'info@abc.com'
            },
            'tel': '123456789',
        }
    }
}
pd.json_normalize(json_obj, max_level=1)   



json_obj = {
    'school': 'ABC primary school',
    'location': 'London',
    'ranking': 2,
    'info': {
        'president': 'John Kasich',
        'contacts': {
            'email': {
                'admission': 'admission@abc.com',
                'general': 'info@abc.com'
            },
            'tel': '123456789',
        }
    }
}
pd.json_normalize(json_obj, max_level=2)   



# 解析一个带有嵌套列表的Json
json_list = [
    {
        'class': 'Year 1',
        'student count': 20,
        'room': 'Yellow',
        'info': {
            'teachers': {
                'math': 'Rick Scott',
                'physics': 'Elon Mask'
            }
        }
    },
    {
        'class': 'Year 2',
        'student count': 25,
        'room': 'Blue',
        'info': {
            'teachers': {
                'math': 'Alan Turing',
                'physics': 'Albert Einstein'
            }
        }
    }
]
pd.json_normalize(json_list)    



json_list = [
    {
        'class': 'Year 1',
        'student count': 20,
        'room': 'Yellow',
        'info': {
            'teachers': {
                'math': 'Rick Scott',
                'physics': 'Elon Mask'
            }
        }
    },
    {
        'class': 'Year 2',
        'student count': 25,
        'room': 'Blue',
        'info': {
            'teachers': {
                'math': 'Alan Turing',
                'physics': 'Albert Einstein'
            }
        }
    }
]
pd.json_normalize(json_list, max_level=2)


json_list = [
    {
        'class': 'Year 1',
        'student count': 20,
        'room': 'Yellow',
        'info': {
            'teachers': {
                'math': 'Rick Scott',
                'physics': 'Elon Mask'
            }
        }
    },
    {
        'class': 'Year 2',
        'student count': 25,
        'room': 'Blue',
        'info': {
            'teachers': {
                'math': 'Alan Turing',
                'physics': 'Albert Einstein'
            }
        }
    }
]
pd.json_normalize(json_list, max_level=3)



son_obj = {
    'school': 'ABC primary school',
    'location': 'London',
    'ranking': 2,
    'info': {
        'president': 'John Kasich',
        'contacts': {
            'email': {
                'admission': 'admission@abc.com',
                'general': 'info@abc.com'
            },
            'tel': '123456789',
        }
    },
    'students': [
        {'name': 'Tom'},
        {'name': 'James'},
        {'name': 'Jacqueline'}
    ],
}
pd.json_normalize(json_obj)


json_obj = {
    'school': 'ABC primary school',
    'location': 'London',
    'ranking': 2,
    'info': {
        'president': 'John Kasich',
        'contacts': {
            'email': {
                'admission': 'admission@abc.com',
                'general': 'info@abc.com'
            },
            'tel': '123456789',
        }
    },
    'students': [
        {'name': 'Tom'},
        {'name': 'James'},
        {'name': 'Jacqueline'}
    ],
}
pd.json_normalize(json_obj, record_path='students')

pd.json_normalize(json_obj, record_path='students',
                  meta=['school', 'location', ['info', 'contacts', 'tel'], ['info', 'contacts', 'email', 'general']])   





# 当Key不存在时如何忽略系统报错
data = [
    {
        'class': 'Year 1',
        'student count': 20,
        'room': 'Yellow',
        'info': {
            'teachers': {
                'math': 'Rick Scott',
                'physics': 'Elon Mask',
            }
        },
        'students': [
            {'name': 'Tom', 'sex': 'M'},
            {'name': 'James', 'sex': 'M'},
        ]
    },
    {
        'class': 'Year 2',
        'student count': 25,
        'room': 'Blue',
        'info': {
            'teachers': {
                # no math teacher
                'physics': 'Albert Einstein'
            }
        },
        'students': [
            {'name': 'Tony', 'sex': 'M'},
            {'name': 'Jacqueline', 'sex': 'F'},
        ]
    },
]
pd.json_normalize(
    data,
    record_path=['students'],
    meta=['class', 'room', ['info', 'teachers', 'math']]
)


pd.json_normalize(
    data,
    record_path=['students'],
    meta=['class', 'room', ['info', 'teachers', 'math']],
    errors='ignore'
)  



# 使用sep参数为嵌套Json的Key设置分隔符
json_obj = {
    'school': 'ABC primary school',
    'location': 'London',
    'ranking': 2,
    'info': {
        'president': 'John Kasich',
        'contacts': {
            'email': {
                'admission': 'admission@abc.com',
                'general': 'info@abc.com'
            },
            'tel': '123456789',
        }
    }
}
pd.json_normalize(json_obj, sep='->')   



# 为嵌套列表数据和元数据添加前缀
json_obj = {
    'school': 'ABC primary school',
    'location': 'London',
    'ranking': 2,
    'info': {
        'president': 'John Kasich',
        'contacts': {
            'email': {
                'admission': 'admission@abc.com',
                'general': 'info@abc.com'
            },
            'tel': '123456789',
        }
    },
    'students': [
        {'name': 'Tom'},
        {'name': 'James'},
        {'name': 'Jacqueline'}
    ],
}

# 为嵌套列表数据添加students->前缀，为元数据添加meta->前缀，将嵌套key之间的分隔符修改为->
pd.json_normalize(json_obj, record_path='students',
                  meta=['school', 'location', ['info', 'contacts', 'tel'], ['info', 'contacts', 'email', 'general']],
                  record_prefix='students->',
                  meta_prefix='meta->',
                  sep='->') 



# 通过URL获取Json数据并进行解析

# 通过天气API，获取广州近7天的天气
url = 'https://tianqiapi.com/free/week'
# 传入url，并设定好相应的params
r = requests.get(url, params={"appid": "59257444", "appsecret": "uULlTGV9 ", 'city': '广州'})
# 将获取到的值转换为json对象
result = r.json()
result


df = pd.json_normalize(result, meta=['city', 'cityid', 'update_time'], record_path=['data'])
df = df[['cityid','city','date','wea_img','tem_day','tem_night','win','win_speed','update_time']]
df


df = pd.json_normalize(result, record_path=['data'])
df


# 解析带有多个嵌套列表的Json
json_obj = {
    'school': 'ABC primary school',
    'location': 'shenzhen',
    'ranking': 2,
    'info': {
        'president': 'John Kasich',
        'contacts': {
            'email': {
                'admission': 'admission@abc.com',
                'general': 'info@abc.com'
            },
            'tel': '123456789',
        }
    },
    'students': [
        {'name': 'Tom'},
        {'name': 'James'},
        {'name': 'Jacqueline'}
    ],
    # 添加university嵌套列表，加上students,该JSON对象中就有2个嵌套列表了
    'university': [
        {'university_name': 'HongKong university shenzhen'},
        {'university_name': 'zhongshan university shenzhen'},
        {'university_name': 'shenzhen university'}
    ],
}
# 尝试在record_path中写上两个嵌套列表的名字，即record_path = ['students', 'university],结果无济于事
# 于是决定分两次进行解析，分别将record_path设置成为university和students,最终将2个结果合并起来
df1 = pd.json_normalize(json_obj, record_path=['university'],
                        meta=['school', 'location', ['info', 'contacts', 'tel'],
                              ['info', 'contacts', 'email', 'general']],
                        record_prefix='university->',
                        meta_prefix='meta->',
                        sep='->')
df2 = pd.json_normalize(json_obj, record_path=['students'],
                        meta=['school', 'location', ['info', 'contacts', 'tel'],
                              ['info', 'contacts', 'email', 'general']],
                        record_prefix='students->',
                        meta_prefix='meta->',
                        sep='->')
# 将两个结果根据index关联起来并去除重复列
# df1.merge(df2, how='left', left_index=True, right_index=True, suffixes=['->', '->']).T.drop_duplicates().T
```

# 例子

```python
json_obj = {
    "reason": "查询成功!",
    "result": {
        "city": "苏州",
        "realtime": {
            "temperature": "16",
            "humidity": "83",
            "info": "阴",
            "wid": "02",
            "direct": "东北风",
            "power": "4级",
            "aqi": "115"
        },
        "future": [
            {
                "date": "2023-05-22",
                "temperature": "13/21℃",
                "weather": "小雨转多云",
                "wid": {
                    "day": "07",
                    "night": "01"
                },
                "direct": "北风转西北风"
            },
            {
                "date": "2023-05-23",
                "temperature": "16/26℃",
                "weather": "多云转小雨",
                "wid": {
                    "day": "01",
                    "night": "07"
                },
                "direct": "东风转东南风"
            },
            {
                "date": "2023-05-24",
                "temperature": "17/22℃",
                "weather": "小雨转多云",
                "wid": {
                    "day": "07",
                    "night": "01"
                },
                "direct": "东南风"
            },
            {
                "date": "2023-05-25",
                "temperature": "21/30℃",
                "weather": "多云",
                "wid": {
                    "day": "01",
                    "night": "01"
                },
                "direct": "东南风"
            },
            {
                "date": "2023-05-26",
                "temperature": "22/30℃",
                "weather": "多云",
                "wid": {
                    "day": "01",
                    "night": "01"
                },
                "direct": "南风转东南风"
            }
        ]
    },
    "error_code": 0
}   


# 获取city的值，如果city的值为一级，则可以直接获取['city']，如果是在第二级,则可以
# [‘result’,'city']获取，record_path可以解析数据结构相同的值'result'为第一级
# ‘future’为第二级列表的值，取值方法类似于字典取值xxx.yyy
df1 = pd.json_normalize(json_obj,meta=[['result','city']],record_path=['result','future'])

# 字段重新排序显示
df2 = df1[['result.city','date','temperature','weather','direct','wid.day','wid.night']]

# 修改列名
df2.rename(columns={'result.city':'city','wid.day':'day','wid.night':'night'},inplace=True)
```














