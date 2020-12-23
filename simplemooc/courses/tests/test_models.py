from django.test import TestCase
from ..models import Course

class CourseModelsTest(TestCase):
	def setUp(self):
		self.course = Course.objects.create(
			name = "Python para Web"
			)

	def test_str_course(self):
		self.assertEqual(str(self.course), 'Python para Web')