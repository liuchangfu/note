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
        # 抓取第1页到第51页的数据
        for page in range(1, 51):
            yield feapder.Request(f"https://chaping.chayu.com/?p={page}", page=page)  # 把page的值传入到parse方法

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
            # class为param的div标签，有4个P标签，p[2]取第2个P标签的值
            brand = con.xpath('.//div[@class="fl tea_info"]/div[@class="param"]/p[2]/a/text()').extract_first()
            prod = con.xpath('.//div[@class="fl tea_info"]/div[@class="param"]/p[3]/a/text()').extract_first()
            # callback为回调方法，调用parse_detail方法，获取详情页的数据,把title，score，brand，prod的值传入parse_detail方法
            yield feapder.Request(url, callback=self.parse_detail, title=title, score=score, brand=brand, prod=prod)

    def parse_detail(self, request, response):
        # 用request.字段名接收接收parse方法传入过来的url,title,score,brand,prod,desc的值，
        url = request.url
        title = request.title
        score = request.score
        brand = request.brand
        prod = request.prod
        desc = response.xpath('//div[@class="txt_box"]/div[@class="fl con"]/text()').extract_first()
        log.info(f'{url},{title},{score},{brand},{prod},{desc}')
        # 实例化Item()
        item = Item()
        # 数据库名称
        item.table_name = 'chayu_rank'
        item.url = url
        item.title = title
        item.score = score
        item.brand = brand
        item.prod = prod
        item.desc = desc
        # 批量入库
        yield item


if __name__ == "__main__":
    # thread_count 为线程数
    AirSpiderTest(thread_count=10).start()
