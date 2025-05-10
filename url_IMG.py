import io
import webbrowser
import requests
from tkinter import *
from urllib.request import urlopen
from PIL import ImageTk, Image

class NewsApp:
    def __init__(self, root):
        self.root = root
        self.root.geometry('600x700+0+0')
        self.root.resizable(0, 0)
        self.root.title('News App')
        self.root.configure(background='gainsboro')

        self.newsCatButton = []
        self.newsCat = ["general", "entertainment", "business", "sports", "technology", "health", "science"]

        F2 = LabelFrame(self.root, text="Category", font=(
            "times new roman", 20, "bold"), bg='azure', fg='pink4', bd=10)
        F2.pack(side=LEFT)

        for i in range(len(self.newsCat)):
            b = Button(F2, text=self.newsCat[i].upper(
            ), width=15, bd=2, font="arial 15 bold")
            b.grid(row=i, column=0, padx=10, pady=5)
            b.bind('<Button-1>', self.load_news_item)
            self.newsCatButton.append(b)

    def clear(self):
        for i in self.root.place_slaves():
            i.destroy()

    def load_news_item(self, event):
        category = event.widget.cget('text').lower()
        self.data = requests.get(
            f'http://newsapi.org/v2/top-headlines?country=us&category={category}&apiKey=793e5223f292469393b739eacd25c7eb').json()
        self.display_article(0)

    def display_article(self, index):
        self.clear()
        article = self.data['articles'][index]
        img_url = article.get('urlToImage', 'https://www.hhireb.com/wp-content/uploads/2019/08/default-no-img.jpg')
        
        try:
            raw_data = urlopen(img_url).read()
            im = Image.open(io.BytesIO(raw_data)).resize((350, 250))
            photo = ImageTk.PhotoImage(im)
        except:
            raw_data = urlopen('https://www.hhireb.com/wp-content/uploads/2019/08/default-no-img.jpg').read()
            im = Image.open(io.BytesIO(raw_data)).resize((350, 250))
            photo = ImageTk.PhotoImage(im)

        F1 = Frame(self.root, bg='gainsboro')
        F1.place(x=251, y=0, width=350)

        label = Label(F1, image=photo)
        label.photo = photo
        label.pack()

        heading = Label(F1, text=article['title'], bg='gainsboro', fg='black', wraplength=350, justify='center')
        heading.pack(pady=(0, 20))
        heading.config(font=('verdana 15 bold underline'))

        details = Label(F1, text=article['description'], bg='white', fg='black', wraplength=350, justify='center')
        details.pack(pady=(0, 20))
        details.config(font=('verdana', 12))

        pdate = Label(F1, text=article['publishedAt'], bg='white', fg='black', wraplength=350, justify='right')
        pdate.pack(pady=(0, 10))
        pdate.config(font=('verdana', 12))

        frame = Frame(F1, bg='gainsboro')
        frame.pack(expand=True, fill=BOTH, side=BOTTOM, pady=(0, 20))

        if index != 0:
            prev = Button(frame, text='Prev', width=16, height=3, command=lambda: self.display_article(index - 1))
            prev.pack(side=LEFT)

        read = Button(frame, text='Read More', width=16, height=3, command=lambda: self.open_link(article['url']))
        read.pack(side=LEFT)

        if index != len(self.data['articles']) - 1:
            next = Button(frame, text='Next', width=16, height=3, command=lambda: self.display_article(index + 1))
            next.pack(side=LEFT)

    def open_link(self, url):
        webbrowser.open(url)

if __name__ == '__main__':
    root = Tk()
    obj = NewsApp(root)
    root.mainloop()