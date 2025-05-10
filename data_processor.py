import pandas as pd

class DataProcessor:
    def combine_data(self, api_data, scraped_data):
        combined = []
        for article in api_data:
            url = article['url']
            if url in scraped_data:
                combined_article = {**article, **scraped_data[url], 'category': article.get('category', 'N/A')}
                combined.append(combined_article)
        return combined

    def clean_data(self, data):
        df = pd.DataFrame(data)
        df.drop_duplicates(subset=['url'], inplace=True)
        df.fillna('N/A', inplace=True)
        if 'content' in df.columns:
            df['content_length'] = df['content'].apply(lambda x: len(x) if isinstance(x, str) else 0)
        return df