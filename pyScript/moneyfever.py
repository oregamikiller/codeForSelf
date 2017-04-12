#!/usr/bin/env python
# -*- coding: utf-8 -*-
import urllib
import urllib2
from uiautomator import Device
import time
import json


def getback(d=Device()):
    d.press.back()
    d.press.back()
    d.press.back()
    d.press.back()
    d.press.back()
    d.press.home()

def moneyrun(account='', msg=''):
    print "start...."
    d = Device('1ebf31e4')
    xml = d.dump()
    print xml
    time.sleep(2)
    while d.screen == "off":
        print "off"
        d.screen.on()
        time.sleep(2)
        d.swipe(200, 500, 200, 100, steps=10)
        # d.swipe(1000,640,100,640,steps=10)
        time.sleep(2)
        # print d.info
    print d.info
    # d.swipe(200, 500, 200, 100, steps=10)
    # d.press.home()
    # time.sleep(1)
    # d.swipe(200, 800, 650, 800, steps=10)
    # time.sleep(1)
    while not d(text=u'手机京东').exists:
        d.press.home()
        time.sleep(1)
        # d.swipe(200, 800, 650, 800, steps=10)
        time.sleep(1)
        print u'机京东不存在'
    d(text=u'手机京东').click()
    time.sleep(3)
    # d.swipe(200, 600, 550, 600, steps=100)
    if d(text=u'领京豆').exists:
        d(text=u'领京豆').click()
        time.sleep(3)
        print d.dump()
        d.click(625, 260)

    time.sleep(4)
    # getback(d)
    return 1

moneyrun()
# try:
#     while True:
#         moneyrun()
# except Exception, e:
#     print e
