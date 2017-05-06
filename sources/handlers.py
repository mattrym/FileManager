import requests
import tornado.web
import tornado.httpclient
from .utils import *

class BaseHandler(tornado.web.RequestHandler):
    def initialize(self, rootpath):
        self.rootpath = rootpath

    def get_current_user(self):
        return self.get_secure_cookie("user")

class LoginHandler(BaseHandler):
    def post(self):
        entered_login = self.get_argument('login')
        entered_password = self.get_argument('password')

        if (self.application.settings['login'] == entered_login and 
                self.application.settings['password'] == entered_password):
            self.set_secure_cookie('user', entered_login)
        self.redirect('/')

class LogoutHandler(BaseHandler):
    def get(self):
        self.clear_cookie('user')
        self.redirect('/')

class DownloadHandler(BaseHandler):
    def get(self, relpath):
        abspath = get_abspath(relpath, self.rootpath)
        filename = get_basename(relpath).replace(' ', '_')
        print(filename)
        if not relpath or not os.path.exists(abspath):
            raise HTTPError(404)
        self.set_header('Content-Type', 'application/force-download')
        self.set_header('Content-Disposition', 'attachment; filename=%s' % filename)
        with open(abspath, "rb") as f:
            try:
                while True:
                    buffer = f.read(4096)
                    if buffer:
                        self.write(buffer)
                    else:
                        f.close()
                        self.finish()
                        return
            except:
                raise HTTPError(404)
        raise HTTPError(500)

class UploadHandler(BaseHandler):
    @tornado.web.authenticated
    def post(self, relpath):
        try:
            uploadFile = self.request.files['uploadFile'][0]
            filename = get_basename(uploadFile['filename'])
            frelpath = get_relpath(filename, relpath)
            fabspath = get_abspath(frelpath, self.rootpath)
            print(fabspath)

            with open(fabspath, 'wb') as fd:
                fd.write(uploadFile['body'])
        except KeyError:
            response = 'No file selected'
        except IOError as error:
            raise HTTPError(500) 
        self.redirect("/" + relpath)

class MainHandler(BaseHandler):
    def get(self, relpath):
        self.render('main-template.html',
                currpath = relpath,
                currdir = get_basename(relpath),
                subdirs = get_subdirs(relpath, self.rootpath),
                subfiles = get_subfiles(relpath, self.rootpath))
