import logging
import os

def log(msg):
    logPath = os.getcwd() + '/logs'
    if not os.path.exists(logPath):
        os.mkdir(logPath, 0775)
    logging.basicConfig(level = logging.DEBUG,
                        format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                        datefmt='%a, %d %b %Y %H:%M:%S',
                        filename=logPath + '/command.log',
                        filemode='w')
    logging.error(msg)

