import unittest
from assesment_with_split import parse_with_split

class TestParser(unittest.TestCase):
    def test_parse_with_split_pos_nr(self):
        test_nr1 = 1347 * 31536000
        self.assertEqual(parse_with_split("P1347Y"), test_nr1)

    def test_parse_with_split_dec_nr(self):
        test_nr3 = 2*31536000  + 5*86400 + 12*3600 + 35*60 + 3.51
        self.assertEqual(parse_with_split("P2Y5DT12H35M3.51S"), test_nr3)

    def test_parse_with_split_no_p(self):
        result = parse_with_split("2Y5DT12H35M3.51S")
        self.assertIsInstance(result, ValueError)
        self.assertEqual(str(result), "Error, input must start with P.")

    def test_parse_with_split_only_month(self):
        result = parse_with_split("P20M")
        self.assertIsInstance(result, ValueError)
        self.assertEqual(str(result), "Error, month can't be used for this conversion")

    def test_parse_with_split_only_minute(self):
        test_nr6 = 2*3600 + 5*60 + 3.55
        self.assertEqual(parse_with_split("PT2H5M3.55S") , test_nr6)

    def test_parse_with_split_month_minute(self):
        result = parse_with_split("P2Y10MT2H5M3.79S")
        self.assertIsInstance(result, ValueError)
        self.assertEqual(str(result), "Error, month can't be used for this conversion")

if __name__ == '__main__':
    unittest.main()