
from Utilities import test_base
import time


def login(driver, url, username, password):
	try:
		test_base.open_url(driver, url)
		test_base.maximize_window(driver)
		test_base.send_keys(driver, "LP_txtbx_username", username)
		test_base.send_keys(driver, "LP_txtbx_password", password)
		test_base.click(driver, "LP_btn_submit")
		time.sleep(5)

		if driver.current_url == 'https://www.linkedin.com/feed/':
			return True
		else:
			test_base.get_text(driver, "LP_txt_invalid_login") == "There were one or more errors in your submission. "
			return False
	except Exception as e:
		print("login | Exp Desc: ", e)
