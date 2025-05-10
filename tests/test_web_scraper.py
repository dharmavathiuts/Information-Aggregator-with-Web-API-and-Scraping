import unittest
from web_scraper import WebScraper

class TestWebScraper(unittest.TestCase):
    def setUp(self):
        self.scraper = WebScraper()

    def test_scrape_valid_url(self):
        url = 'https://example.com/news-article'
        data = self.scraper.scrape_article(url)
        self.assertIn('content', data)

    def test_scrape_invalid_url(self):
        url = 'invalid_url'
        with self.assertRaises(Exception):
            self.scraper.scrape_article(url)

if __name__ == '__main__':
    unittest.main()