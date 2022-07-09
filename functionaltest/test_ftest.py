from selenium import webdriver
import unittest
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import WebDriverException
from django.test import LiveServerTestCase
import time


class PageTest(LiveServerTestCase):
	def setUp(self):
		self.browser = webdriver.Firefox()
		
	def test_start_list_and_retrieve_it(self):
		self.browser.get(self.live_server_url)
		self.assertIn('E-nimals', self.browser.title)
		headerText = self.browser.find_element_by_tag_name('h1').text
		self.assertIn('Puppy Adoption Application', headerText)

#M1
		inpSurname = self.browser.find_element_by_id('surname')
		btn_button=self.browser.find_element_by_id('button')
		self.assertEqual(inpSurname.get_attribute('placeholder'),'Enter your surname here.')
		inpSurname.click()
		inpSurname.send_keys('Dinapo')
		time.sleep(1)

		inpFirstname = self.browser.find_element_by_id('firstname')
		inpFirstname.click()
		inpFirstname.send_keys('Maria Linda')
		time.sleep(1)

		inpAddress = self.browser.find_element_by_id('address')
		inpAddress.click()
		inpAddress.send_keys('Mabuhay City')
		time.sleep(1)

		inpContactNumber = self.browser.find_element_by_id('cnumber')
		inpContactNumber.click()
		inpContactNumber.send_keys('09480656609')
		time.sleep(1)

		btn_Dot_button = self.browser.find_element_by_id('button')
		btn_Dot_button.click()
		time.sleep(1)

#M2

		inpSurname = self.browser.find_element_by_id('surname')
		btn_button=self.browser.find_element_by_id('button')
		self.assertEqual(inpSurname.get_attribute('placeholder'),'Enter your surname here.')
		inpSurname.click()
		inpSurname.send_keys('Eme')
		time.sleep(1)

		inpFirstname = self.browser.find_element_by_id('firstname')
		inpFirstname.click()
		inpFirstname.send_keys('Clara')
		time.sleep(1)

		inpAddress = self.browser.find_element_by_id('address')
		inpAddress.click()
		inpAddress.send_keys('Paliparan')
		time.sleep(1)

		inpContactNumber = self.browser.find_element_by_id('cnumber')
		inpContactNumber.click()
		inpContactNumber.send_keys('09480656656')
		time.sleep(1)

		btn_Dot_button = self.browser.find_element_by_id('button')
		btn_Dot_button.click()
		time.sleep(1)


		table=self.browser.find_element_by_id('registryTable')
		rows = table.find_elements_by_tag_name('tr')
		self.assertIn('1: Dinapo, Maria Linda, Mabuhay City, 9480656609', [row.text for row in rows])

		self.assertIn('2: Eme, Clara, Paliparan, 9480656656', [row.text for row in rows])



if __name__ == '__main__':
	unittest.main(warnings='ignore')
