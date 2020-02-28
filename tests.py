import unittest
from getbirthday import GetBirthDay

class TestGetBirthDay(unittest.TestCase):

    def setUp(self):
        pass

    def output_under_upper_limit(self, gbd_instance, upperLimit):
        self.assertLess(gbd_instance.getBirthDay(), upperLimit)
    
    def output_over_lower_limit(self, gbd_instance, lowerLimit):
        self.assertGreater(gbd_instance.getBirthDay(), lowerLimit)
    
    def test_errors_if_year_outside_limits(self):
        self.assertRaises(ValueError, lambda: GetBirthDay(-1, 1, 1900))
        self.assertRaises(ValueError, lambda: GetBirthDay(1, -1, 1900))
        self.assertRaises(ValueError, lambda: GetBirthDay(1, -1, -1))
        self.assertRaises(ValueError, lambda: GetBirthDay(32, 1, 1900))
        self.assertRaises(ValueError, lambda: GetBirthDay(1, 13, 1900))
    
    def test_errors_if_dates_outside_month_limits(self):
        self.assertRaises(ValueError, lambda: GetBirthDay(32, 1, 1900))
        self.assertRaises(ValueError, lambda: GetBirthDay(30, 2, 1900))
        self.assertRaises(ValueError, lambda: GetBirthDay(32, 3, 1900))
        self.assertRaises(ValueError, lambda: GetBirthDay(31, 4, 1900))
        self.assertRaises(ValueError, lambda: GetBirthDay(32, 5, 1900))
        self.assertRaises(ValueError, lambda: GetBirthDay(31, 6, 1900))
        self.assertRaises(ValueError, lambda: GetBirthDay(32, 7, 1900))
        self.assertRaises(ValueError, lambda: GetBirthDay(32, 8, 1900))
        self.assertRaises(ValueError, lambda: GetBirthDay(31, 9, 1900))
        self.assertRaises(ValueError, lambda: GetBirthDay(32, 10, 1900))
        self.assertRaises(ValueError, lambda: GetBirthDay(31, 11, 1900))
        self.assertRaises(ValueError, lambda: GetBirthDay(32, 12, 1900))
    
    def test_outputs_within_limits(self):
        gbd = GetBirthDay(1, 1, 1900)
        self.output_over_lower_limit(gbd, -1)
        self.output_under_upper_limit(gbd, 7)

if __name__ == '__main__':
    unittest.main()