# -*- coding: utf-8 -*-
"""
Created on Tue Jan 23 21:11:39 2024

@author: Turzo
"""
from selenium.webdriver.common.by import By

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.login_icon = (By.XPATH, '//*[@id="app-wrapper"]/div[1]/div[2]/div/nav/div/ul[2]/li[2]/div/a')
        self.login_by_email = (By.XPATH, '/html/body/div[3]/div/div/div/div[2]/div[2]/div/div[6]/button')
        self.signup = (By.XPATH, '/html/body/div[3]/div/div/div/div[2]/div[2]/div[1]/button[2]')
        self.username = (By.ID, 'input_name')
        self.email = (By.ID, 'input_email')
        self.password = (By.ID, 'input_password')
        self.confirm_password = (By.ID, 'input_password-confirm')
        self.submit_button = (By.XPATH, '/html/body/div[3]/div/div/div/div[2]/div[2]/div/form/div[2]/div')
        self.login = (By.XPATH, '/html/body/div[3]/div/div/div/div[2]/div[2]/div[1]/form/div[2]/div/button')
        
    def click_login_icon(self):
        self.driver.find_element(*self.login_icon).click()
    def click_email(self):
        self.driver.find_element(*self.login_by_email).click()
    def click_signup(self):
        self.driver.find_element(*self.signup).click()
    def enter_username(self, username):
        self.driver.find_element(*self.username).send_keys(username)
    def enter_email(self, email):
        self.driver.find_element(*self.email).send_keys(email)
    def enter_password(self, password):
        self.driver.find_element(*self.password).send_keys(password)
    def confirm_key(self, key):
        self.driver.find_element(*self.confirm_password).send_keys(key)
    def click_submit(self):
        self.driver.find_element(*self.submit_button).click()
    def click_login(self):
        self.driver.find_element(*self.login).click()