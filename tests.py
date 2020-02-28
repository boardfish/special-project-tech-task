import unittest
from getbirthday import GetBirthDay

class TestGetBirthDay(unittest.TestCase):

    def setUp(self):
        pass

    def inputs_within_upper_limits(self, upperLimit):
        self.assertLess(GetBirthDay.foo(), upperLimit)
    
    def test_foo_within_upper_limits(self):
        self.inputs_within_upper_limits(15)

if __name__ == '__main__':
    unittest.main()