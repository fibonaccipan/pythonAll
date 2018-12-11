from selenium import webdriver
from selenium.webdriver import ActionChains
import time
import sys
# https://blog.csdn.net/sanpic/article/details/81454478


def main():
    # b = webdriver.Chrome()
    # b.get("http://www.baidu.com/")
    # time.sleep(5)
    # b.quit()
    browser = webdriver.Chrome()
    browser.get("https://payment.suning.com/epps-pppm/miniGateway/show.htm?payOrderId=1812114425382595804")
    time.sleep(25)
    # print(browser.page_source)
    amntElement  = browser.find_element_by_class_name("num payment-item-pay-amount")
    print(amntElement)
    time.sleep(25)

    browser.close()


def init():
    print('=========init================')
    wd = webdriver.Chrome()
    wd.get('https://payment.suning.com/epps-pppm/miniGateway/show.htm?payOrderId=1812114425382757584')  # get  url
    wd.maximize_window()
    time.sleep(2)
    return wd


def do_login(driver,name_pwd):
    print('=====do_login=====')
    # 切换到账号登录tab
    driver.find_element_by_xpath('//*[@id="login-box"]/div[2]/a').click()
    driver.find_element_by_id('username').send_keys(name_pwd[0])
    driver.find_element_by_id('password').send_keys(name_pwd[1])

    driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/span').click()


    # 获取活动模块
    # button = driver.find_element_by_xpath('//*[@id="siller1_dt_child_content_containor"]/div[3]')
    button = driver.find_element_by_xpath('//*[@id="J_StaticForm_dt_child_content_containor"]/div[3]')

    action = ActionChains(driver)
    action.click_and_hold(button).perform()

    # # 滑动模块
    # x = 0
    # while True:
    #     action.move_by_offset(xoffset=x, yoffset=0).perform()
    #     x += 50
    #     print(x)
    #     time.sleep(0.1)
    #     if x >= 300:
    #         break
    #
    # time.sleep(1)
    # action.release().perform()
    time.sleep(10)

    # 点击登录按钮
    driver.find_element_by_xpath('//*[@id="submit"]').click()
    time.sleep(2)


def refreshAmount(driver):
    driver.refresh()
    amnt = 1355
    j = 0
    while amnt > 300 and j < 1:
        i = 0
        flg = True
        # amntEmt = None
        while flg:
            i = i+1
            # try:
            driver.find_element_by_xpath('/html/body/div[2]/div[6]/div[2]/div[5]/div[8]/ul/li[1]/div[2]/div[6]/span[2]')
            flg = False
            print("inner try" +str(i))
            # except :
            #     flg = True
            #     time.sleep(0.01)
            #     print("inner except" +str(i))


        # time.sleep(2)
        amntEmt = driver.find_element_by_xpath( '/html/body/div[2]/div[6]/div[2]/div[5]/div[8]/ul/li[1]/div[2]/div[6]/span[2]')
        print("i = " + str(i))
        # price = amntEmt.text
        # price = price.split(".")
        print(amntEmt.text)

        j = j+1
    print("j = " + str(j))



if __name__ == '__main__':
    # if len(sys.argv) != 3:
    #     print('请输入用户名和密码！')
    # else:
    dr = init()
    do_login(dr, ['17778175326','eric'])
    refreshAmount(dr)
    # js = 'window.open("https://payment.suning.com/epps-pppm/miniGateway/show.htm?payOrderId=1812114425382757584");'
    # dr2 = dr.execute_script(js)
    # dr

