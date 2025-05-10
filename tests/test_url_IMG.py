import unittest
from unittest.mock import patch, MagicMock
from tkinter import Tk
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from url_IMG import NewsApp

class TestNewsApp(unittest.TestCase):
    def setUp(self):
        # Patch requests.get
        patcher = patch('url_IMG.requests.get')
        self.mock_get = patcher.start()
        self.addCleanup(patcher.stop)

        # Create GUI instance
        self.root = Tk()
        self.app = NewsApp(self.root)
        self.maxDiff = None

        # Mocked NewsAPI JSON response
        self.mock_response = {
            'status': 'ok',
            'totalResults': 2,
            'articles': [
                {
                    'source': {'id': None, 'name': 'Test Source 1'},
                    'author': 'Test Author 1',
                    'title': 'Test Article 1',
                    'description': 'Description 1',
                    'url': 'http://example.com/1',
                    'urlToImage': 'http://example.com/image1.jpg',
                    'publishedAt': '2023-01-01T00:00:00Z',
                    'content': 'Detailed content 1'
                },
                {
                    'source': {'id': None, 'name': 'Test Source 2'},
                    'author': 'Test Author 2',
                    'title': 'Test Article 2',
                    'description': 'Description 2',
                    'url': 'http://example.com/2',
                    'urlToImage': 'http://example.com/image2.jpg',
                    'publishedAt': '2023-01-02T00:00:00Z',
                    'content': 'Detailed content 2'
                }
            ]
        }
        self.mock_get.return_value.json.return_value = self.mock_response

    def tearDown(self):
        self.root.destroy()

    def test_category_buttons(self):
        self.assertEqual(len(self.app.newsCatButton), len(self.app.newsCat))
        for i, btn in enumerate(self.app.newsCatButton):
            self.assertEqual(btn.cget('text').lower(), self.app.newsCat[i])

    @patch('url_IMG.NewsApp.clear')
    def test_load_news_item(self, mock_clear):
        mock_event = MagicMock()
        mock_event.widget.cget.return_value = 'technology'
        
        self.app.load_news_item(mock_event)
        self.assertEqual(self.app.data, self.mock_response)
        mock_clear.assert_called_once()

    @patch('url_IMG.NewsApp.clear')
    @patch('webbrowser.open')
    def test_display_article(self, mock_webbrowser_open, mock_clear):
        self.app.data = self.mock_response
        self.app.display_article(0)
        
        mock_clear.assert_called_once()
        
        labels = self.root.place_slaves()
        self.assertEqual(len(labels), 1)
        
        F1 = labels[0]
        self.assertEqual(len(F1.winfo_children()), 5)  # Image, Title, Description, PublishedAt, Frame
        
        article = self.mock_response['articles'][0]
        self.assertEqual(F1.winfo_children()[1].cget('text'), article['title'])
        self.assertEqual(F1.winfo_children()[2].cget('text'), article['description'])
        self.assertEqual(F1.winfo_children()[3].cget('text'), article['publishedAt'])
        
        buttons = F1.winfo_children()[4].winfo_children()
        self.assertEqual(len(buttons), 2)

        # Simulate clicking "Read More"
        buttons[0].invoke()
        mock_webbrowser_open.assert_called_once_with(article['url'])

    def test_open_link(self):
        with patch('webbrowser.open') as mock_open:
            url = 'http://example.com'
            self.app.open_link(url)
            mock_open.assert_called_once_with(url)

if __name__ == '__main__':
    unittest.main()
