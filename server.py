import os.path

import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web

from lib.core.engine import scan

from tornado.options import define, options
define("port", default=8000, help="run on the given port", type=int)

class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('index.html')

class FeedBackHandler(tornado.web.RequestHandler):
    def post(self):
        target = self.get_argument('target')
        self.render('feedback.html', target=scan(target))

if __name__ == '__main__':
    tornado.options.parse_command_line()
    app = tornado.web.Application(
        handlers=[(r'/', IndexHandler), (r'/feedback', FeedBackHandler)],
        template_path=os.path.join(os.path.dirname(__file__), "templates")
    )
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
