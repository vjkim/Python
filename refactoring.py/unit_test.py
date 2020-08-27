### 8/26/2020
### A function to test


import unittest

from test_funtion_1 import get_formatted_name

class NamesTestCase(unittest.TestCase):
	"""Tests for the function test_funtion_1.py"""

	def test_first_last_name(self):
		"""Test first and last names."""
		formatted_name = get_formatted_name('v', 'kim')
		self.assertEqual(formatted_name, 'V Kim')


unittest.main()