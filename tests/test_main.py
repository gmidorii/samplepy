import unittest
import main

class TestMain(unittest.TestCase):

	def test_return_four(self):
		self.assertEqual(main.main(), 4)

if __name__ == '__main__':
	unittest.main()
