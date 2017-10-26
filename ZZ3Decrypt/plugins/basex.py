#!/usr/bin/env python
#coding: utf-8

import base64
from common.log import Log
from common.iplugin import DecryptPlugin

logger=Log.getLogger('zz3.log')

class BaseX(DecryptPlugin):
    def __init__(self):
        self.name = 'Base系列(64,32,16)'
        self.desc = 'Base系列(64,32,16)'
        self.auth = '蔚蓝行'

    def decrypt(self,text,key=None):
        result_dict = {}
        try:
            rst_b64 = base64.b64decode(text)
        except:
            rst_b64 = ''

        try:
            rst_b32 = base64.b32decode(text)
        except:
            rst_b32 = ''

        try:
            rst_b16 = base64.b16decode(text)
        except:
            rst_b16 = ''

        return {
            'base64': rst_b64,
            'base32': rst_b32,
            'base16': rst_b16,
        }

if __name__ == '__main__':
    bx = BaseX()
    print bx.decrypt('c3VjY2Vzcw==')