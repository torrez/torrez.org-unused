import base

class NewIndexHandler(base.BaseHandler):
    def get(self):
        return self.render('home/index.html')

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

class ConferenceHandler(base.BaseHandler):
	def check_xsrf_cookie(self):
		pass

	def get(self):
		return self.post()

	def post(self):
		return self.render("home/conference.xml")