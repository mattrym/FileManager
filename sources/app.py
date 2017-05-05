import os.path
import tornado.web
from .handlers import (
        MainHandler,
        )

handlers = [
        (r'/', MainHandler)
        ]

settings = {
        'template_path': os.path.join(os.getcwd(), 'templates'),
        'static_path': os.path.join(os.getcwd(), 'static'),
        'debug': True,
        }

class FMApplication(tornado.web.Application):
    def __init__(self):
        tornado.web.Application.__init__(self, handlers, **settings)

def make_application():
    return FMApplication()
