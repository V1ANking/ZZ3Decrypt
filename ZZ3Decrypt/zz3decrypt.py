#!/usr/bin/env python
#coding: utf-8

import os

from common.log import Log
from core.iplugin import __ALLMODEL__
from core.pluginmanager import PluginManager

logger=Log.getLogger('zz3.log')

class ZZ3Decrypt(object):
    def __init__(self):
        self._plgsdir = os.path.realpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "plugins"))
        print self._plgsdir
    def get_plugin(self):
        pass

if __name__ == '__main__':
    #加载所有插件
    PluginManager.LoadAllPlugin()

    #遍历所有接入点下的所有插件
    for SingleModel in __ALLMODEL__:
        plugins = SingleModel.GetPluginObject()
        for item in plugins:
            #调用接入点的公共接口
            logger.info('调用插件{0}'.format(item.__class__))
            print item.run('c3VjY2Vzcw==')