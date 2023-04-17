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
        yield feapder.Request("https://www.maoyan.com/board/4?offset=0")

    def parse(self, request, response):
        movie_list = response.xpath('//dl[@class="board-wrapper"]/dd')
        for movie in movie_list:
            item = Item()
            # 数据库表名
            item.table_name = 'chayu_rank'
            item.url = movie.xpath('./a/@href').extract_first()
            item.title = movie.xpath('./a/text()').extract_first()
            item.score = movie.xpath('./span/em/text()').extract_first()
            # 批量入库
            yield item
            log.info(f'正写入数据库。。。')


if __name__ == "__main__":
    AirSpiderTest().start()
