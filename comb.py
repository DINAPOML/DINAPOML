/*mainpage*/


<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8" />
	<meta name="viewport" content="width=device-width, initial-scale=1" />
	<title>E-nimals</title>
</head>
	<body>
		<h1>Puppy Adoption Application</h1>
		<form method="POST">
		<label>Last name:*</label>
		<input 
			type="text" 
			id="surname" 
			size="30" 
			name="surname" 
			placeholder="Enter your surname here."
		/>
		<label>First name:*</label>
		<input 
			type="text" 
			id="firstname" 
			size="30" 
			name="firstname" 
			placeholder="Enter your firstname here."
		/>
		<br><br>
		<label>Address:*</label>
		<input 
			type="text" 
			id="address" 
			size="30" 
			name="address" 
			placeholder="Enter your address here."
		/>
		<label>Contact Number:*</label>
		<input 
			type="text" 
			id="cnumber" 
			size="30" 
			name="cnumber" 
			placeholder="Enter your contact number here."
		/>
		<br><br>
            <label for="answer">Puppy Gender:</label>
        
        <br>
            <input type="radio" name="gender"  id="gender" value="20" > Yes
            <input type="radio" name="gender"  id="gender" value="10" > No

        <br><br>
        <label for="answer">Do you have any pets?</label>
        
        <br>
            <input type="radio" name="yes"  id="yes" value="20" > Yes
            <input type="radio" name="no"  id="no" value="10" > No

		<br><br>
		<label for="answer">Pet Breeds:</label>
                  <select type="dropdown" id="Breeds" name="Breeds" required>
                  <option>Chihuahua</option>
                  <option>Boxer</option>
                  <option>Golden Retriever</option>
                  <option>Poodle</option>
                  <option>German Shepherd</option>
                  </select>
		{% csrf_token %}

		<input id="btnDot"type="submit" name="btnDot" value="Submit"/>
	</form>
	<table id="registryTable">
		<tr>
			<td>1: {{Surname}} {{Firstname}} {{Address}} {{ContactNumber}} {{Gender}} {{Pets}} {{Breeds}}</td>
		</tr>
	</table>		
	</body>	
</html>



TEST

from django.urls import resolve
from django.test import TestCase
from enimalproj.views import MainPage
from django.http import HttpRequest
from django.template.loader import render_to_string

class HomePageTest(TestCase):
	def test_mainpage_as_seen_client(self):
		response = self.client.get('/')
		self.assertTemplateUsed(response, 'mainpage.html')
	
		
	def test_responding_post_request(self):
		resp = self.client.post('/', data={'surname':'Surname', 
			'firstname':'Firstname', 
			'address':'Address', 
			'cnumber':'ContactNumber', 
			'gender':'Gender', 
			'pets':'Pets', 
			'breeds':'Breeds'})
		self.assertIn('Surname', resp.content.decode())
		self.assertTemplateUsed(response, 'mainpage.html')

VIEWS
from django.shortcuts import render
from django.http import HttpResponse

def MainPage(request):
	return render(request, 'mainpage.html' ,
		'Surname'==request.POST.get(surname) ,
		'Firstname'==request.POST.get(firstname) ,
		'Address'==request.POST.get(address) ,
		'ContactNumber'==request.POST.get(cnumber) ,
		'Gender'==request.POST.get(gender) ,
		'Pets'==request.POST.get(pets) ,
		'Breeds'==request.POST.get(breeds))

FTEST
from selenium import webdriver
import unittest
from selenium.webdriver.common.keys import Keys
import time

class PageTest(unittest.TestCase):
	def setUp(self):
		self.browser = webdriver.Firefox()
		
	def test_start_list_and_retrieve_it(self):
		self.browser.get('http://localhost:8000')
		time.sleep(1)
		self.assertIn('E-nimals', self.browser.title)
		headerText = self.browser.find_element_by_tag_name('h1').text
		self.assertIn('Puppy Adoption Application', headerText)
		inpSurname = self.browser.find_element_by_id('surname')
		inpFirstname = self.browser.find_element_by_id('firstname')
		inpAddress = self.browser.find_element_by_id('address')
		inpContactNumber = self.browser.find_element_by_id('cnumber')
		inpGender = self.browser.find_element_by_id('gender')
		inpPets = self.browser.find_element_by_id('pets')
		inpBreeds = self.browser.find_element_by_id('breeds')
		btn_Dot_button = self.browser.find_element_by_id('btnDot')
		self.assertEqual(inpSurname.get_attribute('placeholder'),'Enter your surname here.')
		inpSurname.click()
		time.sleep(1)
		inpSurname.send_keys('Dinapo')

		inpFirstname.click()
		time.sleep(1)
		inpFirstname.send_keys('Maria Linda')

		inpAddress.click()
		time.sleep(1)
		inpAddress.send_keys('Mabuhay City')

		inpContactNumber.click()
		time.sleep(1)
		inpContactNumber.send_keys('09480656609')

		inpContactNumber.click()
		time.sleep(1)
		inpGender.send_keys('female')

		inpPets.click()
		time.sleep(1)
		inpPets.send_keys('Yes')

		inpBreeds.click()
		time.sleep(1)
		inpBreeds.send_keys('Chihuahua')

		btn_Dot_button.click()
		time.sleep(1)

	def checking_if_in_table_list(self,row_test):
		table = self.browser.find_element_by_id('registryTable')
		rows = table.find_elements_by_tag_name('tr')
		self.assertIn('', [rows.text for rows in rows])

if __name__ == '__main__':
	unittest.main(warnings='ignore')
