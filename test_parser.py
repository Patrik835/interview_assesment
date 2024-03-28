import unittest
from assesment_parser import parse_xs_duration_format

class TestParser(unittest.TestCase):
    def test_parse_xs_duration_format_pos_nr(self):
        test_nr1 = 1347 * 31536000
        self.assertEqual(parse_xs_duration_format("P1347Y"), test_nr1)

    def test_parse_sx_duration_format_neg_nr(self):
        test_nr2 = -(1*31536000 + 2*2592000 + 3*86400+ 4*3600 + 5*60 + 6)
        self.assertEqual(parse_xs_duration_format("-P1Y2M3DT4H5M6S"), test_nr2)

    def test_parse_xs_duration_format_dec_nr(self):
        test_nr3 = 2*31536000  + 5*86400 + 12*3600 + 35*60 + 3.51
        self.assertEqual(parse_xs_duration_format("P2Y5DT12H35M3.51S"), test_nr3)

    def test_parse_xs_duration_format_messy_input(self):
        test_nr4 = 0
        self.assertEqual(parse_xs_duration_format("dsad55fa56sf85fe56wcdcx"), test_nr4)

    def test_parse_xs_duration_format_only_month(self):
        test_nr5 = 20*2592000
        self.assertEqual(parse_xs_duration_format("P20M"), test_nr5)

    def test_parse_xs_duration_format_only_minute(self):
        test_nr6 = 2*3600 + 5*60 + 3.55
        self.assertEqual(parse_xs_duration_format("PT2H5M3.55S") , test_nr6)

    def test_parse_xs_duration_format_month_minute(self):
        test_nr7 = 2*31536000 + 10*2592000 + 2*3600 + 5*60 + 3.79
        self.assertEqual(parse_xs_duration_format("P2Y10MT2H5M3.79S"), test_nr7)

if __name__ == '__main__':
    unittest.main()