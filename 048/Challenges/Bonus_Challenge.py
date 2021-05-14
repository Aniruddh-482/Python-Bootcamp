# Bonus Challenge: Practice using Selenium fill in this form and clicking Sign Up #

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

chrome_driver_path = "C:\Development\chromedriver.exe"
driver = webdriver.Chrome(chrome_driver_path)

driver.get("http://secure-retreat-92358.herokuapp.com/")

first_name = driver.find_element_by_name("fName")
first_name.send_keys("Aniruddh")

last_name = driver.find_element_by_name("lName")
last_name.send_keys("Upadhyay")

email = driver.find_element_by_name("email")
email.send_keys("aniruddhupadhyay07@gmail.com")

submit = driver.find_element_by_tag_name("form button")
submit.click()
