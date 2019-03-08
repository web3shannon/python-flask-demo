import multiprocessing

bind = "127.0.0.1:18000"
workers = multiprocessing.cpu_count()
accesslog = 'access.log'
errorlog = 'error.log'
chdir = 'src'
pidfile = 'server.pid'