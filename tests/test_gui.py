import unittest
from tkinter import Tk
import pandas as pd
from gui import NewsAggregatorGUI
from unittest.mock import patch, MagicMock

class TestNewsAggregatorGUI(unittest.TestCase):
    @patch('gui.NewsAPI')
    @patch('gui.WebScraper')
    @patch('gui.DataProcessor')
    def test_fetch_news(self, MockDataProcessor, MockWebScraper, MockNewsAPI):
        root = Tk()
        app = NewsAggregatorGUI(api_key='793e5223f292469393b739eacd25c7eb')
        app.master = root

        mock_api_instance = MockNewsAPI.return_value
        mock_api_instance.fetch_news.return_value = {'articles': [
            {'title': 'Test articles 1', 'description': 'Description 1'},
            {'title': 'Test articles 2', 'description': 'Description 2'}
        ]}
        mock_scraper_instance = MockWebScraper.return_value
        mock_scraper_instance.scrape_articles.return_value = {
            'content': 'Detailed content',
            'author': 'Author Name',
            'publication_date': '2023-01-01'
        }
        mock_processor_instance = MockDataProcessor.return_value
        mock_processor_instance.combine_data.return_value = [
            {'title': 'Test articles 1', 'description': 'Description 1', 'content': 'Detailed content', 'author': 'Author Name', 'publication_date': '2023-01-01'},
            {'title': 'Test articles 2', 'description': 'Description 2', 'content': 'Detailed content', 'author': 'Author Name', 'publication_date': '2023-01-01'}
        ]
        mock_processor_instance.clean_data.return_value = pd.DataFrame([
            {'title': 'Test articles 1', 'description': 'Description 1', 'content': 'Detailed content', 'author': 'Author Name', 'publication_date': '2023-01-01'},
            {'title': 'Test articles 2', 'description': 'Description 2', 'content': 'Detailed content', 'author': 'Author Name', 'publication_date': '2023-01-01'}
        ])

        # Set the category to 'technology'
        app.clicked.set('general')
        app.fetch_news()

        # Check that the articles have been updated correctly
        self.assertEqual(len(app.articles), 2)
        self.assertEqual(app.articles[0]['title'], 'Test articles 1')
        self.assertEqual(app.articles[1]['title'], 'Test articles 2')

        # Cleanup
        root.destroy()

if __name__ == '__main__':
    unittest.main()