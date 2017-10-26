#!/usr/bin/env python
#coding: utf-8

import json
from pluginmanager import PluginManager
from common.zz3exception import PluginException
from common.log import Log

logger=Log.getLogger('zz3.log')


class DecryptPlugin(object):
    __metaclass__ = PluginManager

    def __init__(self):
        self.name = None      #插件名称
        self.desc = None      #插件描述
        self.auth = None      #插件作者

    #加密算法,需子类重写
    def encrypt(self,plain_text,key):
        raise PluginException('Not rewrite the encrypt() function.')

    #解密算法,需子类重写
    def decrypt(self,cipher_text,key):
        raise PluginException('Not rewrite the decrypt() function.')

    #检查子类是否符合规范
    def check_sub(self):
        if self.name is 'default':
            raise PluginException("Not set name.")
        if self.desc is None:
            raise PluginException("Not set desc.")
        if self.auth is None:
            raise PluginException("Not set auth.")

    #json输出
    def _output(self, out_data):
        out = {
            'name': self.name,
            'desc': self.desc,
            'out_data': out_data,
        }
        return json.dumps(out)

    #主方法
    def run(self,text,key=None,method='DECRYPT'):
        self.check_sub()
        if method.lower() == 'encrypt':
            out_data = self.encrypt(text,key)
        else:
            out_data = self.decrypt(text,key)
        return self._output(out_data)

__ALLMODEL__ = (DecryptPlugin,)

if __name__ == '__main__':
    dp = DecryptPlugin()
    print dp.run('明文')