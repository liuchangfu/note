# coding=utf-8
"""
@IDE：PyCharm
@project: feapder
@Author：Liuchangfu
@file： ex_pd.py
@date：2023/4/23 15:58
 """
import pandas as pd

data = [{'date': None, 'monthly_sales': None, 'share_manufacturers': None, 'sales_ranking_month': None,
         'maker_ranking': None, 'ranking_compact_cars': None},
        {'date': '2023-03', 'monthly_sales': '22855', 'share_manufacturers': '58.24%', 'sales_ranking_month': '9',
         'maker_ranking': '1', 'ranking_compact_cars': '4'},
        {'date': '2023-02', 'monthly_sales': '26102', 'share_manufacturers': '52.67%', 'sales_ranking_month': '4',
         'maker_ranking': '1', 'ranking_compact_cars': '2'},
        {'date': '2023-01', 'monthly_sales': '23507', 'share_manufacturers': '58.41%', 'sales_ranking_month': '3',
         'maker_ranking': '1', 'ranking_compact_cars': '2'},
        {'date': '2022-12', 'monthly_sales': '24502', 'share_manufacturers': '43.16%', 'sales_ranking_month': '11',
         'maker_ranking': '1', 'ranking_compact_cars': '3'},
        {'date': '2022-11', 'monthly_sales': '24929', 'share_manufacturers': '57.76%', 'sales_ranking_month': '10',
         'maker_ranking': '1', 'ranking_compact_cars': '3'},
        {'date': '2022-10', 'monthly_sales': '40273', 'share_manufacturers': '55.95%', 'sales_ranking_month': '4',
         'maker_ranking': '1', 'ranking_compact_cars': '1'},
        {'date': '2022-09', 'monthly_sales': '34936', 'share_manufacturers': '49.23%', 'sales_ranking_month': '6',
         'maker_ranking': '1', 'ranking_compact_cars': '3'},
        {'date': '2022-08', 'monthly_sales': '39773', 'share_manufacturers': '54.29%', 'sales_ranking_month': '7',
         'maker_ranking': '1', 'ranking_compact_cars': '2'},
        {'date': '2022-07', 'monthly_sales': '43392', 'share_manufacturers': '53.94%', 'sales_ranking_month': '2',
         'maker_ranking': '1', 'ranking_compact_cars': '1'},
        {'date': '2022-06', 'monthly_sales': '45312', 'share_manufacturers': '56.95%', 'sales_ranking_month': '4',
         'maker_ranking': '1', 'ranking_compact_cars': '2'},
        {'date': '2022-05', 'monthly_sales': '33030', 'share_manufacturers': '62.88%', 'sales_ranking_month': '2',
         'maker_ranking': '1', 'ranking_compact_cars': '1'},
        {'date': '2022-04', 'monthly_sales': '25493', 'share_manufacturers': '67.74%', 'sales_ranking_month': '2',
         'maker_ranking': '1', 'ranking_compact_cars': '1'},
        {'date': '2022-03', 'monthly_sales': '28557', 'share_manufacturers': '50.89%', 'sales_ranking_month': '3',
         'maker_ranking': '1', 'ranking_compact_cars': '1'},
        {'date': '2022-02', 'monthly_sales': '34705', 'share_manufacturers': '46.70%', 'sales_ranking_month': '1',
         'maker_ranking': '1', 'ranking_compact_cars': '1'},
        {'date': '2022-01', 'monthly_sales': '61170', 'share_manufacturers': '55.11%', 'sales_ranking_month': '1',
         'maker_ranking': '1', 'ranking_compact_cars': '1'},
        {'date': '2021-12', 'monthly_sales': '46728', 'share_manufacturers': '52.90%', 'sales_ranking_month': '2',
         'maker_ranking': '1', 'ranking_compact_cars': '1'},
        {'date': '2021-11', 'monthly_sales': '45399', 'share_manufacturers': '49.15%', 'sales_ranking_month': '3',
         'maker_ranking': '1', 'ranking_compact_cars': '2'},
        {'date': '2021-10', 'monthly_sales': '39806', 'share_manufacturers': '50.41%', 'sales_ranking_month': '1',
         'maker_ranking': '1', 'ranking_compact_cars': '1'},
        {'date': '2021-09', 'monthly_sales': '34111', 'share_manufacturers': '45.91%', 'sales_ranking_month': '3',
         'maker_ranking': '1', 'ranking_compact_cars': '2'},
        {'date': '2021-08', 'monthly_sales': '40876', 'share_manufacturers': '50.68%', 'sales_ranking_month': '2',
         'maker_ranking': '1', 'ranking_compact_cars': '1'},
        {'date': '2021-07', 'monthly_sales': '37067', 'share_manufacturers': '49.55%', 'sales_ranking_month': '1',
         'maker_ranking': '1', 'ranking_compact_cars': '1'},
        {'date': '2021-06', 'monthly_sales': '47283', 'share_manufacturers': '61.34%', 'sales_ranking_month': '1',
         'maker_ranking': '1', 'ranking_compact_cars': '1'},
        {'date': '2021-05', 'monthly_sales': '42062', 'share_manufacturers': '56.95%', 'sales_ranking_month': '1',
         'maker_ranking': '1', 'ranking_compact_cars': '1'},
        {'date': '2021-04', 'monthly_sales': '42172', 'share_manufacturers': '52.88%', 'sales_ranking_month': '1',
         'maker_ranking': '1', 'ranking_compact_cars': '1'},
        {'date': '2021-03', 'monthly_sales': '40014', 'share_manufacturers': '55.01%', 'sales_ranking_month': '2',
         'maker_ranking': '1', 'ranking_compact_cars': '2'},
        {'date': '2021-02', 'monthly_sales': '26655', 'share_manufacturers': '52.28%', 'sales_ranking_month': '2',
         'maker_ranking': '1', 'ranking_compact_cars': '1'},
        {'date': '2021-01', 'monthly_sales': '57977', 'share_manufacturers': '53.55%', 'sales_ranking_month': '1',
         'maker_ranking': '1', 'ranking_compact_cars': '1'},
        {'date': '2020-12', 'monthly_sales': '62339', 'share_manufacturers': '51.15%', 'sales_ranking_month': '1',
         'maker_ranking': '1', 'ranking_compact_cars': '1'},
        {'date': '2020-11', 'monthly_sales': '54470', 'share_manufacturers': '46.39%', 'sales_ranking_month': '2',
         'maker_ranking': '1', 'ranking_compact_cars': '1'},
        {'date': '2020-10', 'monthly_sales': '56201', 'share_manufacturers': '50.86%', 'sales_ranking_month': '1',
         'maker_ranking': '1', 'ranking_compact_cars': '1'},
        {'date': '2020-09', 'monthly_sales': '57525', 'share_manufacturers': '52.05%', 'sales_ranking_month': '1',
         'maker_ranking': '1', 'ranking_compact_cars': '1'},
        {'date': '2020-08', 'monthly_sales': '55684', 'share_manufacturers': '54.65%', 'sales_ranking_month': '1',
         'maker_ranking': '1', 'ranking_compact_cars': '1'},
        {'date': '2020-07', 'monthly_sales': '44236', 'share_manufacturers': '47.17%', 'sales_ranking_month': '1',
         'maker_ranking': '1', 'ranking_compact_cars': '1'},
        {'date': '2020-06', 'monthly_sales': '53761', 'share_manufacturers': '50.45%', 'sales_ranking_month': '1',
         'maker_ranking': '1', 'ranking_compact_cars': '1'},
        {'date': '2020-05', 'monthly_sales': '45283', 'share_manufacturers': '45.84%', 'sales_ranking_month': '1',
         'maker_ranking': '1', 'ranking_compact_cars': '1'},
        {'date': '2020-04', 'monthly_sales': '41470', 'share_manufacturers': '50.46%', 'sales_ranking_month': '1',
         'maker_ranking': '1', 'ranking_compact_cars': '1'},
        {'date': '2020-03', 'monthly_sales': '23937', 'share_manufacturers': '53.33%', 'sales_ranking_month': '2',
         'maker_ranking': '1', 'ranking_compact_cars': '2'},
        {'date': '2020-02', 'monthly_sales': '6519', 'share_manufacturers': '44.52%', 'sales_ranking_month': '1',
         'maker_ranking': '1', 'ranking_compact_cars': '1'},
        {'date': '2020-01', 'monthly_sales': '37255', 'share_manufacturers': '41.40%', 'sales_ranking_month': '1',
         'maker_ranking': '1', 'ranking_compact_cars': '1'},
        {'date': '2019-12', 'monthly_sales': '53626', 'share_manufacturers': '45.54%', 'sales_ranking_month': '2',
         'maker_ranking': '1', 'ranking_compact_cars': '2'},
        {'date': '2019-11', 'monthly_sales': '54348', 'share_manufacturers': '47.50%', 'sales_ranking_month': '1',
         'maker_ranking': '1', 'ranking_compact_cars': '1'},
        {'date': '2019-10', 'monthly_sales': '48483', 'share_manufacturers': '45.24%', 'sales_ranking_month': '1',
         'maker_ranking': '1', 'ranking_compact_cars': '1'},
        {'date': '2019-09', 'monthly_sales': '42972', 'share_manufacturers': '40.01%', 'sales_ranking_month': '2',
         'maker_ranking': '1', 'ranking_compact_cars': '2'},
        {'date': '2019-08', 'monthly_sales': '33795', 'share_manufacturers': '33.08%', 'sales_ranking_month': '1',
         'maker_ranking': '1', 'ranking_compact_cars': '1'},
        {'date': '2019-07', 'monthly_sales': '25008', 'share_manufacturers': '31.06%', 'sales_ranking_month': '6',
         'maker_ranking': '1', 'ranking_compact_cars': '6'},
        {'date': '2019-06', 'monthly_sales': '32629', 'share_manufacturers': '33.52%', 'sales_ranking_month': '2',
         'maker_ranking': '1', 'ranking_compact_cars': '2'},
        {'date': '2019-05', 'monthly_sales': '30889', 'share_manufacturers': '34.60%', 'sales_ranking_month': '6',
         'maker_ranking': '1', 'ranking_compact_cars': '4'},
        {'date': '2019-04', 'monthly_sales': '27902', 'share_manufacturers': '34.38%', 'sales_ranking_month': '4',
         'maker_ranking': '1', 'ranking_compact_cars': '3'},
        {'date': '2019-03', 'monthly_sales': '45038', 'share_manufacturers': '39.51%', 'sales_ranking_month': '2',
         'maker_ranking': '1', 'ranking_compact_cars': '2'},
        {'date': '2019-02', 'monthly_sales': '23553', 'share_manufacturers': '38.55%', 'sales_ranking_month': '4',
         'maker_ranking': '1', 'ranking_compact_cars': '2'}]


df = pd.DataFrame(data[1:],
                  columns=['date', 'monthly_sales', 'share_manufacturers', 'sales_ranking_month', 'maker_ranking',
                           'ranking_compact_cars'], dtype=str)
print(df)
df.to_csv('test1.csv')