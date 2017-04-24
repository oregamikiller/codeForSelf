#!/usr/bin/env python
# -*- coding: utf-8 -*-
import urllib
import urllib2
from uiautomator import Device
import time
import json
import sys  

reload(sys) 
sys.setdefaultencoding('utf-8')

def getback(d=Device()):
    d.press.back()
    d.press.back()
    d.press.back()
    d.press.back()
    d.press.back()
    d.press.home()

def moneyrun(device=None):
    print "start...."
    d = Device('1ebf31e4')
    time.sleep(2)
    while d.screen == "off":
        print "off"
        d.screen.on()
        time.sleep(4)
        d.swipe(300, 1000, 300, 400, steps=10)
        time.sleep(4)
    print d.info
    # d.swipe(200, 500, 200, 100, steps=10)
    # d.press.home()
    # time.sleep(1)
    # d.swipe(200, 800, 650, 800, steps=10)
    # time.sleep(1)
    while not d(text=u'手机京东').exists:
        d.press.home()
        time.sleep(1)
        d.swipe(300, 1000, 300, 400, steps=10)
        time.sleep(1)
        print u'手机京东不存在'
    d(text=u'手机京东').click()
    time.sleep(4)
    # d.swipe(200, 600, 550, 600, steps=100)
    if d(text=u'领京豆').exists:
        d(text=u'领京豆').click()
        time.sleep(6)
        print d.dump()
        d.click(650, 260)
        time.sleep(4)
        d.click(530, 660)
        time.sleep(4)
        d.click(360, 960)

    time.sleep(4)
    getback(d)
    return 1

def jingdongFinance(device=None):
    print "start...."
    d = Device()
    time.sleep(2)
    while d.screen == "off":
        print "off"
        d.screen.on()
        time.sleep(2)
        d.swipe(200, 500, 200, 100, steps=10)
        time.sleep(2)
    while not d(text=u'京东金融').exists:
        d.press.home()
        time.sleep(2)
        print u'京东金融不存在'
    d(text=u'京东金融').click()
    time.sleep(15)
    if d(text=u'立即登录体验').exists:
        d(text=u'立即登录体验').click()
        time.sleep(5)
    if d(text=u'用其他账号登录').exists:
        d(text=u'用其他账号登录').click()
        time.sleep(5)
    if d(text=u'手机京东一键登录').exists:
        d(text=u'手机京东一键登录').click()
        time.sleep(10)
        d.click(350, 800)
    time.sleep(10)
    if d(text=u'白条可用额度').exists:
        d(text=u'白条可用额度').click()
        time.sleep(10)
    if d(text=u'1个提额包').exists:
        d(text=u'1个提额包').click()
        time.sleep(10)
    time.sleep(10)
    d.click(600, 1200)
    time.sleep(8)
    d.click(630, 450)
    time.sleep(8)
    getback(d)
    return 1

# moneyrun()
jingdongFinance()

#jingdongFinance()
# try:
#     while True:
#         moneyrun()
# except Exception, e:
#     print e
