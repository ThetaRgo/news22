#!/usr/bin/env python
# encoding:utf-8
# @Time   : 2018/3/26
# @Author : 茶葫芦
# @Site   : 
# @File   : sale_server.py

import tornado.web
import tornado.ioloop
import urls
import config
import torndb
import redis


class Application(tornado.web.Application):
    def __init__(self, *args, **kwargs):
        super(Application, self).__init__(*args, **kwargs)
        self.db = torndb.Connection(**config.mysqlconf)
        self.redis= redis.StrictRedis(**config.redisconf)


def main():
    tornado.options.parse_command_line()
    app = Application(urls.rute_urls,
                      **config.settings
                      )
    app.listen(urls.options['port'])
    tornado.ioloop.IOLoop.current().start()


if __name__ == '__main__':
    print "web running"
    main()
