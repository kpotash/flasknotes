import logging
 
import time
 
 
 
class Logger(object):
 
 def __init__(self
              , logFilePath
              , logLevel=logging.INFO
              , consoleLevel=logging.WARNING):
 
     # ////////////////// LOGGING //////////////////
     self.logger = logging.getLogger()
     self.logger.setLevel(logLevel)
 
     formatter = logging.Formatter(
         "%(asctime)s %(process)d:%(thread)d %(levelname)s %(filename)s:%(lineno)d %(message)s")
 
 
 
     #======== add console handler ================
 
     sh = logging.StreamHandler()
 
     sh.setLevel(consoleLevel)
 
     sh.setFormatter(formatter)
 
     self.logger.addHandler(sh)
 
 
 
     #======== add file handler ===================
 
     fh = logging.FileHandler(filename=logFilePath
 
                              +time.strftime("%Y%m%d"))
 
     fh.setLevel(logLevel)
 
     fh.setFormatter(formatter)
 
     self.logger.addHandler(fh)
 
