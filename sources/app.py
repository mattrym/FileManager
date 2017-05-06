import os.path
import tornado.web
from .handlers import (
        LoginHandler,
        LogoutHandler,
        DownloadHandler,
        UploadHandler,
        MainHandler,
        )
from . import modules

source_dir = os.path.dirname(__file__)
top_dir = os.path.dirname(source_dir)

class FMApplication(tornado.web.Application):
    def __init__(self, rootpath):
        init_dict = {'rootpath': rootpath}
        handlers = [
                (r'/login', LoginHandler, init_dict),
                (r'/logout', LogoutHandler, init_dict),
                (r'/upload/(.*)', UploadHandler, init_dict),
                (r'/download/(.*)', DownloadHandler, init_dict),
                (r'/static/(.*)', tornado.web.StaticFileHandler, {'path': 'static'}),
                (r'/(.*)', MainHandler, init_dict),
                ]
        settings = {
                'login': 'admin',
                'password': 'password',
                'ui_modules': modules,
                'template_path': os.path.join(top_dir, 'templates'),
                'static_path': os.path.join(top_dir, 'static'),
                'cookie_secret': 'f0bd1353-0143-4038-9e58-f35092e3cd20',
                }

        tornado.web.Application.__init__(self,
                handlers, **settings)

def make_application(rootdir):
    return FMApplication(rootdir)
