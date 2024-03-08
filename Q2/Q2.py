# -*- coding: utf-8 -*-
"""
Created on Tue Jan 23 21:11:39 2024

@author: Turzo
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from login_page import LoginPage
from locators import Locators
import imaplib
import email
from email.header import decode_header
import time
import requests
import random
import re

path_to_chromedriver = 'C:\\Users\ASUS\OneDrive\Desktop\Q2\chromedriver.exe'
service = Service(path_to_chromedriver)
driver = webdriver.Chrome(service=service)

def test_home_page_load():
    driver.get('https://bikroy.com/en')
    time.sleep(3)
    assert driver.title == 'Bikroy - Electronics, Cars, Property and Jobs in Bangladesh', "Home page did not load successfully"
    driver.quit()
    
def test_logo_redirect():
    locators = Locators(driver)
    driver.get('https://bikroy.com/en')
    time.sleep(3)
    locators.LogoClick()
    time.sleep(3)
    if driver.current_url == "https://bikroy.com/en":
        print("Test passed: The logo redirects to the home page.")
    else:
        print("Test failed: The logo does not redirect to the home page.")

    driver.quit()
    
def test_search_functionality():
    locators = Locators(driver)
    driver.get('https://bikroy.com/en')
    search_term = 'Laptop'

    locators.SearchBox(search_term)
    locators.SearchButton()

    title = driver.title
    
    if search_term in title:
        print('Search functionality is working')
    else:
        print("Search functionality did not work for search term '{search_term}'")

    driver.quit()

def test_search_no_results():
    locators = Locators(driver)
    driver.get('https://bikroy.com/en')
    locators.SearchBox('flxkdfuv')
    locators.SearchButton()

    no_results_message = "No results found" in driver.page_source
    print(f"Test result: {no_results_message}")

    driver.quit() 

def test_homepage_links():
    driver.get('https://bikroy.com/en')
    links = driver.find_elements(By.TAG_NAME, 'a')

    for link in links:
        url = link.get_attribute('href')
        print(url)
        response = requests.get(url)
        assert response.status_code == 200, f'Broken link: {url}'

    driver.quit()

def test_product_listings():
    locators = Locators(driver)
    driver.get('https://bikroy.com/en')
    locators.Mobiles()
    time.sleep(8)
    names =  WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CLASS_NAME, "content--3JNQz")))
    text_format_names = [name.text for name in names]
    split_list = [s.split('\n') for s in text_format_names]
    
    for item in split_list:
        print(item)

    driver.quit()

def test_product_link():
    locators = Locators(driver)
    driver.get('https://bikroy.com/en')
    locators.Electronics()
    locators.Product()
    
    product_id = driver.find_element(By.TAG_NAME, 'h1').text
    
    if product_id in driver.title:
        print('Product page is correct')
    else:
        print('Incorrect product detail page')
        
    driver.quit()
    
def test_product_details():
    locators = Locators(driver)
    driver.get('https://bikroy.com/en')
    locators.Vehicles()
    locators.Item()
    
    product_name = driver.find_element(By.XPATH, '//*[@id="app-wrapper"]/div[1]/div[2]/div[2]/div[3]/div[1]/div[1]/div/h1').text
    product_price = driver.find_element(By.XPATH, '//*[@id="app-wrapper"]/div[1]/div[2]/div[2]/div[3]/div[2]/div/div[1]/div/div[2]/div[1]/div/div[1]').text
    product_description = driver.find_element(By.XPATH, '//*[@id="collapsible-content-0"]/ul/div').text
    product_seller = driver.find_element(By.XPATH, '//*[@id="app-wrapper"]/div[1]/div[2]/div[2]/div[3]/div[2]/div/div[2]/div/div/div[1]/div[1]/div/div/div/div/div').text

    print(product_name)
    print(product_price)
    print(product_description)
    print(product_seller)

    # Check that the product details are not empty
    assert product_name, 'Product name is missing'
    assert product_price, 'Product price is missing'
    assert product_description, 'Product description is missing'
    assert product_seller, 'Product seller information is missing'

def test_user_registration():
    driver.get('https://bikroy.com/en')
   
    login_page = LoginPage(driver)
    login_page.click_login_icon()
    time.sleep(3)
    login_page.click_email()
    time.sleep(3)
    login_page.click_signup()
    login_page.enter_username('testuser')
    login_page.enter_email('hulkhogan64@gmail.com')
    login_page.enter_password('123456789')
    login_page.confirm_key('123456789')
    login_page.click_login()
    time.sleep(3)
    
    account = driver.find_element(By.XPATH, '//*[@id="app-wrapper"]/div[1]/div[2]/div/nav/div/ul[2]/li[2]/div/a').text
    if account == 'Login':
        print('Registration Unsucessful')
    elif account == 'My account':
        print('Registration Successful')
    
def test_confirm_password():
    driver.get('https://bikroy.com/en')
    login_page = LoginPage(driver)
    login_page.click_login_icon()
    time.sleep(3)
    login_page.click_email()
    time.sleep(3)
    login_page.click_signup()
    login_page.enter_username('testuser')
    login_page.enter_email('howdydoo810@gmail.com')
    login_page.enter_password('123456789')
    login_page.confirm_key('1234567890')
    check_message = driver.find_element(By.XPATH, '/html/body/div[3]/div/div/div/div[2]/div[2]/div[1]/form/div[1]/div[4]/div[2]').text
    assert "Passwords do not match" in check_message
    print(check_message)
    driver.quit()
    
    
def test_existing_user_registration():
    driver.get('https://bikroy.com/en')
    login_page = LoginPage(driver)
    login_page.click_login_icon()
    time.sleep(3)
    login_page.click_email()
    time.sleep(3)
    login_page.click_signup()
    login_page.enter_username('testuser')
    login_page.enter_email('howdydoo810@gmail.com')
    login_page.enter_password('123456789')
    login_page.confirm_key('123456789')
    login_page.click_submit()
    time.sleep(3)
    error_message = driver.find_element(By.XPATH, '/html/body/div[3]/div/div/div/div[2]/div[2]/div[1]/div[1]')
    print(error_message.text)
    
def test_user_login():
    driver.get('https://bikroy.com/en')
    login_page = LoginPage(driver)
    login_page.click_login_icon()
    time.sleep(3)
    login_page.click_email()
    time.sleep(3)
    login_page.enter_email('howdydoo810@gmail.com')
    login_page.enter_password('123456789')
    login_page.click_login()
    time.sleep(10)
    
    account = driver.find_element(By.XPATH, '//*[@id="app-wrapper"]/div[1]/div[2]/div/nav/div/ul[2]/li[2]/div/a').text
    if account == 'Login':
        print('Login Unsucessful')
    elif account == 'My account':
        print('Login Successful')
        
def test_user_logout():
    driver.get('https://bikroy.com/en')
    login_page = LoginPage(driver)
    locators = Locators(driver)
    login_page.click_login_icon()
    time.sleep(3)
    login_page.click_email()
    time.sleep(3)
    login_page.enter_email('howdydoo810@gmail.com')
    login_page.enter_password('123456789')
    login_page.click_login()
    time.sleep(10)
    locators.MyAccount()
    time.sleep(3)
    locators.Settings()
    time.sleep(3)
    logout = driver.find_element(By.XPATH, '//*[@id="content"]/div[2]/div[3]/button[2]')
    driver.execute_script("arguments[0].scrollIntoView();", logout)
    logout.click()
    
    account = driver.find_element(By.XPATH, '//*[@id="app-wrapper"]/div[1]/div[2]/div/nav/div/ul[2]/li[2]/div/a').text
    if account == 'Login':
        print('Logout Sucessful')
    elif account == 'My account':
        print('Logout unsuccessful')
        
        
def test_sort():
    locators = Locators(driver)
    driver.get('https://bikroy.com/en')
    locators.AllAds()
    time.sleep(3)
    locators.Sort()
    locators.SortOptions()
    
    prices =  WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'price--3SnqI')))
    text_format_prices = [price.text for price in prices]
    split_list = [s.split('\n') for s in text_format_prices]
    
    for _ in range(5):
        split_list.pop(0)

    numbers = [int(re.sub(r'\D', '', item[0])) for item in split_list]
    
    is_sorted = numbers == sorted(numbers, reverse=True)
    if is_sorted == True:
        print('The items are sorted')
    
    
def test_forgot_password():
    driver.get('https://bikroy.com/en')
    locators = Locators(driver)
    login_page = LoginPage(driver)
    login_page.click_login_icon()
    time.sleep(3)
    login_page.click_email()
    time.sleep(3)
    locators.ForgotPassword()
    login_page.enter_email('howdydoo810@gmail.com')
    locators.SubmitButton()
    time.sleep(5)
    # Connecting to the email server
    mail = imaplib.IMAP4_SSL("imap.gmail.com")
    
    # Login to the email account
    mail.login('howdydoo810@gmail.com', 'uwyn spmm shai ycts')
    
    #select the mailbox(Inbox) you're interested in
    mailbox = "INBOX"
    mail.select(mailbox)
    
    # Search for specific mail
    resp, items = mail.search(None, '(FROM "support@bikroy.com" SUBJECT "How to reset your Bikroy password")')
    items = items[0].split()
    
    # Get the latest email
    latest = items[-1]
    
    # Get the raw content of the email
    resp, msg = mail.fetch(latest, "(BODY[])")
    raw = msg[0][1]
    
    # Parse the raw email into a readable object
    email_message = email.message_from_bytes(raw)
    
    # Get the subject of the email
    subject = decode_header(email_message['Subject'])[0][0]
    
    # Print the subject
    print('Email Recevied, Subject:', subject)

def test_send_message():
    driver.get('https://bikroy.com/en')
    locators = Locators(driver)
    login_page = LoginPage(driver)
    login_page.click_login_icon()
    time.sleep(3)
    login_page.click_email()
    time.sleep(3)
    login_page.enter_email('howdydoo810@gmail.com')
    login_page.enter_password('123456789')
    login_page.click_login()
    time.sleep(8)
    locators.AllAds()
    time.sleep(3)
    locators.Item()
    locators.Chat()
    time.sleep(5)
    locators.Inbox('This is a test message')
    locators.Button()
    time.sleep(20)
    message = driver.find_element(By.XPATH, '/html/body/div[4]/div/div/div/div[2]/div/div/div/div[1]/ul/li[1]/div/div[1]').text
    print(message)
    

def test_filter():
    driver.get('https://bikroy.com/en')
    locators = Locators(driver)
    locators.AllAds()
    time.sleep(3)
    locators.Location()
    time.sleep(3)
    locators.SelectLoc()
    time.sleep(5)
    locators.SelectLoc2()
    time.sleep(3)
    locators.Category()
    time.sleep(3)
    locators.SelectCat()
    time.sleep(3)
    locators.SelectCat2()
    elements = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CLASS_NAME, "description--2-ez3")))
    text_format_elements = [element.text for element in elements]
    keyword = 'Chattogram, Mobile Phones'
    if keyword in text_format_elements:
        print('Filtered results are correct')
    else:
        print('Results not filtered correctly')

    
def test_fav():
    driver.get('https://bikroy.com/en')
    login_page = LoginPage(driver)
    locators = Locators(driver)
    login_page.click_login_icon()
    time.sleep(3)
    login_page.click_email()
    time.sleep(3)
    login_page.enter_email('howdydoo810@gmail.com')
    login_page.enter_password('123456789')
    login_page.click_login()
    time.sleep(10)
    locators.AllAds()
    time.sleep(3)
    locators.Element()
    locators.SaveAd()
    element = driver.find_element(By.XPATH, '//*[@id="app-wrapper"]/div[1]/div[2]/div[2]/div[3]/div[1]/div[1]/div/h1').text
    locators.MyAccount()
    time.sleep(3)
    locators.Favorites()
    elements = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CLASS_NAME, "heading--2eONR")))
    text_format_elements = [element.text for element in elements]
    if element in text_format_elements:
        print('Item added to favorites')
    else:
        print('Item not found in favorites')


def test_update_info():
    driver.get('https://bikroy.com/en')
    login_page = LoginPage(driver)
    locators = Locators(driver)
    login_page.click_login_icon()
    time.sleep(3)
    login_page.click_email()
    time.sleep(3)
    login_page.enter_email('howdydoo810@gmail.com')
    login_page.enter_password('123456789')
    login_page.click_login()
    time.sleep(10)
    locators.MyAccount()
    time.sleep(3)
    locators.Settings()
    time.sleep(3)
    
    # Locate the button element
    locators.Button2()
    time.sleep(3)
    # Generate a random number between 0 and 18
    random_number1 = random.randint(0, 18)
    # Update your locator with the random number
    locator1 = f"downshift-0-item-{random_number1}"
    # Use WebDriverWait to wait for the presence of element with the updated locator
    location = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, locator1)))
    location.click()
    
    locators.Button3()
    options = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, '//*[@id="downshift-1-menu"]/ul')))
    text_format_options = [option.text for option in options]
    new_list = text_format_options[0].split('\n')
    item_count = len(new_list)-1
    random_number2 = random.randint(0, item_count)
    time.sleep(3)
    locator2 = f"downshift-1-item-{random_number2}"
    sublocation = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, locator2)))
    sublocation.click()
    locators.UpdateInfo()
    time.sleep(2)
    success_message = driver.find_element(By.XPATH, '//*[@id="content"]/div[1]/div/div')
    print(success_message.text)
    
def test_change_password():
    driver.get('https://bikroy.com/en')
    login_page = LoginPage(driver)
    locators = Locators(driver)
    old_pass = '123456789'
    new_pass = '22334455'
    login_page.click_login_icon()
    time.sleep(3)
    login_page.click_email()
    time.sleep(3)
    login_page.enter_email('howdydoo810@gmail.com')
    login_page.enter_password(old_pass)
    login_page.click_login()
    time.sleep(10)
    locators.MyAccount()
    time.sleep(3)
    locators.Settings()
    time.sleep(3)
    locators.CurrentPass(old_pass)
    locators.NewPass(new_pass)
    locators.ConfirmPass(new_pass)
    locators.ChangePass()
    message = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, '//*[@id="content"]/div[1]/div/div')))
    print(message.text)







#test_change_password()
#test_update_info()
#test_fav()
#test_filter()
#test_sort()
#test_send_message()
#test_logo_redirect() 
#test_forgot_password()
#test_confirm_password()
#test_search_no_results()
#test_user_logout()
#test_user_login()
#test_existing_user_registration()
#test_user_registration()
#test_product_details() 
#test_product_link()    
#test_product_listings()
#test_homepage_links()
#test_home_page_load()
#test_search_functionality()