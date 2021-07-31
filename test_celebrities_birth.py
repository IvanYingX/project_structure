import unittest
from celebrities_births import Date
from celebrities_births import Scraper

class DateTestCase(unittest.TestCase):
    def test_lower_than(self):
        date_1 = Date(1, 5, 2020)
        date_2 = Date(2, 3, 2050)
        self.assertLess(date_1, date_2)
    
    def test_date_validity(self):
        with self.assertRaises(ValueError) as err:
            Date(32, 5, 2020)
    
    def test_from_string(self):
        date_1 = Date(1, 5, 2020)
        date_2 = Date.from_string('1-5-2020')
        self.assertEqual(date_1, date_2)

class ScraperTestCase(unittest.TestCase):
    def setUp(self):
        self.scraper = Scraper()

    def test_wrong_date(self):
        date = 'February_30'
        with self.assertRaises(ValueError) as err:
            self.scraper.get_celebrities(date)
    
    def test_birth_header(self):
        date = 'March_27'
        h2 = self.scraper._get_birth_header(date)
        self.assertEqual(h2.text, 'Births[edit]')

class CelebrityTestCase(unittest.TestCase):
    def setUp(self):
        self.scraper = Scraper()

    def test_celebrity_with_date(self):
        date = Date(27, 3, 2020).to_wiki_format()
        celebrities = self.scraper.get_celebrities(date)
        self.assertIn('Quentin Tarantino', celebrities)
