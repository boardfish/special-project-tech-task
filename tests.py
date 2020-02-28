import unittest
from getbirthday import GetBirthDay

class TestGetBirthDay(unittest.TestCase):

    def setUp(self):
        pass

    def test_inputs_within_upper_limits(self):
        self.assertEqual(GetBirthDay.foo(), 12)

if __name__ == '__main__':
    unittest.main()