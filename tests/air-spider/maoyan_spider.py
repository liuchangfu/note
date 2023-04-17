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

    def start_requests(self):
        yield feapder.Request("https://www.maoyan.com/board/4?offset=0",render=True)

    def download_midware(self, request):
        request.headers = {
            'User-Agent': "'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) "
                          "Chrome/29.0.1547.62 Safari/537.36'"}
        return request

    def validate(self, request, response):
        if response.status_code != 200:
            raise Exception("response code not 200")

    def parse(self, request, response):
        movie_list = response.xpath('//dl[@class="board-wrapper"]/dd')
        log.info(movie_list)
        log.info(len(movie_list))
        for movie in movie_list:
            rank = movie.xpath('./i/text()').extract_first()
            title = movie.xpath('./a/@title').extract_first()
            star = movie.xpath('./div[@class="movie-item-info"]/p[@class="star"]/text()').extract_first()
            release_time = movie.xpath('./div[@class="movie-item-info"]/p[@class="releasetime"]/text()').extract_first()
            score1 = movie.xpath('./div[@class="movie-item-number score-num"]/p/i[1]/text()').extract_first()
            score2 = movie.xpath('./div[@class="movie-item-number score-num"]/p/i[2]/text()').extract_first()
            log.info(f'{rank},{title},{star},{release_time},{score1},{score2}')


if __name__ == "__main__":
    AirSpiderTest().start()
