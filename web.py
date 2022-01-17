from selenium import webdriver
from selenium.webdriver.common.by import By
import random
import time

web = webdriver.Chrome()
web.get("https://forms.gle/3XhnvjBVBM6xeJs17")
web.maximize_window()
time.sleep(1)

gender_range=random.randint(0,1)
age_range=random.randint(2,7)
check_range1=random.randint(0,2)
check_range2=random.randint(3,4)
drop_range=random.randint(0,3)

gender = web.find_elements(By.CLASS_NAME,"appsMaterialWizToggleRadiogroupOffRadio")
gender[gender_range].click()

time.sleep(1)

age = web.find_elements(By.CLASS_NAME,"appsMaterialWizToggleRadiogroupOffRadio")
age[age_range].click()
time.sleep(1)

check = web.find_elements(By.CLASS_NAME,"quantumWizTogglePapercheckboxInnerBox")
check[check_range1].click()
time.sleep(1)

check = web.find_elements(By.CLASS_NAME,"quantumWizTogglePapercheckboxInnerBox")
check[check_range2].click()
time.sleep(1)

drop = web.find_element(By.CLASS_NAME,"quantumWizMenuPaperselectOptionList")
drop.click()
time.sleep(2)


droplist = web.find_element(By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[2]/div[4]/span')
droplist.click()


