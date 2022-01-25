#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
"""
@Author: awei84    
@Contact:  xx
@Modify_Time: 2022/1/17 14:47       
@Desciption: 豆瓣电影分类排行榜查询
"""

import urllib3
import requests

urllib3.disable_warnings()


def CrawlerMovie(url, params):
    res = []
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36"
    }
    r = requests.get(url, headers=headers, verify=False, params=params)
    if r.content:
        res = r.json()
    return res


def main(type_c="", interval_id="", start="", limit=""):
    if not type_c:
        type_c = "动作"
    if not interval_id:
        interval_id = "100:90"
    if not start:
        start = "0"
    if not limit:
        limit = "20"
    type_num = {"动作": "13"}
    params = {
        "type": type_num[type_c],  # 分类
        "interval_id": interval_id,  # 好于100%-90%
        "action": "",
        "start": start,  # 开始
        "limit": limit,  # top 多少
    }
    url = "https://movie.douban.com/j/chart/top_list"
    res = CrawlerMovie(url, params)
    # 获取数据，整理格式输出
    if res:
        for each in res:
            rank = each["rank"]
            movie_name = each["title"]
            regions = ",".join(each["regions"])
            types = each["types"]
            cover_url = each["cover_url"]
            url_ = each["url"]
            release_date = each["release_date"]
            actors = ",".join(each["actors"])
            print(
                f"排名：{rank}\n电影名称：{movie_name}，国家：{regions}, 类型：{types}\n封面：{cover_url}\n豆瓣链接：{url_}\n电影发布时间：{release_date}\n主演名单：{actors} \n"
            )


if __name__ == "__main__":
    type_c = input("电影类型(默认值：动作):")
    interval_id = input("好评区间（默认值：100:90）:")
    limit = input("获取电影数量（默认值:20）:")
    main(type_c=type_c, interval_id=interval_id, limit=limit)
