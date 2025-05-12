import io
import webbrowser
import requests
from tkinter import *
from tkinter import ttk
from urllib.request import urlopen
from PIL import ImageTk, Image

class NewsApp:
    def __init__(self, root):
        self.root = root
        self.root.title("News Aggregator")
        self.root.geometry("850x700")
        self.root.configure(bg='white')

        self.newsCat = ["general", "entertainment", "business", "sports", "technology", "health", "science"]
        self.newsCatButton = []

        self.create_layout()

    def create_layout(self):
        # Left sidebar for category buttons
        self.sidebar = Frame(self.root, bg='lightgray', width=200)
        self.sidebar.pack(side=LEFT, fill=Y)

        Label(self.sidebar, text="Categories", font=("Arial", 16, "bold"), bg='lightgray').pack(pady=10)

        for cat in self.newsCat:
            btn = Button(self.sidebar, text=cat.title(), font=("Arial", 12), width=20, bg="white", command=lambda c=cat: self.load_news(c))
            btn.pack(pady=5)
            self.newsCatButton.append(btn)

        # Right main content area
        self.content_frame = Frame(self.root, bg='white')
        self.content_frame.pack(side=RIGHT, fill=BOTH, expand=True)

        self.canvas = Canvas(self.content_frame, bg='white')
        self.scroll_y = Scrollbar(self.content_frame, orient=VERTICAL, command=self.canvas.yview)
        self.scroll_frame = Frame(self.canvas, bg='white')

        self.scroll_frame.bind("<Configure>", lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")))
        self.canvas.create_window((0, 0), window=self.scroll_frame, anchor="nw")
        self.canvas.configure(yscrollcommand=self.scroll_y.set)

        self.canvas.pack(side=LEFT, fill=BOTH, expand=True)
        self.scroll_y.pack(side=RIGHT, fill=Y)

    def clear_content(self):
        for widget in self.scroll_frame.winfo_children():
            widget.destroy()

    def load_news(self, category):
        self.clear_content()
        try:
            url = f"https://newsapi.org/v2/top-headlines?country=us&category={category}&apiKey=793e5223f292469393b739eacd25c7eb"
            self.data = requests.get(url).json()
            for index, article in enumerate(self.data['articles']):
                self.display_article(article, index)
        except Exception as e:
            Label(self.scroll_frame, text=f"Error fetching news: {str(e)}", fg="red", bg="white").pack()

    def display_article(self, article, index):
        article_frame = Frame(self.scroll_frame, bd=2, relief=RIDGE, bg="white", padx=10, pady=10)
        article_frame.pack(padx=10, pady=10, fill=X)

        img_url = article.get("urlToImage", "https://www.hhireb.com/wp-content/uploads/2019/08/default-no-img.jpg")
        try:
            raw_data = urlopen(img_url).read()
            im = Image.open(io.BytesIO(raw_data)).resize((100, 80))
            photo = ImageTk.PhotoImage(im)
        except:
            photo = None

        if photo:
            img_label = Label(article_frame, image=photo, bg="white")
            img_label.image = photo
            img_label.grid(row=0, column=0, rowspan=3, padx=5)

        title = Label(article_frame, text=article.get("title", ""), font=("Arial", 14, "bold"), bg="white", wraplength=600, justify=LEFT)
        title.grid(row=0, column=1, sticky="w")

        desc = Label(article_frame, text=article.get("description", ""), font=("Arial", 11), bg="white", wraplength=600, justify=LEFT)
        desc.grid(row=1, column=1, sticky="w", pady=5)

        date = Label(article_frame, text=article.get("publishedAt", ""), font=("Arial", 9, "italic"), fg="gray", bg="white")
        date.grid(row=2, column=1, sticky="w")

        btn = Button(article_frame, text="Read More", command=lambda url=article["url"]: self.open_link(url), bg="lightblue")
        btn.grid(row=0, column=2, rowspan=3, padx=10)

    def open_link(self, url):
        webbrowser.open(url)

if __name__ == "__main__":
    root = Tk()
    app = NewsApp(root)
    root.mainloop()
