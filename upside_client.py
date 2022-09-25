
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy

import time

class UpsideClient:
	def __init__(self,driver):
		self.driver = driver
	
	app_name ='com.upside.consumer.android.beta'
	app_activity ='com.upside.consumer.android.activities.MainActivity'
	caps = {}
	caps["deviceName"] = "Android_Device"
	caps["platformName"] = "Android"
	caps["platformVersion"] = "13"
	caps["appPackage"] = app_name
	caps["appActivity"] = app_activity


	hub = "http://127.0.0.1:4723/wd/hub"

	def login(self,username,password,login_type, submit_button=False):		
		try:
			back_btn = self.driver.find_element(AppiumBy.ID,'sign_up_back_iv')
			print(f'back_btn={back_btn}')
			if back_btn is not None:
				print('inside back button')
				back_btn.click()

			back_btn2 = self.driver.find_element(AppiumBy.ID,'login_back_iv')
			if back_btn2 is not None:
				back_btn2.click()
		except:
			print('back button not found!')		
		
		signup_btn = self.driver.find_element(AppiumBy.ID,'sign_up_button')
		signup_btn.click()
		time.sleep(5)
		continue_email_btn = self.driver.find_elements(AppiumBy.ID,'sign_up_option_title')
		for i in continue_email_btn:
			if login_type in i.text:
				i.click();
		self.driver.find_element(AppiumBy.ID,'sign_up_email_edit_et').send_keys(username)
		self.driver.find_element(AppiumBy.ID,'sign_up_password_edit_et').send_keys(password)

		create_account_btn = self.driver.find_element(AppiumBy.ID,'action_button')
		create_account_attr = create_account_btn.get_attribute('clickable')
		print(f'create_account_attr={create_account_attr}')
		if submit_button:
			create_account_btn.click()
			time.sleep(10)
		actual_text = self.driver.find_element(AppiumBy.ID,'sign_up_title_tv').text
		return actual_text,create_account_attr

	
if __name__ =='__main__':
	print('this is main')
