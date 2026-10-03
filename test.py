import unittest

from my_product import product


class TestSum(unittest.TestCase):
    def test_list_int(self):
        """
        Test that it can sum a list of integers
        """
        data = [1, 2, 3, 4]
        result = product(data)
        self.assertEqual(result, 24)

if __name__ == "__main__":
    unittest.main()

"""
This test uses the unittest module to test whether the method 'product' performs the expected operation.

1 * 2 * 3 * 4 should equal 24.

Test result:
OK

"""