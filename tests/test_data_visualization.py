import unittest
import pandas as pd
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
        self.visualization.plot_article_distribution_by_source()
        # Add more assertions here if necessary

    def test_plot_sentiment_analysis(self):
        self.visualization.plot_sentiment_analysis()
        # Add more assertions here if necessary

    def test_plot_trending_keywords(self):
        self.visualization.plot_trending_keywords()
        # Add more assertions here if necessary

if __name__ == '__main__':
    unittest.main()