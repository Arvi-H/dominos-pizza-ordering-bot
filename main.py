import time

# webdriver allows us to open up a web browser
from selenium import webdriver

# specify that the web browser we want is chrome
driver = webdriver.Chrome(r"/Users/arvihaxhillari/Downloads/chromedriver")

# open Dominos website on web browser
driver.get("https://www.dominos.com/")

# select featured combo deal
driver.find_element_by_xpath('/html/body/div[1]/main/section[2]/div[2]/div/div/div/div[3]/a').click()

# wait for the delivery element to load on screen
time.sleep(1) 
# select delivery
driver.find_element_by_xpath('/html/body/div[2]/div[3]/div/div/div[2]/form/div/div[1]/label[1]/span[1]').click()

time.sleep(9)
 
# change location as you wish
location = '1060 E Campus Dr'
zip_code = '84604'

driver.find_element_by_xpath('/html/body/div[2]/div[3]/div/div/div[2]/form/div/div[2]/fieldset/div[3]/div[3]/input').send_keys(location)
driver.find_element_by_xpath('/html/body/div[2]/div[3]/div/div/div[2]/form/div/div[2]/fieldset/div[3]/div[7]/div[1]/div/div/input').send_keys(zip_code)

