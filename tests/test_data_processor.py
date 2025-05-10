import unittest
import pandas as pd
import sys, os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from data_processor import DataProcessor  # adjust if needed

class TestDataProcessor(unittest.TestCase):
    def setUp(self):
        self.processor = DataProcessor()

    def test_combine_data(self):
        api_data = [{
            'url': 'https://example.com',
            'title': 'Example',
            'source': {'name': 'Example Source'},
            'content': 'Example content'
        }]
        scraped_data = {
            'https://example.com': {
                'author': 'John Doe',
                'publishedAt': '2023-05-15'
            }
        }
        combined = self.processor.combine_data(api_data, scraped_data)
        self.assertEqual(combined[0]['author'], 'John Doe')

    def test_clean_data(self):
        data = [{
            'url': 'https://example.com',
            'title': 'Example',
            'source': {'name': 'Example Source'},
            'content': 'Example content',
            'author': 'John Doe',
            'publishedAt': '2023-05-15'
        }]
        df = self.processor.clean_data(data)
        self.assertIsInstance(df, pd.DataFrame)
        self.assertFalse(df.empty)

if __name__ == '__main__':
    unittest.main()
