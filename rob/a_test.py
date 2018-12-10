from selenium import webdriver
import time


def main():
    # b = webdriver.Chrome()
    # b.get("http://www.baidu.com/")
    # time.sleep(5)
    # b.quit()
    browser = webdriver.Chrome()
    browser.get("http://www.baidu.com")
    print(browser.page_source)
    time.sleep(15)
    browser.close()


if __name__ == '__main__':
    main()
