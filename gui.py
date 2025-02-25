import tkinter as tk
from tkinter import scrolledtext
import requests

# Function to fetch stock news
def get_news():
    ticker = entry.get()
    if not ticker:
        result_text.insert(tk.END, "Please enter a stock ticker.\n")
        return

    url = f"https://newsapi.org/v2/everything?q={ticker}&apiKey=YOUR_NEWSAPI_KEY"
    response = requests.get(url).json()

    result_text.delete("1.0", tk.END)  # Clear previous results

    if "articles" in response:
        for article in response["articles"][:5]:
            result_text.insert(tk.END, f"Title: {article['title']}\n")
            result_text.insert(tk.END, f"Link: {article['url']}\n\n")
    else:
        result_text.insert(tk.END, "No news found.\n")

# GUI Setup
root = tk.Tk()
root.title("Stock News Scraper")
root.geometry("500x400")

tk.Label(root, text="Enter Stock Ticker:").pack()
entry = tk.Entry(root)
entry.pack()

btn = tk.Button(root, text="Get News", command=get_news)
btn.pack()

result_text = scrolledtext.ScrolledText(root, height=15)
result_text.pack()

root.mainloop()
