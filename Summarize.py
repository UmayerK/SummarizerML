#all Libraries neeeded declared here
import tkinter as tk

import nltk
from textblob import TextBlob
from newspaper import Article

#Summarize Function
def summarize():
    #main start
    #making a new article object and then passing the url into it and parsing

    url = utext.get('1.0', "end").strip()
    article = Article(url)
    article.download()
    article.parse()

    #call nlp to summarize the article using machine language
    article.nlp()

    title.config(state='normal')
    author.config(state='normal')
    pubd.config(state='normal')
    summary.config(state='normal')
    sent.config(state='normal')

    title.delete('1.0', 'end')
    title.insert('1.0', article.title)

    author.delete('1.0', 'end')
    author.insert('1.0', article.authors)

    pubd.delete('1.0', 'end')
    pubd.insert('1.0', article.publish_date)

    summary.delete('1.0', 'end')
    summary.insert('1.0', article.summary)

    # this esentially takes the article and does an analysis on it
    # Create analysis object pass article into it
    analysis = TextBlob('article.text')
    sent.delete('1.0', 'end')
    # polarity means if this is a happy or sad or neutral tone
    print(analysis.polarity)
    # logic for determining what type of tone this article is
    sent.insert('1.0', f'Sentiment: {"Positive" if analysis.polarity > 0 else "Negative" if analysis.polarity < 0 else "Neutral"} ')

    title.config(state='disabled')
    author.config(state='disabled')
    pubd.config(state='disabled')
    summary.config(state='disabled')
    sent.config(state='disabled')






#make a gui and make a base tkinter module
root = tk.Tk()
root.title("USummarizer")
root.geometry('1200x600')


#url
ulab= tk.Label(root, text="Enter your URL:")
ulab.pack()
utext = tk.Text(root, height=1, width=140)
utext.pack()


#title of article
lableT = tk.Label(root, text="Article Title")
lableT.pack()
title = tk.Text(root, height=1, width=140)
title.config(state= 'disabled', bg='#dddddd')
title.pack()

#author(s) of article
alab= tk.Label(root, text="Written by:")
alab.pack()
author = tk.Text(root, height=1, width=140)
author.config(state= 'disabled', bg='#dddddd')
author.pack()

#publication date
plab= tk.Label(root, text="Published:")
plab.pack()
pubd = tk.Text(root, height=1, width=140)
pubd.config(state= 'disabled', bg='#dddddd')
pubd.pack()

#Sentiment Analysis
selab= tk.Label(root, text="Tone:")
selab.pack()
sent = tk.Text(root, height=1, width=140)
sent.config(state= 'disabled', bg='#dddddd')
sent.pack()

#The Summary of the article
slab= tk.Label(root, text="Summary:")
slab.pack()
summary= tk.Text(root, height=20, width=140)
summary.config(state= 'disabled', bg='#dddddd')
summary.pack()

#button
button= tk.Button(root, text= "Summarize", command=summarize)
button.pack()





root.mainloop()



