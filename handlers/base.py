import tornado.web


class BaseHandler(tornado.web.RequestHandler):
    def render_string(self, template_name, **kwargs):
        kwargs['settings'] = self.settings
        return super(BaseHandler, self).render_string(template_name, **kwargs)
    
    def render(self, template_name, **kwargs):
        template_name = "%s/%s" % (self.settings['template_path'], template_name)
        return super(BaseHandler, self).render(template_name, **kwargs)
