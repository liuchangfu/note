# -*- coding: utf-8 -*-
"""
Created on 2023-04-19 15:08:38
---------
@summary:
---------
@author: SL-COM-254
"""
import json
import feapder
from feapder.utils.log import log
from items import *
from feapder.pipelines import BasePipeline
from feapder import Item
import csv


class Jincongxing(feapder.AirSpider):
    __custom_setting__ = dict(
        # 指定数据存储pipeline，框架内置mysql，mongo。这里存txt，因此指向自定义pipeline
        ITEM_PIPELINES=[
            # "feapder.pipelines.mysql_pipeline.MysqlPipeline",
            # "feapder.pipelines.mongo_pipeline.MongoPipeline",
            "spiders.jincongxing.Pipeline"
        ],
        # 框架日志等级
        LOG_LEVEL="DEBUG"
    )

    def start_requests(self):
        for page in range(1, 3):
            yield feapder.Request(f"https://xl.16888.com/level-3-{page}.html")

    def parse(self, request, response):
        sales_list = response.xpath('//table[@class="xl-table-def xl-table-a"]//tr')
        for sale in sales_list:
            rank = sale.xpath('.//td[@class="xl-td-t1"]/text()').extract_first()
            vehicle_type = sale.xpath('.//td[@class="xl-td-t2"][1]/a/text()').extract_first()
            manufacturers = sale.xpath('.//td[@class="xl-td-t2"][2]/a/text()').extract_first()
            sales = sale.xpath('.//td[@class="xl-td-t3"]/text()').extract_first()
            price = sale.xpath('.//td[@class="xl-td-t5"]/a/text()').extract_first()
            histroy_sale_url = sale.xpath('.//div[@class="lbBox"]/a[1]/@href').extract_first()
            # if rank is not None or vehicle_type is not None or manufacturers is not None or sales is not None or price is not None:
            #     item = jincongxin_item.JincongxinItem()  # 声明一个item
            #     item.rank = rank
            #     item.manufacturers = manufacturers  # 给item属性赋值
            #     item.vehicle_type = vehicle_type
            #     item.sales = sales
            #     item.price = price
            #     yield item
            yield feapder.Request(histroy_sale_url, callback=self.parse_detail, rank=rank, vehicle_type=vehicle_type,
                                  manufacturers=manufacturers, sales=sales, price=price,
                                  histroy_sale_url=histroy_sale_url)

    def parse_detail(self, request, response):
        histroy_sale_url = request.histroy_sale_url
        rank = request.rank
        vehicle_type = request.vehicle_type
        manufacturers = request.manufacturers
        sales = request.sales
        price = request.price
        # if rank is not None or vehicle_type is not None or manufacturers is not None or sales is not None or price is not None:
        # item = jincongxin_item.JincongxinItem()  # 声明一个item
        # item.rank = rank
        # item.manufacturers = manufacturers  # 给item属性赋值
        # item.vehicle_type = vehicle_type
        # item.sales = sales
        # item.price = price
        # yield item
        log.info(f'{rank}--{vehicle_type}--{manufacturers}--{sales}---{price}')
        if histroy_sale_url is not None:
            sales_list = response.xpath('//table[@class="xl-table-def xl-table-a"]//tr')
            for sale in sales_list:
                date = sale.xpath('.//td[@class="xl-td-t4"][1]/text()').extract_first()
                monthly_sales = sale.xpath('.//td[@class="xl-td-t4"][2]/text()').extract_first()
                share_manufacturers = sale.xpath('.//td[@class="xl-td-t4"][3]/text()').extract_first()
                sales_ranking_month = sale.xpath('.//td[@class="xl-td-t5"][1]/a/text()').extract_first()
                maker_ranking = sale.xpath('.//td[@class="xl-td-t5"][2]/a/text()').extract_first()
                ranking_compact_cars = sale.xpath('.//td[@class="xl-td-t5"][3]/a/text()').extract_first()
                log.info(
                    f'{vehicle_type}--日期：{date}---月销量(辆)：{monthly_sales}---占厂商份额:{share_manufacturers}--当月销量排名:{sales_ranking_month}--在厂商排名:{maker_ranking}--在紧凑型车排名:{ranking_compact_cars}')
                # 创建item 并入库
                item = Item()
                item.table_name = vehicle_type
                item.date = date
                item.monthly_sales = monthly_sales
                item.share_manufacturers = share_manufacturers
                item.sales_ranking_month = sales_ranking_month
                item.maker_ranking = maker_ranking
                item.ranking_compact_cars = ranking_compact_cars
                yield item


class Pipeline(BasePipeline):
    def save_items(self, table, items) -> bool:
        """
        保存数据
        Args:
            table: 表名
            items: 数据，[{},{},...]

        Returns: 是否保存成功 True / False
                 若False，不会将本批数据入到去重库，以便再次入库

        # # """
        # 保存为TXT文件
        # for item in items:
        #     with open(f"./txt/{table}.txt", "a") as file:
        #         file.write(json.dumps(item, ensure_ascii=False) + "\n")

        # 保存为CSV文件
        with open(f'./csv/{table}.csv', 'w', newline='') as file:
            fieldnames = ['date', 'monthly_sales', 'share_manufacturers', 'sales_ranking_month', 'maker_ranking',
                          'ranking_compact_cars']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            # 写入表头
            writer.writeheader()
            # 写入数据
            writer.writerows(items[1:])
        return True


if __name__ == "__main__":
    Jincongxing().start()
