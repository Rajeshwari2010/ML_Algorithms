import requests
from bs4 import BeautifulSoup

url = "https://books.toscrape.com/"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

books = soup.find_all("article", class_="product_pod")

for b in books:
    title = b.h3.a['title']
    price = b.find("p", class_="price_color").text
    print(title, "-", price)


#webscraping with mutlithreading
import threading
import requests

urls = [
    "https://httpbin.org/delay/2",
    "https://httpbin.org/delay/3",
    "https://httpbin.org/delay/1"
]

results = {}

def fetch(url):
    try:
        print(f"Fetching: {url}")
        response = requests.get(url)
        results[url] = response.status_code
    except Exception as e:
        results[url] = f"Error: {e}"

threads = []

# Create & start threads
for url in urls:
    t = threading.Thread(target=fetch, args=(url,))
    threads.append(t)
    t.start()

# Wait for all threads to finish
for t in threads:
    t.join()

# Print results
for url, status in results.items():
    print(f"{url} --> {status}")
