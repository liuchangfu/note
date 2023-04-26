# -*- coding: utf-8 -*-
"""
Created on 2021-02-08 16:06:12
---------
@summary:
---------
@author: Boris
"""

import feapder
from feapder import Item, UpdateItem
from feapder.utils.log import log


class TestMongo(feapder.AirSpider):
    __custom_setting__ = dict(
        ITEM_PIPELINES=["feapder.pipelines.mongo_pipeline.MongoPipeline"],
        MONGO_IP="localhost",
        MONGO_PORT=27017,
        MONGO_DB="nba",
        MONGO_USER_NAME="",
        MONGO_USER_PASS="",
    )

    def start_requests(self):
        type_list = ['得分', '篮板', '助攻', '抢断', '盖帽', '犯规', '失误']
        for i in range(len(type_list)):
            yield feapder.Request(
                f"https://stats.qiumibao.com/shuju/public/index.php?_url=/data/index&league=NBA&tab=%E7%90%83%E5%91%98%E6%A6%9C&type={type_list[i]}&year=2022&_t=1682475934704&_platform=web&_env=pc",
                t_date=type_list[i])

    def parse(self, request, response):
        dates = response.json
        log.info(f'正在获取{request.t_date}的数据。。。')
        log.info(f"{dates}")
        log.info(f'{dates["type"]}')
        # log.info(f'{dates["data"][0]["list"]}')
        # log.info(f'{dates["data"][0]["list"][0]}')
        # if dates["type"] == 'fangui' or dates["type"] == 'shiwu':
        #     log.info(f'排名---{dates["data"][0]["list"][0]["排名"]}')
        #     log.info(f'球队---{dates["data"][0]["list"][0]["球队"]}')
        #     log.info(f'球员---{dates["data"][0]["list"][0]["球员"]}')
        #     log.info(f'场均---{dates["data"][0]["list"][0]["场均"]}')
        #     log.info(f'场次---{dates["data"][0]["list"][0]["场次"]}')
        #     log.info(f'篮板---{dates["data"][0]["list"][0]["时间"]}')
        # else:
        #     log.info(f'排名---{dates["data"][0]["list"][0]["排名"]}')
        #     log.info(f'球队---{dates["data"][0]["list"][0]["球队"]}')
        #     log.info(f'球员---{dates["data"][0]["list"][0]["球员"]}')
        #     log.info(f'场均---{dates["data"][0]["list"][0]["场均"]}')
        for index in range(len(dates["data"][0]["list"])):
            item = Item()
            item.table_name = dates["type"]
            if dates["type"] == 'fangui' or dates["type"] == 'shiwu':
                item.rank = dates["data"][0]["list"][index]["排名"]
                item.team = dates["data"][0]["list"][index]["球队"]
                item.player = dates["data"][0]["list"][index]["球员"]
                item.changjun = dates["data"][0]["list"][index]["场均"]
                yield item
            else:
                item.rank = dates["data"][0]["list"][index]["排名"]
                item.team = dates["data"][0]["list"][index]["球队"]
                item.player = dates["data"][0]["list"][index]["球员"]
                item.changjun = dates["data"][0]["list"][index]["场均"]
                item.changci = dates["data"][0]["list"][index]["场次"]
                item.time = dates["data"][0]["list"][index]["时间"]
                yield item


if __name__ == "__main__":
    TestMongo().start()
