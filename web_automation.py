from selenium import webdriver
import selenium
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


driver = webdriver.Chrome(executable_path=r'C:/Users/yashp/Desktop/Harvest/chromedriver_win32/chromedriver.exe')
driver.get('https://www.missingmoney.com/Main/Search.cfm')
firstName1 = driver.find_element_by_name("SearchFirstName")
LastName1 = driver.find_element_by_name("SearchLastName")
HomeState = driver.find_element_by_name("HomeState")
firstName1.send_keys('Maya')
LastName1.send_keys('Brooks')
HomeState.send_keys('NY')

go = driver.find_element_by_name('GO')
go.click()

City = driver.find_element_by_name('SearchCity')
City.send_keys('New York')

state = driver.find_element_by_name('SearchStateID')
for option in state.find_elements_by_tag_name('option'):
	if option.text == 'New York':
		option.click()
		break
go1 = driver.find_element_by_name('GO')
go1.click()


user = driver.find_element_by_id('rColor1')
link = user.find_element_by_tag_name('a')
link.click()

claim = driver.find_element_by_xpath("//input[@value='Yes I can Claim']")
claim.click()	

TextData =  driver.find_elements_by_class_name('TextData')
for i in TextData:
	if(len(i.find_elements_by_tag_name('a'))>0):
		i.find_element_by_tag_name('a').click()


