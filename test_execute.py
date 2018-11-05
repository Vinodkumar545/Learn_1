from Utilities import test_base
from POM import login_page
import pytest

BROWSER = 'Chrome'
URL = "https://www.linkedin.com/"

@pytest.fixture(scope='function')
def driver():
	return test_base.activate_driver(BROWSER)

def test_001_login_with_right_credential(driver):
	assert login_page.login(driver, URL, "right_email_id", "right_password") is True


def test_002_login_with_incorrect_credential(driver):
	assert login_page.login(driver, URL, "right_email_id", "incorrect_password") is False
