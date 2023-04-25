import requests
from bs4 import BeautifulSoup

# send a GET request to the website
url = 'https://www.bbc.com/news'
response = requests.get(url)

# parse the HTML content using Beautiful Soup
soup = BeautifulSoup(response.text, 'html.parser')

# extract the data you want
title = soup.find('title').text
articles = soup.find_all('h3', class_='gs-c-promo-heading__title gel-pica-bold nw-o-link-split__text')

# print the results
print(title)
for article in articles:
    print(article.text.strip())

    # save the results to a text file
    with open('random/bbc_news.txt', 'w', encoding='utf-8') as file:
        file.write(title + '\n')
        for article in articles:
            file.write(article.text.strip() + '\n')