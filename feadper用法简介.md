# #  feadper文档

[feapder官方文档|feapder-document](https://feapder.com/#/README)[feapder官方文档|feapder-document](https://feapder.com/#/README)



# 知识扩展--Xpath语法简介

[Python爬虫必备技能，Xpath提取数据规格详解_Python新世界的博客-CSDN博客](https://blog.csdn.net/weixin_46089319/article/details/107911187?spm=1001.2101.3001.6650.2&utm_medium=distribute.pc_relevant.none-task-blog-2~default~CTRLIST~default-2-107911187-blog-80672281.pc_relevant_multi_platform_whitelistv2&depth_1-utm_source=distribute.pc_relevant.none-task-blog-2~default~CTRLIST~default-2-107911187-blog-80672281.pc_relevant_multi_platform_whitelistv2&utm_relevant_index=4)



# # 代码1

```python
# coding=utf-8
"""
@IDE：PyCharm
@project: feapder
@Author：Liuchangfu
@file： test_chayu_spider.py
@date：2023/4/7 11:12
 """
import feapder
import os
from feapder.utils.log import log

from feapder.setting import LOG_NAME


class AirSpiderTest(feapder.AirSpider):
    # 日志配置
    __custom_setting__ = dict(
        LOG_NAME=os.path.basename(os.getcwd()),
        LOG_PATH="log/%s.log" % LOG_NAME,  # log存储路径
        LOG_LEVEL="DEBUG",
        LOG_COLOR=True,  # 是否带有颜色
        LOG_IS_WRITE_TO_CONSOLE=True,  # 是否打印到控制台
        LOG_IS_WRITE_TO_FILE=True,  # 是否写文件
        LOG_MODE="w",  # 写文件的模式
        LOG_MAX_BYTES=10 * 1024 * 1024,  # 每个日志文件的最大字节数
        LOG_BACKUP_COUNT=20,  # 日志文件保留数量
        LOG_ENCODING="utf8",  # 日志文件编码
        OTHERS_LOG_LEVAL="ERROR",  # 第三方库的log等级
    )

    def start_requests(self):
        yield feapder.Request("https://chaping.chayu.com/")

    def parse(self, request, response):
        con_list = response.xpath('//ul[@class="con"]/li')
        log.info(con_list)
        log.info(len(con_list))
        for con in con_list:
            url = con.xpath('./a/@href').extract_first()
            title = con.xpath('./a/text()').extract_first()
            score = con.xpath('./span/em/text()').extract_first()
            log.info(f'{url},{title},{score}分')


if __name__ == "__main__":
    AirSpiderTest().start()


```

# 代码2

```python
# coding=utf-8
"""
@IDE：PyCharm
@project: feapder
@Author：Liuchangfu
@file： test_chayu_spider.py
@date：2023/4/7 11:12
 """
import feapder
from feapder.utils.log import log
from feapder import Item


class AirSpiderTest(feapder.AirSpider):
    __custom_setting__ = dict(
        # MYSQL配置
        MYSQL_IP="localhost",
        MYSQL_PORT=3306,
        MYSQL_DB="feapder",
        MYSQL_USER_NAME="root",
        MYSQL_USER_PASS="lcfwku",
    )

    def start_requests(self):
        for page in range(1, 11):
            yield feapder.Request(f"https://chaping.chayu.com/?p={page}", page=page)

    def parse(self, request, response):
        log.info(f'正在抓报第{request.page}页的数据。。')
        con_list = response.xpath('//div[@class="search_list tea_comment_list"]/div[@class="list"]')
        for con in con_list:
            url = con.xpath('./div[@class="fl tea_info"]/div[@class="thumb"]/a/@href').extract_first()
            title = con.xpath('./div[@class="fl tea_info"]/div[@class="thumb"]/a/@title').extract_first()
            score1 = con.xpath(
                './div[@class="fl tea_info"]/div[@class="param"]/p/span[@class="score Yahei"]/text()').extract_first()
            score2 = con.xpath(
                './div[@class="fl tea_info"]/div[@class="param"]/p/span[@class="score Yahei"]/em[@class="colorde5406"]/text()').extract_first()
            score = score1 + score2
            brand = con.xpath('.//div[@class="fl tea_info"]/div[@class="param"]/p[2]/a/text()').extract_first()
            prod = con.xpath('.//div[@class="fl tea_info"]/div[@class="param"]/p[3]/a/text()').extract_first()
            yield feapder.Request(url, callback=self.parse_detail, title=title, score=score, brand=brand, prod=prod)

    def parse_detail(self, request, response):
        url = request.url
        title = request.title
        score = request.score
        brand = request.brand
        prod = request.prod
        desc = response.xpath('//div[@class="txt_box"]/div[@class="fl con"]/text()').extract_first()
        log.info(f'{url},{title},{score},{brand},{prod},{desc}')
        item = Item()
        item.table_name = 'chayu_rank'
        item.url = url
        item.title = title
        item.score = score
        item.brand = brand
        item.prod = prod
        item.desc = desc
        yield item


if __name__ == "__main__":
    AirSpiderTest().start()


```

# 代码3

```python
# coding=utf-8
"""
@IDE：PyCharm
@project: feapder
@Author：Liuchangfu
@file： test_chayu_spider.py
@date：2023/4/7 11:12
 """
import feapder
from feapder.utils.log import log
from feapder import Item


class AirSpiderTest(feapder.AirSpider):
    __custom_setting__ = dict(
        # # MYSQL数据库
        MYSQL_IP="localhost",
        MYSQL_PORT=3306,
        MYSQL_DB="feapder",
        MYSQL_USER_NAME="root",
        MYSQL_USER_PASS="lcfwku",
    )

    def start_requests(self):
        yield feapder.Request("https://chaping.chayu.com/")

    def parse(self, request, response):
        con_list = response.xpath('//ul[@class="con"]/li')
        for con in con_list:
            item = Item()            
```
