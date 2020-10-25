import urllib
import uuid

import urllib3
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

# from selenium.webdriver.support.select import Select
# from selenium.webdriver import ActionChains
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class buttonclick:
    def __init__(self,applno,dob):
        self.bot = webdriver.Chrome('chromedriver.exe')
        self.application_number = applno
        self.dob = dob


    def letsclick(self):
        bot = self.bot
        print("\nStarting clicking process!\n")
        bot.get('https://sarathi.parivahan.gov.in/sarathiservice/stateSelection.do')
        bot.implicitly_wait(10)
        # bot.maximize_window()

        # self.bot.find_element_by_xpath("//select[id='stfNameId']").click()
        # self.bot.

        select = Select(bot.find_element_by_id('stfNameId'))

        # select by visible text
        select.select_by_visible_text('Bihar')

        # select by value
        # select.select_by_value('1')

        bot.implicitly_wait(10)
        wait = WebDriverWait(bot, 10)
        but_loc = wait.until(EC.visibility_of_element_located(
            (By.XPATH, '//*[@id="navbarNavDropdown"]/ul/li[5]')))  # hover over button
        ActionChains(bot).move_to_element(but_loc).perform()
        sec_but = WebDriverWait(bot, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="navbarNavDropdown"]/ul/li[5]/ul/li[2]/a')))  # click on contact
        sec_but.click()

        bot.implicitly_wait(10)


        self.bot.find_element_by_xpath("//*[@id='dlslotipform']/div/div[1]/div/div[2]/div/div/div[2]/div/div[1]/div[1]/label").click()


        self.bot.find_element_by_xpath('//input[@id="applno"]').send_keys(self.application_number)
        bot.implicitly_wait(5)
        self.bot.find_element_by_xpath('//input[@id="dob"]').send_keys(self.dob)
        verification_code = str(input("Enter Captcha: "))
        self.bot.find_element_by_xpath('//input[@id="captcha"]').send_keys(verification_code)
        self.bot.find_element_by_xpath('//*[@id="dlslotipform_   SAVE   "]').click()


    def getInputFromGUI(self):
       print("create api")


    def letsclickNike(self):
        driver = webdriver.Chrome('chromedriver.exe')
        # driver.get("http://www.nike.com/us/en_us/c/men")
        # driver.maximize_window()
        #
        # wait = WebDriverWait(driver, 10)
        # actions = ActionChains(driver)
        #
        # # open men's hover menu in top nav bar
        # # men_menu = driver.find_element_by_css_selector("li[data-nav-tracking=men]")
        # # actions.move_to_element(men_menu).perform()
        #
        # # click shirt
        # wait.until(EC.visibility_of_element_located(
        #     (By.CSS_SELECTOR, "li[data-nav-tracking=men] a[data-subnav-label$=Shirts]"))).click()




print("Starting Application")


applno = str(input("Enter your Application Number(numberic form): "))
dob = str(input("Enter your DOB (DD/MM/YYYY): "))
bc = buttonclick(applno,dob)
bc.letsclick()
# bc.letsclickNike()