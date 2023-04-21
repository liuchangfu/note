# coding=utf-8
"""
@IDE：PyCharm
@project: feapder
@Author：Liuchangfu
@file： ex_code.py
@date：2023/4/14 9:35
 """
import json
import time
from feapder.utils.log import log
import feapder
from feapder import Item
from feapder.pipelines import BasePipeline


class FeapderAirSpider(feapder.AirSpider):
    """
    必应爬虫
    """

    __custom_setting__ = dict(
        # 指定数据存储pipeline，框架内置mysql，mongo。这里存txt，因此指向自定义pipeline
        ITEM_PIPELINES=[
            # "feapder.pipelines.mysql_pipeline.MysqlPipeline",
            # "feapder.pipelines.mongo_pipeline.MongoPipeline",
            "ex_code.Pipeline"
        ],
        # 框架日志等级
        LOG_LEVEL="DEBUG"
    )

    def start_requests(self):
        """
        下发任务
        :return:
        """
        keyword = "feapder"
        # 翻5页
        for i in range(1, 50, 10):
            yield feapder.Request(
                f"https://cn.bing.com/search?q={keyword}&pq={keyword}&first={i}",
                keyword=keyword,
            )

    def download_midware(self, request):
        """
        下载中间件
        :param request:
        :return:
        """
        # 自定义请求头，否则会自动随机
        request.headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) "
                          "Chrome/92.0.4515.159 Safari/537.36"
        }
        # request.cookies = {}
        # request.proxies = {}
        return request

    def validate(self, request, response):
        """
        校验函数, 可用于校验response是否正确
            若函数内抛出异常，则重试请求
            若返回True 或 None，则进入解析函数
            若返回False，则抛弃当前请求
            可通过request.callback_name 区分不同的回调函数，编写不同的校验逻辑
        :param request:
        :param response:
        :result: True / None / False
        """
        if response.status_code == 404:
            return False  # 忽略当前请
        elif response.status_code != 200:
            raise Exception(response)  # 返回状态码 不为200，抛异常，触发自动重试

    def parse(self, request, response):
        """
        默认的解析函数
        :param request:
        :param response:
        :return:
        """
        keyword = request.keyword
        results = response.css(".b_title > h2")
        for result in results:
            title = result.xpath("string(.)").extract_first(default="").strip()
            url = result.xpath(".//a/@href").extract_first()

            # 创建item 并入库
            item = Item()
            item.table_name = "biying"
            item.title = title
            item.url = url
            item.search_keyword = keyword
            yield item

            # 下发详情任务
            # yield feapder.Request(url, callback=self.parse_detail)

    def parse_detail(self, request, response):
        """
        解析详情
        :param request:
        :param response:
        :return:
        """
        log.info(f"解析详情:{response.url}")

    def start_callback(self):
        """
        @summary: 程序开始的回调
        ---------
        ---------
        @result: None
        """
        self.start_time = time.time()

    def end_callback(self):
        """
        @summary: 程序结束的回调
        ---------
        ---------
        @result: None
        """

        self.end_time = time.time()
        log.info(f"耗时 {self.end_time - self.start_time}")


class Pipeline(BasePipeline):
    def save_items(self, table, items) -> bool:
        """
        保存数据
        Args:
            table: 表名
            items: 数据，[{},{},...]

        Returns: 是否保存成功 True / False
                 若False，不会将本批数据入到去重库，以便再次入库

        """
        for item in items:
            log.info(f'{item}')
            log.info(f'{table}')
            with open(f"{table}.txt", "a") as file:
                file.write(json.dumps(item, ensure_ascii=False) + "\n")

        return True


if __name__ == "__main__":
    # 启动5个线程
    FeapderAirSpider(thread_count=5).start()
