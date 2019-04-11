#!/usr/bin/env python

import json
import time
import urllib.parse
import urllib.request

from core import info_collection
from conf import settings


class ArgvHandler(object):
    def __init__(self, args):
        self.args = args
        self.parse_args()

    def parse_args(self):
        if len(self.args) > 1 and hasattr(self, self.args[1]):
            func = getattr(self, self.args[1])
            func()
        else:
            self.help_msg()

    @staticmethod
    def help_msg():
        msg = '''收集硬件信息'''

        print(msg)

    @staticmethod
    def collect_data():
        info = info_collection.InfoCollection()
        asset_data = info.collect()
        print(asset_data)

    @staticmethod
    def report_data():
        info = info_collection.InfoCollection()
        asset_data = info.collect()

        data = {'asset_data': json.dumps(asset_data)}
        url = 'http://%s:%s%s' % (settings.Params['server'], settings.Params['port'], settings.Params['url'])
        print('正在将数据发送至：【%s】。。。。' % url)

        try:
            data_encode = urllib.parse.urlencode(data).encode()

            response = urllib.request.urlopen(url=url, data=data_encode, timeout=settings.Params['request_timeout'])
            print('\033[31;1m发送完毕！\033[0m ')
            message = response.read().decode()
            print('返回结果：%s' % message)

        except Exception as e:
            message = '发送失败'
            print('\033[31;1m发送失败，%s\033[0m' % e)

        with open(settings.PATH, 'ab') as f:
            string = '发送时间：%s \t 服务器地址：%s \t 返回结果：%s \n' % (time.strftime('%Y-%m-%d %H:%M:%S'), url, message)
            f.write(string.encode())
            print('日志记录成功！')
