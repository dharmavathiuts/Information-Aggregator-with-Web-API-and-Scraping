import requests
from bs4 import BeautifulSoup

class WebScraper:
    def scrape_article(self, url):
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        title = soup.find('title').get_text() if soup.find('title') else 'N/A'
        author = soup.find(attrs={"name": "author"}).get('content') if soup.find(attrs={"name": "author"}) else 'N/A'
        pub_date = soup.find(attrs={"name": "pubdate"}).get('content') if soup.find(attrs={"name": "pubdate"}) else 'N/A'
        content = ' '.join([p.get_text() for p in soup.find_all('p')]) if soup.find_all('p') else 'N/A'
        
        return {
            'title': title,
            'author': author,
            'pub_date': pub_date,
            'content': content
        }