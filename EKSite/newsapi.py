"""

 newsapi.py
 By Leo N.
 An implementation of the News API.
 Requirements: Python 3+, Internet, News API Key.

"""

# Importing Python web modules
import random, json, urllib.parse, requests

# Developer API key
key = "f355c018b1474aef93c183aebcb3b845"


# Articles array
NEWS = []
ARTICLES = []
TITLES = []

# API Endpoint: Querying News
api = 'https://newsapi.org/v2/top-headlines?sources=bbc-news,associated-press,abc-news,cbc-news,engadget,the-economist,the-guardian-au&apiKey='+key


def NewsObjects():
    data = requests.get(
        api,
        verify = True,
    ).json()

    size = len(data['articles'])

    for i in range(size):
        ARTICLES.insert(i, data['articles'][i])



    count = 0

    for news in ARTICLES:
        # print(news['title'])
        TITLES.insert(i, news['title'])
        if news['title'] not in TITLES:
            NEWS.insert(count, news)
            # print(NEWS['articles'][count]['title'])
        count = count + 1

    return ARTICLES



# ------------------------------- #

def main():
    news = NewsObjects()

# ------------------------------- #

if __name__ == '__main__':
    main()
