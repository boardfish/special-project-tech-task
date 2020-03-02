import unittest
from getbirthday import GetBirthDay

class TestGetBirthDay(unittest.TestCase):

    def setUp(self):
        pass

    def output_under_upper_limit(self, gbd_instance, upperLimit):
        self.assertLess(gbd_instance.getBirthDay(), upperLimit)
    
    def output_over_lower_limit(self, gbd_instance, lowerLimit):
        self.assertGreater(gbd_instance.getBirthDay(), lowerLimit)

    #=======================
    # Months
    #=======================
    
    def test_errors_if_year_outside_limits(self):
        self.assertRaises(ValueError, lambda: GetBirthDay(-1, 1, 2020))
        self.assertRaises(ValueError, lambda: GetBirthDay(1, -1, 2020))
        self.assertRaises(ValueError, lambda: GetBirthDay(1, -1, -1))
        self.assertRaises(ValueError, lambda: GetBirthDay(32, 1, 2020))
        self.assertRaises(ValueError, lambda: GetBirthDay(1, 13, 2020))
    
    def test_errors_if_dates_outside_month_limits(self):
        self.assertRaises(ValueError, lambda: GetBirthDay(32, 1, 2020))
        self.assertRaises(ValueError, lambda: GetBirthDay(30, 2, 2020))
        self.assertRaises(ValueError, lambda: GetBirthDay(32, 3, 2020))
        self.assertRaises(ValueError, lambda: GetBirthDay(31, 4, 2020))
        self.assertRaises(ValueError, lambda: GetBirthDay(32, 5, 2020))
        self.assertRaises(ValueError, lambda: GetBirthDay(31, 6, 2020))
        self.assertRaises(ValueError, lambda: GetBirthDay(32, 7, 2020))
        self.assertRaises(ValueError, lambda: GetBirthDay(32, 8, 2020))
        self.assertRaises(ValueError, lambda: GetBirthDay(31, 9, 2020))
        self.assertRaises(ValueError, lambda: GetBirthDay(32, 10, 2020))
        self.assertRaises(ValueError, lambda: GetBirthDay(31, 11, 2020))
        self.assertRaises(ValueError, lambda: GetBirthDay(32, 12, 2020))
    
    def test_outputs_within_limits(self):
        for x in range(1, 31):
            gbd = GetBirthDay(x, 1, 2020)
            self.output_over_lower_limit(gbd, -1)
            self.output_under_upper_limit(gbd, 7)

    #==========================
    # Years
    #==========================

    # Leap year specific tests
    @unittest.skip("Delete this line for the extension task")
    def test_errors_if_dates_outside_feb_limits(self):
        # divisible by 4
        self.assertIsInstance(GetBirthDay(29, 2, 2020), GetBirthDay)
        # divisible by 100 but not 400
        self.assertRaises(ValueError, lambda: GetBirthDay(30, 2, 1900))
        # divisible by 400
        self.assertIsInstance(GetBirthDay(29, 2, 2000), GetBirthDay)
    
    @unittest.skip("Delete this line for the extension task")
    def test_important_dates(self):
        # My birthday
        self.assertEquals(GetBirthDay(8, 4, 1998).getBirthDay(), 2)
        # Christmas this year
        self.assertEquals(GetBirthDay(25, 12, 2020).getBirthDay(), 4)
        # Super Smash Bros. Ultimate's release date
        self.assertEquals(GetBirthDay(6, 12, 2018).getBirthDay(), 4)
        # Satoru Iwata's birthday
        self.assertEquals(GetBirthDay(6, 12, 1959).getBirthDay(), 6)
        # Kamen Rider's first airdate
        self.assertEquals(GetBirthDay(6, 12, 1959).getBirthDay(), 5)

if __name__ == '__main__':
    unittest.main()