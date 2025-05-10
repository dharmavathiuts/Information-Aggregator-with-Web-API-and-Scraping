import unittest
from tkinter import Tk
import pandas as pd
from unittest.mock import patch, MagicMock
import sys, os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from gui_app import NewsAggregatorGUI  # <- update this if you renamed

class TestNewsAggregatorGUI(unittest.TestCase):
    @patch('gui_app.DataProcessor')
    @patch('gui_app.WebScraper')
    @patch('gui_app.NewsAPI')
    def test_fetch_news(self, MockNewsAPI, MockWebScraper, MockDataProcessor):
        root = Tk()
        root.withdraw()  # Prevent GUI from opening

        app = NewsAggregatorGUI(api_key='fake_api_key')

        # Mock setup
        mock_api_instance = MockNewsAPI.return_value
        mock_api_instance.fetch_news.return_value = {'articles': [
            {'title': 'Test articles 1', 'url': 'http://example.com', 'source': {'name': 'Source A'}},
            {'title': 'Test articles 2', 'url': 'http://example.com', 'source': {'name': 'Source B'}}
        ]}

        mock_scraper_instance = MockWebScraper.return_value
        mock_scraper_instance.scrape_article.return_value = {
            'content': 'Detailed content',
            'author': 'Author Name',
            'publishedAt': '2023-01-01'
        }

        mock_processor_instance = MockDataProcessor.return_value
        mock_processor_instance.combine_data.side_effect = lambda api_data, scraped: api_data
        mock_processor_instance.clean_data.return_value = pd.DataFrame([
            {'title': 'Test articles 1', 'content': 'Detailed content', 'author': 'Author Name', 'publishedAt': '2023-01-01', 'source': {'name': 'Source A'}},
            {'title': 'Test articles 2', 'content': 'Detailed content', 'author': 'Author Name', 'publishedAt': '2023-01-01', 'source': {'name': 'Source B'}}
        ])

        app.clicked.set('general')
        app.fetch_news()

        # Check expected list
        self.assertEqual(len(app.articles), 2)
        self.assertEqual(app.articles[0]['title'], 'Test articles 1')
        self.assertEqual(app.articles[1]['title'], 'Test articles 2')

        root.destroy()

if __name__ == '__main__':
    unittest.main()
