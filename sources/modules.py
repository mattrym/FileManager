import os.path
import tornado.web

class LoginModule(tornado.web.UIModule):
    def render(self):
        if self.current_user:
            return self.render_string("logout-module.html")
        return self.render_string("login-module.html")

class UploadModule(tornado.web.UIModule):
    def render(self, relpath):
        return self.render_string("upload-module.html",
                currpath = relpath)

class ParentDirModule(tornado.web.UIModule):
    def render(self, relpath):
        parent_path = os.path.dirname(relpath)
        return self.render_string("dir-module.html",
                relpath = parent_path, name = "..")

class DirModule(tornado.web.UIModule):
    def render(self, relpath):
        name = os.path.basename(relpath)

        return self.render_string("dir-module.html",
                relpath = relpath, name = name)

class FileModule(tornado.web.UIModule):
    def render(self, relpath):
        name = os.path.basename(relpath)
        relpath = os.path.join("download", relpath)

        return self.render_string("file-module.html",
                 relpath = relpath, name = name)
