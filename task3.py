import requests
from bs4 import BeautifulSoup

# Base URL of the website to scrape
base_url = 'http://quotes.toscrape.com/page/'

page = 1
while True:
    # Send a GET request to the current page
    response = requests.get(f"{base_url}{page}/")
    
    # Check if the request was successful
    if response.status_code != 200:
        print("No more pages to scrape.")
        break
    
    # Parse the HTML content of the page
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find all quotes
    quotes = soup.find_all('span', class_='text')
    authors = soup.find_all('small', class_='author')
    tags = soup.find_all('div', class_='tags')

    # Extract and print the text from each quote
    for i in range(len(quotes)):
        quote = quotes[i].get_text()
        author = authors[i].get_text()
        quote_tags = [tag.get_text() for tag in tags[i].find_all('a', class_='tag')]
        
        print(f"{(page-1)*10 + i + 1}. {quote} - {author}")
        print(f"Tags: {', '.join(quote_tags)}\n")

    # Check if there is a next page
    next_page = soup.find('li', class_='next')
    if not next_page:
        print("No more pages to scrape.")
        break

    page += 1