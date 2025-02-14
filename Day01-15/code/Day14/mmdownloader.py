from time import time
from threading import Thread

import requests


class DownloadHanlder(Thread):

    def __init__(self, url):
        super().__init__()
        self.url = url

    def run(self):
        # rfind('/')为之前数据，需要修改如下
        filename = self.url[self.url.rfind('\\') + 1:]
        resp = requests.get(self.url)
        with open('e:\\PythonDownloads\\' + filename, 'wb') as f:
            f.write(resp.content)


def main():
    # 通过requests模块的get函数获取网络资源...
    resp = requests.get(
        'http://api.tianapi.com/usermake/index?key=6f9dd432e7bf2ab15dde5f0b4dcdc9f9&num=10&urlid=133')
    # 将服务器返回的JSON格式的数据解析为字典
    data_model = resp.json()
    for mm_dict in data_model['newslist']:
        url = mm_dict['picUrl']
        # 通过多线程的方式实现图片下载
        DownloadHanlder(url).start()


if __name__ == '__main__':
    main()