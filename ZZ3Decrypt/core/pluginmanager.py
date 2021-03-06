#!/usr/bin/env python
#coding: utf-8

import os
import sys
from imp import find_module
from imp import load_module
from common.log import Log

logger=Log.getLogger('zz3.log')

class PluginManager(type):
    #静态变量配置插件路径
    __PluginPath = os.path.realpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "../plugins/"))

    #调用时将插件注册
    def __init__(self,name,bases,dict):
        if not hasattr(self,'AllPlugins'):
            self.__AllPlugins = {}
        else:
            self.RegisterAllPlugin(self)

    #设置插件路径
    @staticmethod
    def SetPluginPath(path):
        if os.path.isdir(path):
            PluginManager.__PluginPath = path
        else:
            print '%s is not a valid path' % path

    #递归检测插件路径下的所有插件，并将它们存到内存中
    @staticmethod
    def LoadAllPlugin():
        pluginPath = PluginManager.__PluginPath
        if not os.path.isdir(pluginPath):
            raise EnvironmentError,'{0} is not a directory'.format(pluginPath)

        items = os.listdir(pluginPath)
        for item in items:
            if os.path.isdir(os.path.join(pluginPath,item)):
                PluginManager.__PluginPath = os.path.join(pluginPath,item)
                PluginManager.LoadAllPlugin()
            else:
                if item.endswith('.py') and item != '__init__.py':
                    moduleName = item[:-3]
                    if moduleName not in sys.modules:
                        fileHandle, filePath,dect = find_module(moduleName,[pluginPath])
                    try:
                        moduleObj = load_module(moduleName,fileHandle,filePath,dect)
                    finally:
                        if fileHandle : fileHandle.close()

    #返回所有的插件
    @property
    def AllPlugins(self):
        return self.__AllPlugins

    #注册插件
    def RegisterAllPlugin(self,aPlugin):
        pluginName = '.'.join([aPlugin.__module__,aPlugin.__name__])
        pluginObj = aPlugin()
        self.__AllPlugins[pluginName] = pluginObj

    #注销插件
    def UnregisterPlugin(self,pluginName):
        if pluginName in self.__AllPlugins:
            pluginObj = self.__AllPlugins[pluginName]
            del pluginObj

    #获取插件对象
    def GetPluginObject(self, pluginName = None):
        if pluginName is None:
            return self.__AllPlugins.values()
        else:
            result = self.__AllPlugins[pluginName] if pluginName in self.__AllPlugins else None
            return result

    #根据插件名字，获取插件对象（提供插件之间的通信）
    @staticmethod
    def GetPluginByName(pluginName):
        if pluginName is None:
            return None
        else:
            for SingleModel in __ALLMODEL__:
                plugin = SingleModel.GetPluginObject(pluginName)
                if plugin:
                    return plugin