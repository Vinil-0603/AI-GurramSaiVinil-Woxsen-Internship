import requests
from bs4 import BeautifulSoup
from datetime import datetime, timedelta
from config import SCRAPE_URL
import time

def scrape_news():
    articles = []
    cutoff_date = datetime.now() - timedelta(days=45)

    response = requests.get(SCRAPE_URL)

    try:
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching page: {e}")
        return articles

    soup = BeautifulSoup(response.content, 'html.parser')
    news_items = soup.find_all('div', class_='newsItem___wZtKx')

    for item in news_items:
        title_element = item.find('div', class_='title___1baLV')
        description_element = item.find('div', class_='description___z7ktb')
        date_element = item.find('div', class_='date___3dzkE')
        url_element = item.find('a', href=True)  

        if title_element and description_element and date_element and url_element:
            title = title_element.text.strip()
            description = description_element.text.strip()
            date_str = date_element.text.strip()
            article_url = url_element['href']

            try:
                date = datetime.strptime(date_str, '%b %d, %Y %H:%M')
            except ValueError:
                print(f"Error parsing date: {date_str}")
                continue  # Skip to the next article if date parsing fails

            if date < cutoff_date:
                break

            articles.append({
                'title': title,
                'description': description,
                'date': date_str,
                'url': article_url
            })

    return articles