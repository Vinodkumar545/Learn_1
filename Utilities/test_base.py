from selenium import webdriver
from Utilities.obj_property import locator

def activate_driver(browser_name):
	try:
		if browser_name.strip().lower() == 'chrome':
			driver = webdriver.Chrome()
			print("Chrome WebDriver is initialized.")
			return driver
	except Exception as e:
		print("activate_driver | Exp Desc: ", e)
		assert False
def open_url(driver, url):
	try:
		driver.get(url)
		print("Application URL: " + url + " is successfully opened.")
	except Exception as e:
		print("open_url | Exp Desc: ", e)
		assert False
def maximize_window(driver):
	try:
		driver.maximize_window()
		print("Browser window is now maixmized.")
	except Exception as e:
		print("maximize_window | Exp Desc: ", e)
		assert False
def click(driver, web_ele):
	try:
		driver.find_element(locator(web_ele)[0], locator(web_ele)[1]).click()
		print("Clicked on weblement " + web_ele + " successfully.")
	except Exception as e:
		print("click | Exp Desc: ", e)
		assert False
def send_keys(driver, web_ele, value):
	try:
		driver.find_element(locator(web_ele)[0], locator(web_ele)[1]).clear()
		driver.find_element(locator(web_ele)[0], locator(web_ele)[1]).send_keys(value)
		print("value " + value + " is successfully inputed into the " + web_ele + " field.")
	except Exception as e:
		print("send_keys | Exp Desc: ", e)
		assert False

def get_text(driver, web_ele):
	try:
		return driver.find_element(locator(web_ele)[0], locator(web_ele)[1]).text
	except Exception as e:
		print("get_text | Exp Desc: ", e)
