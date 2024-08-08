#【练习】封装网络请求工具

# 知识点
# 类和方法
# HTTP 请求
# 请求头
# 回调函数

# 作业要求
# 编写一个Python程序，封装一个网络请求工具类。
# 对 get/post/put/delete四种请求方式分别封装对应的请求方法
# 参数有 `url, header(使用字典)`，`callback`回调函数
# `callback`回调函数中，用来显示前两个参数的信息

import requests

class HttpRequestTools:
    @classmethod
    def get(cls, url: str, header: dict, callback):
        callback(url, header)

    @classmethod
    def post(cls, url: str, header: dict, callback):
        callback(url, header)

    @classmethod
    def put(cls, url: str, header: dict, callback):
        callback(url, header)

    @classmethod
    def delete(cls, url: str, header: dict, callback):
        callback(url, header)


def func(url: str, header: dict):
    print(f"请求的网址为：{url}")
    print(f"请求的信息有：")
    for k, v in header.items():
        print(f"{k}: {v}")

HttpRequestTools.get('http://www.baidu.com', {"content-type":"text/html", "cache-control":"no-cache"}, func)
# 请求的网址为：http://www.baidu.com
# 请求的信息有：
# content-type: text/html
# cache-control: no-cache
HttpRequestTools.post('http://www.baidu.com', {"content-type":"text/html"}, func)
HttpRequestTools.put('http://www.baidu.com', {"content-type":"text/html"}, func)
HttpRequestTools.delete('http://www.baidu.com', {"content-type":"text/html"}, func)

