import unittest
from unittest.mock import patch, MagicMock
import sys
import os

# Add root path if needed
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from web_scraper import WebScraper

class TestWebScraper(unittest.TestCase):

    @patch('web_scraper.requests.get')
    def test_scrape_valid_url(self, mock_get):
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.text = """
        <html>
            <head><title>Test Article</title><meta name="author" content="Author A"></head>
            <body><p>This is a test paragraph.</p></body>
        </html>
        """
        mock_get.return_value = mock_response

        scraper = WebScraper()
        data = scraper.scrape_article("http://example.com/test")
        self.assertIn("content", data)
        self.assertIn("This is a test paragraph.", data["content"])

    def test_scrape_invalid_url(self):
        scraper = WebScraper()
        with self.assertRaises(Exception):
            scraper.scrape_article("invalid_url")

if __name__ == '__main__':
    unittest.main()
