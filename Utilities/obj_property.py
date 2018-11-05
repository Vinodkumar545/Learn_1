__author__ = 'Vinodkumar Kouthal'

"""
###############################################################################################################
This python class/function is built to retrieve locator type and value of an webelement.
locator() functions reads .ini object repository file and below is the standard syntax to be followed:
web_element_name = locator_type:>:locator_value
E.g.,   
	- login_page_btn_username = xpath:>://input[@id='username']
	- login_page_btn_password = id:>:password
It means, 
	- web_element_name this string needs to be passed as an argument to function locator(obj_value)
	- locator_type helps to navigate through element using xpath/id/name/css/classname/linktext/partiallinktext
	- :>: helps to differentiate between locator_type and locator_value
	- locator_value tells the address of the web-element 
################################################################################################################
"""

from selenium.webdriver.common.by import By
import configparser

def locator(web_element_name):
	try:
		global web_element
		config = configparser.ConfigParser()
		config.read("/home/vinod/automation/learn/Utilities/obj_repo.ini") # ini file path
		for section in config.sections():
			for lines in config.items(section):
				if lines[0].lower() == web_element_name.lower():
					web_element = lines[1]

		locator_type = web_element.split(':>:')[0]
		locator_value = web_element.split(':>:')[1]

		if locator_type.strip().lower() == "id":
			return [By.ID, locator_value]
		elif locator_type.strip().lower() == "xpath":
			return [By.XPATH, locator_value]
		elif locator_type.strip().lower() == "linktext":
			return [By.LINK_TEXT, locator_value]
		elif locator_type.strip().lower() == "partiallinktext":
			return [By.PARTIAL_LINK_TEXT, locator_value]
		elif locator_type.strip().lower() == 'name':
			return [By.NAME, locator_value]
		elif locator_type.strip().lower() == "tagname":
			return [By.TAG_NAME, locator_value]
		elif locator_type.strip().lower() == "claasname":
			return [By.CLASS_NAME, locator_value]
		elif locator_type.strip().lower() == 'css':
			return [By.CSS_SELECTOR, locator_value]

	except Exception as e:
		print("Method locator | Exp Desc: ", e)
		assert False

