from django.test import TestCase
from django.urls import reverse


# teste view home
class HomeViewTest(TestCase):
	
	#configuração
	def setUp(self):
		self.response = self.client.get(reverse('core:index'))
	
	#teste de status code == 200
	def test_status_code_200(self):
		self.assertEquals(self.response.status_code, 200)

	# teste existencia de template
	def test_template(self):
		self.assertTemplateUsed(self.response, 'index.html')
		
	# teste link de template
	def test_link_home(self):
		self.assertContains(self.response, '<a href="%s">Início</a>' % reverse("core:index"), html=True)

# teste view contact
class ContactViewTest(TestCase):
	
	#configuração
	def setUp(self):
		self.response = self.client.get(reverse('core:contact'))

	# teste de status code == 200
	def test_status_code_200(self):
		self.assertEquals(self.response.status_code, 200)

	# teste existencia de template
	def test_template(self):
		self.assertTemplateUsed(self.response, 'contact.html')

	# teste link de template
	def test_link_home(self):
		self.assertContains(self.response, '<a href="%s">Contato</a>' % reverse("core:contact"), html=True)


