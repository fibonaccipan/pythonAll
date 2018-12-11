from selenium import webdriver
# from selenium.webdriver import A
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
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
    # driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/span')

    # 获取活动模块
    # button = driver.find_element_by_xpath('//*[@id="siller1_dt_child_content_containor"]/div[3]')
    button = driver.find_element_by_xpath('//*[@id="J_StaticForm_dt_child_content_containor"]/div[3]')

    action = ActionChains(driver)
    action.click_and_hold(button).perform()

    # 滑动模块
    x = 0
    y = 0
    while True:
        action.move_by_offset(xoffset=x, yoffset=y).perform()
        x += 20
        y += 1
        # action.move_by_offset(xoffset=x, yoffset=0).perform()
        print(x)
        time.sleep(0.1)
        if x >= 300:
            break

    # time.sleep(1)
    action.release(button).perform()
    # action.click_and_hold(button).perform()
    # action.release().perform()
    driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/span').click()
    # action.release().perform()
    time.sleep(6)

    # 点击登录按钮
    driver.find_element_by_xpath('//*[@id="submit"]').click()
    time.sleep(2)


def refreshAmount(driver):
    # driver.refresh()
    amnt = 1355
    j = 0
    # s =0
    while amnt > 300 and j < 1000:
        i = 0
        # flg = True
        # amntEmt = None
        while True:
            i = i+1
            try:
                sss = driver.find_element_by_xpath('/html/body/div[2]/div[6]/div[2]/div[5]/div[8]/ul/li[1]/div[2]/div[6]/span[2]')
                # flg = False
                print("inner try" + str(i) + "------")
                print(type(sss))
                print(sss.text)  # 拿到对象但是拿不到值
                try:
                    ppp:str = sss.text
                    amnt = int(ppp.split(".")[0])
                    print("0000000000000")
                    break
                except:
                    time.sleep(0.01)
                    print("++++++++++++++++++++++++++++++++++++")
                # break
            except:
                time.sleep(0.03)
                print("inner except" + str(i))
        # -------------------------------------------------------微调
        # time.sleep(1)
        # amntEmt = driver.find_element_by_xpath( '/html/body/div[2]/div[6]/div[2]/div[5]/div[8]/ul/li[1]/div[2]/div[6]/span[2]')
        # print("i = " + str(i))
        # pricestr: str = amntEmt.text
        # print(pricestr + "===========-=---=-=-=-=-=")
        # price = int(pricestr.split(".")[0])
        # print(price)
        if amnt < 300:
            print(str(amnt) + "==" + "yes")
            # action = Action()
            # driver.find_element_by_id('confirmPay').click()
            action = ActionChains(driver)
            action.send_keys("999999").perform()
            driver.find_element_by_id('confirmPay').click()
            break
        else:
            print(str(amnt) + "==" + "no")
            # driver.find_element_by_id('simplePassword').click()  # .send_keys("999999")
            # driver.find_element_by_xpath('//*[@id="simplePassword"]/li[1]').send_keys('9')
            # actions1 = ActionChains(driver)
            # actions1.send_keys("999999")
            action = ActionChains(driver)
            action.send_keys("999999").perform()
            # driver.find_element_by_id('confirmPay').click()
            # time.sleep(1000)
        print(str(amnt) + "6666666666666")
        # time.sleep(5)
        j = j+1
        driver.refresh()
        print("j = " + str(j))



if __name__ == '__main__':
    # if len(sys.argv) != 3:
    #     print('请输入用户名和密码！')
    # else:
    dr = init()
    do_login(dr, ['17778175326','eric------'])
    refreshAmount(dr)
    # js = 'window.open("https://payment.suning.com/epps-pppm/miniGateway/show.htm?payOrderId=1812114425382757584");'
    # dr2 = dr.execute_script(js)
    # dr

