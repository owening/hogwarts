#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：hogwarts 
@File ：test_playwight_demo
@IDE  ：PyCharm 
@Author ：Owen
@Date ：2023/8/11 15:09 
'''
import time


from playwright.sync_api import sync_playwright

def test_palywright():



    playwright = sync_playwright().start()

    browser = playwright.chromium.launch(headless=False,slow_mo=1000,args=['--start-maximized'])
    # 实例化一个新的context
    context = browser.new_context()
    # 设置trace的参数信息
    context.tracing.start(screenshots=True, snapshots=True, sources=True)
    # 使用context生成的page实例进行对应的操作
    page = context.new_page()
    page.goto("https://www.baidu.com")
    # page.locator("[name='wd']").fill("selenium")
    page.fill("[name='wd']","selenium")
    # page.locator("#su").click()
    page.click("#su")
    # page.wait_for_timeout(2000)
    page.click("//*[@id='s_tab']/div/a[2]")
    # page.locator("//*[@id='s_tab']/div/a[2]",).click()
    result = page.inner_text("//*[@id='pagelet_frs-header/pagelet/head']/div/div[3]/div[2]/div[2]/div[2]/a")
    # str = page.locator("//*[@id='pagelet_frs-header/pagelet/head']/div/div[3]/div[2]/div[2]/div[2]/a").inner_text()
    # page.wait_for_timeout(2000)
    # 结束追踪
    context.tracing.stop(path="trace.zip")
    browser.close()
    assert result == "selenium吧"


