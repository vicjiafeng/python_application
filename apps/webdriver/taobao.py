#!/usr/bin/python
# coding:utf-8

from selenium import webdriver
import datetime
import time

browser = webdriver.Chrome()
browser.maximize_window()

def login():
    browser.get("http://www.taobao.com")
    time.sleep(3)
    if browser.find_element_by_link_text("亲，请登录"):
        browser.find_element_by_link_text("亲，请登录").click()
    print("请在15秒内完成扫码")
    time.sleep(15)
    browser.get("https://cart.taobao.com/cart.htm")
    time.sleep(3)
    if browser.find_element_by_id("J_SelectAll1"):
        browser.find_element_by_id("J_SelectAll1").click()

    now = datetime.datetime.now()
    print('login success:', now.strftime('%Y-%m-%d %H:%M:%S'))

def buy(buytime):
    while True:
        now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
    #对比时间，时间到就结算
        if now > buytime:
    #点击结算
            try:
                if browser.find_element_by_id("J_Go"):
                    browser.find_element_by_id("J_Go").click()
                browser.find_element_by_link_text('提交订单').click()
            except:
                time.sleep(0.1)
        print(now)
        time.sleep(0.005)

if __name__=="__main__":
    buytime = input("请输入抢购时间，格式如(2019-5-20 9:00:00.000000):")
    login()
    buy(buytime)
