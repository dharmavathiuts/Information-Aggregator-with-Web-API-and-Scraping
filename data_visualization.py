pip install seaborn matplotlib pandas wordcloud textblob nltk
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from wordcloud import WordCloud
from textblob import TextBlob
import nltk
from nltk.corpus import stopwords

# Ensure NLTK stopwords are downloaded
# nltk.download('stopwords')
# nltk.download('punkt')

class DataVisualization:
    def __init__(self, data):
        self.data = data

    def plot_article_distribution_by_source(self):
        self.data['source_name'] = self.data['source'].apply(lambda x: x['name'] if isinstance(x, dict) else 'Unknown')
        source_counts = self.data['source_name'].value_counts()
        plt.figure(figsize=(10, 5))
        source_counts.plot(kind='bar')
        plt.title('Article Distribution by Source')
        plt.xlabel('Source')
        plt.ylabel('Number of Articles')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

    def plot_article_distribution_by_author(self):
        category_counts = self.data['author'].value_counts()
        plt.figure(figsize=(10, 5))
        category_counts.plot(kind='pie', autopct='%1.1f%%', startangle=140)
        plt.title('Article Distribution by Author')
        plt.ylabel('')
        plt.tight_layout()
        plt.show()

    def plot_article_lengths(self):
        plt.figure(figsize=(10, 5))
        self.data['content_length'].plot(kind='hist', bins=20)
        plt.title('Distribution of Article Lengths')
        plt.xlabel('Content Length')
        plt.ylabel('Frequency')
        plt.tight_layout()
        plt.show()

    def plot_articles_over_time(self):
        self.data['publishedAt'] = pd.to_datetime(self.data['publishedAt'])
        self.data.set_index('publishedAt', inplace=True)
        articles_over_time = self.data.resample('D').size()
        plt.figure(figsize=(10, 5))
        articles_over_time.plot()
        plt.title('Number of Articles Over Time')
        plt.xlabel('Date')
        plt.ylabel('Number of Articles')
        plt.tight_layout()
        plt.show()

    def plot_correlation_heatmap(self):
        numerical_data = self.data.select_dtypes(include=['float64', 'int64'])
        correlation_matrix = numerical_data.corr()
        plt.figure(figsize=(10, 5))
        sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', linewidths=0.5)
        plt.title('Correlation Heatmap of Numerical Features')
        plt.tight_layout()
        plt.show()

    def plot_wordcloud_for_titles(self):
        titles = ' '.join(self.data['title'])
        wordcloud = WordCloud(width=800, height=400, background_color='white').generate(titles)
        plt.figure(figsize=(10, 5))
        plt.imshow(wordcloud, interpolation='bilinear')
        plt.axis('off')
        plt.title('Word Cloud for Article Titles')
        plt.tight_layout()
        plt.show()

    def plot_top_authors(self):
        if 'author' in self.data.columns:
            author_counts = self.data['author'].value_counts().head(10)
            plt.figure(figsize=(10, 5))
            author_counts.plot(kind='barh')
            plt.title('Top Authors by Number of Articles')
            plt.xlabel('Author')
            plt.ylabel('Number of Articles')
            plt.xticks(rotation=45)
            plt.tight_layout()
            plt.show()
        else:
            print("No 'author' column found in data")

    def plot_publication_time_distribution(self):
        self.data['publishedAt'] = pd.to_datetime(self.data['publishedAt'])
        self.data['hour'] = self.data['publishedAt'].dt.hour
        hour_counts = self.data['hour'].value_counts().sort_index()
        plt.figure(figsize=(10, 5))
        hour_counts.plot(kind='bar')
        plt.title('Article Publication Time Distribution')
        plt.xlabel('Hour of Day')
        plt.ylabel('Number of Articles')
        plt.tight_layout()
        plt.show()

    def plot_sentiment_analysis(self):
        def get_sentiment(text):
            blob = TextBlob(text)
            if blob.sentiment.polarity > 0:
                return 'Positive'
            elif blob.sentiment.polarity < 0:
                return 'Negative'
            else:
                return 'Neutral'

        self.data['sentiment'] = self.data['title'].apply(lambda x: get_sentiment(str(x)))
        plt.figure(figsize=(10, 6))
        sns.countplot(data=self.data, x='sentiment', order=['Positive', 'Neutral', 'Negative'])
        plt.title('Sentiment Analysis of News Headlines')
        plt.xlabel('Sentiment')
        plt.ylabel('Number of Articles')
        plt.tight_layout()
        plt.show()

    def plot_trending_keywords(self):
        stop_words = set(stopwords.words('english'))
        all_titles = ' '.join(self.data['title'].dropna()).lower()
        words = nltk.word_tokenize(all_titles)
        filtered_words = [word for word in words if word.isalnum() and word not in stop_words]

        freq_dist = nltk.FreqDist(filtered_words)
        most_common = freq_dist.most_common(20)

        keywords_df = pd.DataFrame(most_common, columns=['Keyword', 'Frequency'])
        plt.figure(figsize=(10, 6))
        sns.barplot(data=keywords_df, x='Frequency', y='Keyword')
        plt.title('Trending Keywords in News Headlines')
        plt.xlabel('Frequency')
        plt.ylabel('Keyword')
        plt.tight_layout()
        plt.show()

    def get_data_for_display(self):
        return self.data