#!/usr/bin/env python
#coding: utf-8

import logging, os, sys
from config.conf import DEBUG

class Log(object):
    @staticmethod
    def getLogger(log_filename):
        logger=logging.getLogger()
        if log_filename == None:
            return logger
        else:
            logfile = os.path.join(os.path.dirname(__file__),"../logs/"+log_filename)
            handler=logging.FileHandler(logfile)
            datefmt="%y-%m-%d %H:%M:%S"
            formatter = logging.Formatter("%(asctime)s[%(process)d %(filename)s(%(funcName)s): %(lineno)d] %(levelname)s: %(message)s",datefmt)
            handler.setFormatter(formatter)
            logger.addHandler(handler)
            if DEBUG:
                logger.setLevel(logging.DEBUG)
            else:
                logger.setLevel(logging.INFO)
            return logger

if __name__ == '__main__':

    logger = Log.getLogger('test.log')
    logger.info('test')
