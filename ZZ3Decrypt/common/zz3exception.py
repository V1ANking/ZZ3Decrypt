#!/usr/bin/env python
#coding: utf-8

DESC_INFO = {
    50:'插件异常',
}

class ZZ3Exception(Exception):
    def __init__(self, message):
        super(ZZ3Exception, self).__init__(message)

class PluginException(ZZ3Exception):
    code = 50