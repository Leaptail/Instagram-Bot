from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

def instalogin(name,passw):
    browser = webdriver.Firefox()
    browser.implicitly_wait(5)

    browser.get('https://www.instagram.com/') #types this website and hits enter

    sleep(2)

    username_input = browser.find_element(By.CSS_SELECTOR,"input[name='username']")
    password_input = browser.find_element(By.CSS_SELECTOR,"input[name='password']")

    username_input.send_keys(name)
    password_input.send_keys(passw)

    sleep(5)

    #clicks enter to get in
    submit = browser.find_element(By.TAG_NAME,'form')
    submit.submit()

    sleep(5)

    #save your login info?
    sleep(10)
    notnow = browser.find_element_by_xpath("//button[contains(text(), 'Not Now')]").click()
    #turn on notif
    sleep(10)
    notnow2 = browser.find_element_by_xpath("//button[contains(text(), 'Not Now')]").click()

def instaseeposts():

