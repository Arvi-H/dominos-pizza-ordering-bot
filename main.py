# webdriver allows us to open up a web browser
from selenium import webdriver

# specify that the web browser we want is chrome
driver = webdriver.Chrome(r"/Users/arvihaxhillari/Downloads/chromedriver")

driver.get("https://arvih.com/")
my_resume = driver.find_element_by_id('resume-btn')
my_resume.click()