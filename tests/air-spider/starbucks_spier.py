# coding=utf-8
"""
@IDE：PyCharm
@project: feapder
@Author：Liuchangfu
@file： starbucks_spier.py
@date：2023/4/14 10:26
 """
import re

import feapder
from feapder.utils.log import log
import requests
from pathlib import Path


class AirSpiderTest(feapder.AirSpider):

    def start_requests(self):
        yield feapder.Request("https://www.starbucks.com.cn/menu/")

    def parse(self, request, response):
        menu_list = response.xpath('//ul[@class="grid padded-3 product"]/li/a')
        log.info(menu_list)
        log.info(len(menu_list))
        for menu in menu_list:
            url = re.findall('(/images.*.jpg)',
                             str(menu.xpath('.//div[@class="preview circle"]/@style').extract_first()))
            name = menu.xpath('.//strong/text()').extract_first()
            if len(url) != 0:
                img_url = 'https://www.starbucks.com.cn' + url[0]
                img_rul_content = requests.get(img_url).content
                current_folder = Path.cwd()
                images_folder = current_folder / 'images'
                if not Path.exists(images_folder):
                    Path.mkdir(images_folder)
                try:
                    with open(f'{images_folder}\\{name}.png', 'wb') as f:
                        f.write(img_rul_content)
                        log.info(f'{name},{img_url}')
                except FileNotFoundError as e:
                    log.info(f'{images_folder}\\{name}.png,无法写入!!,错误原因：{e}')


if __name__ == "__main__":
    AirSpiderTest(thread_count=5).start()
