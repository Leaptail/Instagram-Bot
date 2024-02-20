from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

#i wonder how this works
browser = webdriver.Firefox()
browser.implicitly_wait(5)

browser.get('https://www.instagram.com/') #types this website and hits enter

sleep(2)

username_input = browser.find_element(By.CSS_SELECTOR,"input[name='username']")
password_input = browser.find_element(By.CSS_SELECTOR,"input[name='password']")

username_input.send_keys("AdiyaaisLive@gmail.com")
password_input.send_keys("Wanttoevolvefurther")

sleep(5)

#clicks enter to get in
submit = browser.find_element(By.TAG_NAME,'form')
submit.submit()

#login_link = browser.find_element(By.XPATH, "//button[text()='Log in']") 
#there are a few other methods we can use
#login_link.click()


sleep(5)

browser.close()

