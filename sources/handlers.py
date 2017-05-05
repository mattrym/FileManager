import os
import tornado.web

def abs_path(rel_path):

    return os.path.join(root_dir, rel_path)

class BaseHandler(tornado.web.RequestHandler):

    def write_error(self, status_code, **kwargs):
        tornado.web.RequestHandler.write_error(self, status_code, **kwargs)

class DirectoryHandler(BaseHandler):
    
    def get(self, dir_path):
        
        self.write(dir_path)

class LoginHandler(BaseHandler):
    pass

class MainHandler(BaseHandler):

    def get(self):
        self.render("index.html")
