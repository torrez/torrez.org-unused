#!/usr/bin/env python
import tornado.httpserver
import tornado.ioloop
import tornado.web
from tornado.options import define, options

from settings import settings
from routes import routes

if __name__ == "__main__":
    define("on_port", default=8002, help="Run on port")
    tornado.options.parse_command_line()
    
    application = tornado.web.Application(routes,  **settings)
    http_server = tornado.httpserver.HTTPServer(application)
    
    print "starting on port %s" % (options.on_port)
    http_server.listen(int(options.on_port))
    tornado.ioloop.IOLoop.instance().start()