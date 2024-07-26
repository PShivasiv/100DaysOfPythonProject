from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrom_option = webdriver.ChromeOptions()
chrom_option.add_experimental_option("detach",True)

driver = webdriver.Chrome(options=chrom_option)
driver.get("http://secure-retreat-92358.herokuapp.com/")

name = driver.find_element(By.NAME ,value="fName")
name.send_keys("P")

lname = driver.find_element(By.NAME,value="lName")
lname.send_keys("shiva")

email = driver.find_element(By.NAME,value="email")
email.send_keys("siv23shiva@gmail.com")

login = driver.find_element(By.CSS_SELECTOR,value=".form-signin button")
login.click()

