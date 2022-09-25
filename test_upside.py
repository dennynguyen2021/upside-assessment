import pytest
import time

from appium import webdriver
#from appium.webdriver.common.appiumby import AppiumBy
from upside_client import UpsideClient

class TestUpside:
	@pytest.fixture(scope='class')
	def client(self):
		'''initial the client and driver '''
		self.driver = webdriver.Remote(UpsideClient.hub, UpsideClient.caps)
		self.driver.implicitly_wait(20)
		self.client = UpsideClient(self.driver)
		print(f'Client={self.client}')
		return self.client
	
	def test_login_with_negative_email(self,client):
		'''Verify login with username has no domain'''
		print('Verify login with username has no domain')
		username = 'emailnodomain'
		password = 'Test12345!'
		login_type = 'Continue with email'
		exp_attr = 'false'
		exp_text = 'Create account'
		
		print(f'username={username}, password={password}, login_type={login_type}, exp_attr={exp_attr} exp_text={exp_text}')
		actual_text,create_account_attr = client.login(username,password,login_type)
		assert create_account_attr == exp_attr,f'Actual attr={create_account_attr} is different than expected attr={exp_attr}'
		assert actual_text == exp_text,f'Actual text={actual_text} is different than expected text={exp_text}'

	
	def test_login_with_negative_password(self,client):
		'''Verify password without special char '''
		print('Verify password without special char')
		username = 'test@email.com'
		password = 'Test12345'
		login_type = 'Continue with email'
		exp_attr = 'false'
		exp_text = 'Create account'

		actual_text,create_account_attr = client.login(username,password,login_type)
		assert create_account_attr == exp_attr,f'Actual attr={create_account_attr} is different than expected attr={exp_attr}'
		assert actual_text == exp_text,f'Actual text={actual_text} is different than expected text={exp_text}'

	def test_positive_login(self,client):
		'''Verify valid username and password'''
		print('Verify valid username and password')
		username = 'test@email.com'
		password = 'Test12345!'
		login_type = 'Continue with email'
		exp_attr = 'true'
		exp_text = 'Account already\nexists'
		submit_button = True

		actual_text,create_account_attr = client.login(username,password,login_type,submit_button)
		assert create_account_attr == exp_attr,f'Actual attr={create_account_attr} is different than expected attr={exp_attr}'
		assert actual_text == exp_text,f'Actual text={actual_text} is different than expected text={exp_text}'
