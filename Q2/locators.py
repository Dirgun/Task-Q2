# -*- coding: utf-8 -*-
"""
Created on Thu Feb  1 13:57:32 2024

@author: Turzo
"""

from selenium.webdriver.common.by import By

class Locators:    
    def __init__(self, driver):
        self.driver = driver
        self.logo = (By.XPATH, '//*[@id="app-wrapper"]/div[1]/div[2]/div/nav/div/ul[1]/li[1]/div/a')
        self.search_box = (By.NAME, 'query')
        self.search_button = (By.XPATH, '//*[@id="app-wrapper"]/div[1]/div[3]/div[2]/div/div/form/div/button')
        self.electronics = (By.XPATH, '//*[@id="app-wrapper"]/div[1]/div[3]/div[4]/ul/li[10]/a')
        self.vehicles = (By.XPATH, '//*[@id="app-wrapper"]/div[1]/div[3]/div[4]/ul/li[3]/a')
        self.mobiles = (By.XPATH, '//*[@id="app-wrapper"]/div[1]/div[3]/div[4]/ul/li[1]/a')
        self.product = (By.TAG_NAME, 'h2')
        self.item = (By.XPATH, '//*[@id="app-wrapper"]/div[1]/div[3]/div/div[2]/div[3]/div[2]/div/div[1]/div[1]/ul/li[1]/a')
        self.all_ads = (By.XPATH, '//*[@id="app-wrapper"]/div[1]/div[2]/div/nav/div/ul[1]/li[2]/a')
        self.sort = (By.ID, 'dd-button')
        self.sort_options = (By.ID, 'price_desc')
        self.filter_urgent = (By.XPATH, '//*[@id="app-wrapper"]/div[1]/div[3]/div/div[2]/div[2]/div/div[2]/div[2]/div/label/span[1]')
        self.filter_featured = (By.XPATH, '//*[@id="app-wrapper"]/div[1]/div[3]/div/div[2]/div[2]/div/div[2]/div[3]/div/label/span[1]')
        self.chat = (By.XPATH, '//*[@id="app-wrapper"]/div[1]/div[2]/div[2]/div[3]/div[2]/div/div[2]/div/div/div[1]/div[2]/div[2]/button')
        self.inbox = (By.ID, 'input_2')
        self.button = (By.ID, 'sendChatButton')
        self.forgot_pass = (By.XPATH,'/html/body/div[3]/div/div/div/div[2]/div[2]/div[1]/button[1]')
        self.submit_button = (By.XPATH, '/html/body/div[3]/div/div/div/div[2]/div/div/form/div[2]/div/button')
        self.location = (By.XPATH, '//*[@id="app-wrapper"]/div[1]/div[3]/div/div[2]/div[1]/div/div/div[2]/div[1]/div/button')
        self.select_loc = (By.XPATH, '/html/body/div[4]/div/div/div/div[2]/div/div/div/div[2]/div/ul/li[2]/button/div/div[1]')
        self.select_loc2 = (By.XPATH, '/html/body/div[4]/div/div/div/div[2]/div/div[2]/div/div[2]/ul/li[3]/button/div/div')
        self.category = (By.XPATH, '//*[@id="app-wrapper"]/div[1]/div[3]/div/div[2]/div[1]/div/div/div[2]/div[2]/div/div[2]/button')
        self.select_cat = (By.XPATH, '/html/body/div[5]/div/div/div/div[2]/div/div/div/ul/li[2]/button/div/div[1]')
        self.select_cat2 = (By.XPATH, '/html/body/div[5]/div/div/div/div[2]/div/div[2]/div/ul/li[2]/button/div/div')
        self.element = (By.XPATH, '//*[@id="app-wrapper"]/div[1]/div[3]/div/div[2]/div[3]/div[2]/div/div[1]/div[1]/ul/li[3]/a/div/div[2]/h2')
        self.save_ad = (By.XPATH, '//*[@id="app-wrapper"]/div[1]/div[2]/div[2]/div[3]/div[1]/div[2]/div/div[2]/button/div[2]')
        self.my_account = (By.LINK_TEXT, 'My account')
        self.favorites = (By.LINK_TEXT, 'Favorites')
        self.settings = (By.LINK_TEXT, 'Settings')
        self.button2 = (By.XPATH, '//*[@id="content"]/div[2]/form/div[1]/div[2]/div[1]/button')
        self.button3 = (By.XPATH, '//*[@id="content"]/div[2]/form/div[1]/div[3]/div[1]/button')
        self.update_info = (By.XPATH, '//*[@id="content"]/div[2]/form/div[2]/div/button')
        self.current_pass = (By.ID, 'input_current-password')
        self.new_pass = (By.ID, 'input_password')
        self.confirm_pass = (By.ID, 'input_password-confirm')
        self.change_pass = (By.XPATH, '//*[@id="content"]/div[2]/div[2]/form/div[2]/div/button')
        
    def LogoClick(self):
        self.driver.find_element(*self.logo).click()
    def SearchBox(self,search_term):
        self.driver.find_element(*self.search_box).send_keys(search_term)
    def SearchButton(self):
        self.driver.find_element(*self.search_button).click()
    def Electronics(self):
        self.driver.find_element(*self.electronics).click()
    def Vehicles(self):
        self.driver.find_element(*self.vehicles).click()
    def Mobiles(self):
        self.driver.find_element(*self.mobiles).click()
    def Product(self):
        self.driver.find_element(*self.product).click()
    def Item(self):
        self.driver.find_element(*self.item).click()
    def AllAds(self):
        self.driver.find_element(*self.all_ads).click()
    def Sort(self):
        self.driver.find_element(*self.sort).click()
    def SortOptions(self):
        self.driver.find_element(*self.sort_options).click()
    def FilterUrgent(self):
        self.driver.find_element(*self.filter_urgent).click()
    def FilterFeatured(self):
        self.driver.find_element(*self.filter_featured).click()
    def Chat(self):
        self.driver.find_element(*self.chat).click()
    def Inbox(self,message):
        self.driver.find_element(*self.inbox).send_keys(message)
    def Button(self):
        self.driver.find_element(*self.button).click()
    def ForgotPassword(self):
        self.driver.find_element(*self.forgot_pass).click()
    def SubmitButton(self):
        self.driver.find_element(*self.submit_button).click()
    def Location(self):
        self.driver.find_element(*self.location).click()
    def SelectLoc(self):
        self.driver.find_element(*self.select_loc).click()
    def SelectLoc2(self):
        self.driver.find_element(*self.select_loc2).click()
    def Category(self):
        self.driver.find_element(*self.category).click()
    def SelectCat(self):
        self.driver.find_element(*self.select_cat).click()
    def SelectCat2(self):
        self.driver.find_element(*self.select_cat2).click()
    def Element(self):
        self.driver.find_element(*self.element).click()
    def SaveAd(self):
        self.driver.find_element(*self.save_ad).click()
    def MyAccount(self):
        self.driver.find_element(*self.my_account).click()
    def Favorites(self):
        self.driver.find_element(*self.favorites).click()
    def Settings(self):
        self.driver.find_element(*self.settings).click()
    def Button2(self):
        self.driver.find_element(*self.button2).click()
    def Button3(self):
        self.driver.find_element(*self.button3).click()
    def UpdateInfo(self):
        self.driver.find_element(*self.update_info).click()
    def CurrentPass(self,password):
        self.driver.find_element(*self.current_pass).send_keys(password)
    def NewPass(self,password):
        self.driver.find_element(*self.new_pass).send_keys(password)
    def ConfirmPass(self,password):
        self.driver.find_element(*self.confirm_pass).send_keys(password)
    def ChangePass(self):
        self.driver.find_element(*self.change_pass).click()
    