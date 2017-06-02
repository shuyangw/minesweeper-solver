import unittest
import os
import sys

modcwd = os.getcwd()[:-6]+"\\func"
sys.path.append(modcwd)

import screen

class TestTest(unittest.TestCase):
	def test1(self):
		self.assertEqual(3**3 , 9)
	def test2(self):
		self.assertEqual(3**4, 9)
		
if __name__ == "__main__":
	print("TODO")
	pass
