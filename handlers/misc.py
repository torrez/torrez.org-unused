import base

class UptimeHandler(base.BaseHandler):
    def get(self):
        return self.write('success')
