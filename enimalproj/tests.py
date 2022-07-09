from django.test import TestCase
from enimalproj.views import MainPage
from django.urls import resolve
from django.http import HttpRequest
from django.template.loader import render_to_string
from enimalproj.models import DogOwnerInfo


class HomePageTest(TestCase):
	def test_mainpage_as_seen_client(self):
		response = self.client.get('/')
		self.assertTemplateUsed(response, 'mainpage.html')
	

	def test_save_post_request(self):
		response = self.client.post('/', data={'surname': 'Dinapo',
         'firstname' : 'Maria Linda',
         'address' : 'Mabuhay City',
         'cnumber' : '639480656609'})

		cData = DogOwnerInfo.objects.first()
		self.assertEqual(cData.ownersLastName, 'Dinapo')
		self.assertEqual(cData.ownersFirstName, 'Maria Linda')
		self.assertEqual(cData.ownersAddress, 'Mabuhay City')
		self.assertEqual(cData.ownersContactNumber, 639480656609)

	def test_models(self):
		self.client.get('/')
		self.assertEqual(DogOwnerInfo.objects.count(), 0)

class ORMtest(TestCase):
    def test_retrieveModels(self):
        M1 = DogOwnerInfo()
        M1.ownersLastName = 'Dinapo'
        M1.ownersFirstName = 'Maria Linda'
        M1.ownersAddress = 'Mabuhay City'
        M1.ownersContactNumber = '639480656609'
        M1.Rdbtn = 'Yes'
        M1.save()

        M2 = DogOwnerInfo()
        M2.ownersLastName = 'Eme'
        M2.ownersFirstName = 'Clara'
        M2.ownersAddress = 'Paliparan'
        M2.ownersContactNumber = '639480656656'
        M2.Rdbtn = 'Yes'
        M2.save()

        RList = DogOwnerInfo.objects.all()
        self.assertEqual(RList.count(), 2)

        Information1 = RList[0]
        Information2 = RList[1]

        self.assertEqual(Information1.ownersLastName, 'Dinapo')
        self.assertEqual(Information1.ownersFirstName, 'Maria Linda')
        self.assertEqual(Information1.ownersAddress, 'Mabuhay City')
        self.assertEqual(Information1.ownersContactNumber, 639480656609)

        self.assertEqual(Information2.ownersLastName, 'Eme')
        self.assertEqual(Information2.ownersFirstName, 'Clara')
        self.assertEqual(Information2.ownersAddress, 'Paliparan')
        self.assertEqual(Information2.ownersContactNumber, 639480656656)

    def test_template(self):
    	DogOwnerInfo.objects.create(ownersLastName = 'Dinapo',
	        ownersFirstName = 'Maria Linda',
	        ownersAddress = 'Mabuhay City',
	        ownersContactNumber = '639480656609',)
    	response = self.client.get('/')
    	self.assertIn('1: Dinapo, Maria Linda, Mabuhay City, 639480656609', response.content.decode())
    	

    	