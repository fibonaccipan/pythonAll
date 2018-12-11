# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver import ActionChains
import time
import sys


def init():
    print('=====init=====')
    driver = webdriver.Chrome('C:/Program Files (x86)/Google/Chrome/Application/chromedriver.exe')
    driver.get('https://passport.suning.com/ids/login?method=GET&loginTheme=b2c')
    time.sleep(2)
    driver.maximize_window()
    return driver


def do_login(driver,name_pwd):
    print('=====do_login=====')
    # 切换到账号登录tab
    driver.find_element_by_xpath('/html/body/div[2]/div/div/div[1]/a[2]').click()
    driver.find_element_by_id('userName').send_keys(name_pwd[0])
    driver.find_element_by_id('password').send_keys(name_pwd[1])
    # 获取活动模块
    button = driver.find_element_by_xpath('//*[@id="siller1_dt_child_content_containor"]/div[3]')
    action = ActionChains(driver)
    action.click_and_hold(button).perform()

    # 滑动模块
    x = 0
    while True:
        action.move_by_offset(xoffset=x, yoffset=0).perform()
        x += 50
        print(x)
        if x >= 274:
            break

    time.sleep(1)
    action.release().perform()

    # 点击登录按钮
    driver.find_element_by_xpath('//*[@id="submit"]').click()
    time.sleep(2)


def do_dk(driver):
    print('=====do_dk=====')
    # 点击我的易购按钮
    driver.find_element_by_xpath('/html/body/div[3]/div/div[2]/div[4]').click()
    time.sleep(1)

    # 输出当前窗口句柄（百度）
    # print(driver.current_window_handle)

    # 判断是否已打卡，是则直接关闭浏览器
    if driver.find_element_by_xpath(
            '//*[@id="ms-center"]/div/div/div[2]/div[1]/div[2]/div[1]/div[3]/a/span').text == '已打卡':
        print('已打卡')
        driver.close()
        driver.quit()
    else:
        # 点击打卡按钮
        driver.find_element_by_xpath('//*[@id="ms-center"]/div/div/div[2]/div[1]/div[2]/div[1]/div[3]/a').click()

        handles = driver.window_handles  # 获取当前窗口句柄集合（列表类型）
        # 切换到新开窗口
        driver.switch_to_window(handles[-1])
        time.sleep(2)
        # 点击开始打卡按钮
        driver.find_element_by_xpath('/html/body/div[4]/div/div[2]/div/div[1]/div[2]/div[1]/div/div[1]/div[2]').click()
        time.sleep(5)
        driver.close()
        driver.quit()
        print('=====打卡成功！=====')


if __name__ == '__main__':
    if len(sys.argv) != 3:
        print('请输入用户名和密码！')
    else:
        dr = init()
        do_login(dr, sys.argv[1::])
        do_dk(dr)

# /html/body/div[2]/div[6]/div[2]/div[5]/div[8]/ul/li[1]/div[2]/div[6]/span[2]
# /html/body/div[2]/div[6]/div[2]/div[5]/div[8]/ul/li[1]/div[2]/div[6]/span[2]
# /html/body/div[2]/div[6]/div[2]/div[5]/div[8]/ul/li[1]/div[2]/div[6]/span[2]