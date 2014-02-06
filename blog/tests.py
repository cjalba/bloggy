from django.test import TestCase
from models import Post

class PostTest(TestCase):
	"""docstring for ClassName"""
	def test_str(self):
		my_title = Post(title = 'This is a basic')
		self.assertEquals(str(my_title.title), 'This is a basic')