import handlers.home
import handlers.misc

routes = [
    (r'/', handlers.home.IndexHandler),
    (r'/new', handlers.home.NewIndexHandler),
    (r'/projects', handlers.home.ProjectsHandler),
    (r'/domains', handlers.home.DomainsHandler),
    (r'/where-i-am', handlers.home.LocationHandler),
    (r'/uptime.txt', handlers.misc.UptimeHandler),
    (r'/conference', handlers.home.ConferenceHandler),
    (r'/projects/xumouse.shtml', handlers.misc.XuMouseHandler),
    (r'/project/XuMouse.zip', handlers.misc.XuMouseDownloadHandler)
]