import unittest
import pandas as pd
import sys, os


# Add root to path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from data_visualization import DataVisualization

class TestDataVisualization(unittest.TestCase):
    def setUp(self):
        data = {
            'source': ['Source 1', 'Source 2', 'Source 1'],
            'category': ['Tech', 'Health', 'Tech'],
            'content': ['Article content 1', 'Article content 2', 'Article content 3'],
            'title': ['Title 1', 'Title 2', 'Title 3'],
            'author': ['Author 1', 'Author 2', 'Author 1'],
            'publishedAt': ['2023-05-01', '2023-05-02', '2023-05-03']
        }
        self.cleaned_data = pd.DataFrame(data)
        self.visualization = DataVisualization(self.cleaned_data)

    def test_plot_article_distribution_by_source(self):
        try:
            self.visualization.plot_article_distribution_by_source()
        except Exception as e:
            self.fail(f"plot_article_distribution_by_source() raised an exception: {e}")

    def test_plot_sentiment_analysis(self):
        try:
            self.visualization.plot_sentiment_analysis()
        except Exception as e:
            self.fail(f"plot_sentiment_analysis() raised an exception: {e}")

    def test_plot_trending_keywords(self):
        try:
            self.visualization.plot_trending_keywords()
        except Exception as e:
            self.fail(f"plot_trending_keywords() raised an exception: {e}")

if __name__ == '__main__':
    unittest.main()
