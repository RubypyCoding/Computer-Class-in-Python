import unittest
from computer import *


class ComputerTests(unittest.TestCase):

	def setUp(self):
		self.func = Computer("Mac","MacBook Air","Intel")

	def test_mark_is_evaluated_as_getter(self):
	    self.assertEqual(self.func.mark, "Mac")

	def test_mark_is_evaluated_as_setter(self):
		with self.assertRaises(AttributeError):
		    self.func.mark = "Dell"

	def test_processor_is_evaluated_as_getter(self):
		self.assertEqual(self.func.processor, "Intel")

	def test_processor_is_evaluated_as_setter(self):
		raised = False
		try:
			self.func.processor = "Intel Core"
		except:
			raised = True
		self.assertFalse(raised, 'Exception raised')

	def test_processor_is_evaluated_as_getter_and_setter(self):
		self.func.processor = "Intel Core"
		self.assertEqual(self.func.processor, "Intel Core")

	def test_type_is_evaluated_as_getter(self):
		with self.assertRaises(AttributeError):
			self.func.type

	def test_type_is_evaluated_as_setter(self):
		raised = False
		try:
			self.func.type = "MacBook Pro"
		except:
			raised = True
		self.assertFalse(raised, 'Exception raised')


if __name__=="__main__":
    unittest.main()