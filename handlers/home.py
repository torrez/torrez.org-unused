import base

class IndexHandler(base.BaseHandler):
    def get(self):
        return self.render('home/index.html')
        
class ProjectsHandler(base.BaseHandler):
    def get(self):
        return self.render('home/projects.html')
        
class DomainsHandler(base.BaseHandler):
    def get(self):
        return self.render('home/domains.html')        
        
class LocationHandler(base.BaseHandler):
    def get(self):
        return self.render('home/where-i-am.html')        