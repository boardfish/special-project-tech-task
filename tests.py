import unittest
from getbirthday import GetBirthDay


class TestGetBirthDay(unittest.TestCase):

    def setUp(self):
        pass

    def output_under_upper_limit(self, gbd_instance, upperLimit):
        self.assertLess(gbd_instance.day_index(), upperLimit)

    def output_over_lower_limit(self, gbd_instance, lowerLimit):
        self.assertGreater(gbd_instance.day_index(), lowerLimit)

    # =======================
    # Months
    # =======================

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

    def test_important_dates_this_year(self):
        # My birthday
        self.assertEqual(GetBirthDay(8, 4, 2020).day_index(), 2)
        # Christmas this year
        self.assertEqual(GetBirthDay(25, 12, 2020).day_index(), 4)
        # Super Smash Bros. Ultimate's second anniversary
        self.assertEqual(GetBirthDay(6, 12, 2020).day_index(), 6)
        # The 2020 Olympics begin
        self.assertEqual(GetBirthDay(24, 7, 2020).day_index(), 4)

    # ==========================
    # Years
    # ==========================

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
        self.assertEqual(GetBirthDay(8, 4, 1998).day_index(), 2)
        # Super Smash Bros. Ultimate's release date
        self.assertEqual(GetBirthDay(6, 12, 2018).day_index(), 3)
        # Satoru Iwata's birthday
        self.assertEqual(GetBirthDay(6, 12, 1959).day_index(), 6)
        # Kamen Rider's first airdate
        self.assertEqual(GetBirthDay(3, 4, 1971).day_index(), 5)


if __name__ == '__main__':
    unittest.main()
