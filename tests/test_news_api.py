import unittest
import sys
import os
from unittest.mock import patch, MagicMock

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from news_api import NewsAPI

class TestNewsAPI(unittest.TestCase):
    @patch('news_api.requests.get')
    def test_fetch_news_success(self, mock_get):
        mock_response = MagicMock()
        mock_response.json.return_value = {'status': 'ok', 'articles': []}
        mock_get.return_value = mock_response

        api = NewsAPI('fake_api_key')
        response = api.fetch_news('science')
        self.assertEqual(response['status'], "ok")
        self.assertIn('articles', response)

    @patch('news_api.requests.get')
    def test_fetch_news_invalid_key(self, mock_get):
        mock_response = MagicMock()
        mock_response.json.return_value = {
            'status': 'error',
            'code': 'apiKeyInvalid',
            'message': 'Invalid API key'
        }
        mock_get.return_value = mock_response

        api = NewsAPI('invalid_key')
        with self.assertRaises(Exception) as context:
            api.fetch_news('science')

        self.assertIn('API Error: Invalid API key', str(context.exception))

if __name__ == '__main__':
    unittest.main()
