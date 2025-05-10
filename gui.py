import tkinter as tk
from tkinter import ttk, messagebox
from news_api import NewsAPI
from web_scraper import WebScraper
from data_processor import DataProcessor
from data_visualization import DataVisualization
import subprocess
import json

class NewsAggregatorGUI(tk.Tk):
    def __init__(self, api_key):
        super().__init__()
        self.title("News Aggregator")
        self.geometry("515x510")

        self.api_key = api_key
        self.create_widgets()

    def create_widgets(self):
        self.label_category = tk.Label(self, text="Select News Category:")
        self.label_category.grid(row=0, column=0, padx=5, pady=5)

        self.clicked = tk.StringVar(self)
        self.categories = ["general","sports","health","entertainment","science","business","technology"]
        self.clicked.set(self.categories[0])
        self.category_menu = tk.OptionMenu(self, self.clicked, *self.categories)
        self.category_menu.grid(row=0, column=1, padx=5, pady=5)

        self.fetch_button = tk.Button(self, text="Fetch Headlines", command=self.fetch_news)
        self.fetch_button.grid(row=0, column=2, padx=5, pady=5)

        self.articles_listbox = tk.Listbox(self, width=80, height=15)
        self.articles_listbox.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

        self.show_details_button = tk.Button(self, text="Show News Content", command=self.show_article_details)
        self.show_details_button.grid(row=2, column=0, columnspan=3, pady=5)

        # Row 3
        self.plot_source_distribution_button = tk.Button(self, text="Plot Source Distribution", command=self.plot_source_distribution)
        self.plot_source_distribution_button.grid(row=3, column=0, padx=5, pady=5)

        self.plot_category_distribution_button = tk.Button(self, text="Plot Author Distribution", command=self.plot_author_distribution)
        self.plot_category_distribution_button.grid(row=3, column=1, padx=5, pady=5)

        self.plot_article_lengths_button = tk.Button(self, text="Plot Article Lengths", command=self.plot_article_lengths)
        self.plot_article_lengths_button.grid(row=3, column=2, padx=5, pady=5)

        # Row 4
        self.plot_articles_over_time_button = tk.Button(self, text="Plot Articles Over Time", command=self.plot_articles_over_time)
        self.plot_articles_over_time_button.grid(row=4, column=0, padx=5, pady=5)

        self.plot_correlation_heatmap_button = tk.Button(self, text="Plot Correlation Heatmap", command=self.plot_correlation_heatmap)
        self.plot_correlation_heatmap_button.grid(row=4, column=1, padx=5, pady=5)

        self.plot_wordcloud_button = tk.Button(self, text="Plot Word Cloud for Titles", command=self.plot_wordcloud_for_titles)
        self.plot_wordcloud_button.grid(row=4, column=2, padx=5, pady=5)

        # Row 5
        self.plot_top_authors_button = tk.Button(self, text="Plot Top Authors", command=self.plot_top_authors)
        self.plot_top_authors_button.grid(row=5, column=0, padx=5, pady=5)

        self.plot_publication_time_button = tk.Button(self, text="Plot Publication Time Distribution", command=self.plot_publication_time_distribution)
        self.plot_publication_time_button.grid(row=5, column=1, padx=5, pady=5)

        self.display_dataframe_button = tk.Button(self, text="Display Cleaned DataFrame", command=self.display_dataframe)
        self.display_dataframe_button.grid(row=5, column=2, padx=5, pady=5)

        # Row 6 for new visualizations
        self.plot_sentiment_analysis_button = tk.Button(self, text="Plot Sentiment Analysis", command=self.plot_sentiment_analysis)
        self.plot_sentiment_analysis_button.grid(row=6, column=0, padx=5, pady=5)

        self.plot_trending_keywords_button = tk.Button(self, text="Plot Trending Keywords", command=self.plot_trending_keywords)
        self.plot_trending_keywords_button.grid(row=6, column=1, padx=5, pady=5)

        self.gui_with_image = tk.Button(self, text="Headlines with related image", command=self.imageGUI)
        self.gui_with_image.grid(row=6,column=2,padx=5,pady=5)

    def fetch_news(self):
        category = self.clicked.get()

        news_api = NewsAPI(self.api_key)
        web_scraper = WebScraper()
        data_processor = DataProcessor()

        try:
            api_data = news_api.fetch_news(category=category)
            self.articles = api_data.get('articles', [])
            combined_data = []

            for article in api_data['articles']:
                try:
                    scraped_data = web_scraper.scrape_article(article['url'])
                    combined_data.append(data_processor.combine_data([article], {article['url']: scraped_data})[0])
                except Exception as e:
                    print(f"Error scraping article {article['url']}: {e}")

            self.cleaned_data = data_processor.clean_data(combined_data)

            self.articles = self.cleaned_data.to_dict('records')
            self.display_articles()
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def display_articles(self):
        self.articles_listbox.delete(0, tk.END)
        for article in self.articles:
            self.articles_listbox.insert(tk.END, article['title'])

    def show_article_details(self):
        selected_index = self.articles_listbox.curselection()
        if not selected_index:
            messagebox.showwarning("Warning", "Please select an article to view details.")
            return

        article = self.articles[selected_index[0]]
        details = (
            f"Title: {article['title']}\n"
            f"Author: {article.get('author', 'N/A')}\n"
            f"Publication Date: {article.get('publishedAt', 'N/A')}\n"
            f"Source: {article['source']['name']}\n\n"
            f"Content:\n{article.get('content', 'Content not available')}"
        )
        messagebox.showinfo("Article Details", details)

    def plot_source_distribution(self):
        if not hasattr(self, 'cleaned_data'):
            messagebox.showwarning("Warning", "Please fetch news data first.")
            return
        viz = DataVisualization(self.cleaned_data)
        viz.plot_article_distribution_by_source()

    def plot_author_distribution(self):
        if not hasattr(self, 'cleaned_data'):
            messagebox.showwarning("Warning", "Please fetch news data first.")
            return
        viz = DataVisualization(self.cleaned_data)
        viz.plot_article_distribution_by_author()

    def plot_article_lengths(self):
        if not hasattr(self, 'cleaned_data'):
            messagebox.showwarning("Warning", "Please fetch news data first.")
            return
        viz = DataVisualization(self.cleaned_data)
        viz.plot_article_lengths()

    def plot_articles_over_time(self):
        if not hasattr(self, 'cleaned_data'):
            messagebox.showwarning("Warning", "Please fetch news data first.")
            return
        viz = DataVisualization(self.cleaned_data)
        viz.plot_articles_over_time()

    def plot_correlation_heatmap(self):
        if not hasattr(self, 'cleaned_data'):
            messagebox.showwarning("Warning", "Please fetch news data first.")
            return
        viz = DataVisualization(self.cleaned_data)
        viz.plot_correlation_heatmap()

    def plot_wordcloud_for_titles(self):
        if not hasattr(self, 'cleaned_data'):
            messagebox.showwarning("Warning", "Please fetch news data first.")
            return
        viz = DataVisualization(self.cleaned_data)
        viz.plot_wordcloud_for_titles()

    def plot_top_authors(self):
        if not hasattr(self, 'cleaned_data'):
            messagebox.showwarning("Warning", "Please fetch news data first.")
            return
        viz = DataVisualization(self.cleaned_data)
        viz.plot_top_authors()

    def plot_publication_time_distribution(self):
        if not hasattr(self, 'cleaned_data'):
            messagebox.showwarning("Warning", "Please fetch news data first.")
            return
        viz = DataVisualization(self.cleaned_data)
        viz.plot_publication_time_distribution()

    def plot_sentiment_analysis(self):
        if not hasattr(self, 'cleaned_data'):
            messagebox.showwarning("Warning", "Please fetch news data first.")
            return
        viz = DataVisualization(self.cleaned_data)
        viz.plot_sentiment_analysis()

    def plot_trending_keywords(self):
        if not hasattr(self, 'cleaned_data'):
            messagebox.showwarning("Warning", "Please fetch news data first.")
            return
        viz = DataVisualization(self.cleaned_data)
        viz.plot_trending_keywords()

    def display_dataframe(self):
        if not hasattr(self, 'cleaned_data'):
            messagebox.showwarning("Warning", "Please fetch news data first.")
            return

        # Create a new window to display the DataFrame
        window = tk.Toplevel(self)
        window.title("DataFrame Display")
        window.geometry("800x600")

        # Create a Treeview widget to display the DataFrame
        tree = ttk.Treeview(window, columns=list(self.cleaned_data.columns), show='headings')
        tree.pack(expand=True, fill=tk.BOTH)

        # Set up column headings
        for col in self.cleaned_data.columns:
            tree.heading(col, text=col)
            tree.column(col, width=100, anchor=tk.CENTER)

        # Insert DataFrame rows into the Treeview
        for index, row in self.cleaned_data.iterrows():
            tree.insert("", tk.END, values=list(row))

        # Add a scrollbar
        scrollbar = ttk.Scrollbar(tree, orient='vertical', command=tree.yview)
        tree.configure(yscroll=scrollbar.set)
        scrollbar.pack(side='right', fill='y')

        # Add a scrollbar to the Treeview
        scrollbar2 = ttk.Scrollbar(tree, orient='horizontal', command=tree.xview)
        tree.configure(xscroll=scrollbar2.set)
        scrollbar2.pack(side='bottom', fill='x')

    def imageGUI(self):
        subprocess.Popen(['python','url_IMG.py'])