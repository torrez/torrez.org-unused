import base

class UptimeHandler(base.BaseHandler):
    def get(self):
        return self.write('success')

class XuMouseHandler(base.BaseHandler):
    def get(self):
        return self.redirect("/projects")
        
class XuMouseDownloadHandler(base.BaseHandler):
    def get(self):
        return self.redirect("/static/files/XuMouse.zip")