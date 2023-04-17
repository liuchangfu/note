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
