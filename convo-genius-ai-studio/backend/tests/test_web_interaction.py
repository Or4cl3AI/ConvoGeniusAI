```python
import requests
from bs4 import BeautifulSoup

def fetch_website_data(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        return None

def extract_data_from_html(html):
    soup = BeautifulSoup(html, 'html.parser')
    # Add code here to extract the desired data from the HTML
    return data

def test_fetch_website_data():
    url = "https://www.example.com"
    html = fetch_website_data(url)
    assert html is not None

def test_extract_data_from_html():
    html = "<html><body><h1>Hello, World!</h1></body></html>"
    data = extract_data_from_html(html)
    assert data == "Hello, World!"

if __name__ == "__main__":
    test_fetch_website_data()
    test_extract_data_from_html()
    print("All tests passed!")
```
