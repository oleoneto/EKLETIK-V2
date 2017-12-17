"""
 newsapi.py
 By Leo N.
 An implementation of the News API.
 Requirements: Python 3+, Internet, News API Key.

"""

# Importing Python web modules
import random, json, urllib.parse, requests


def NewsObjects(keyword):

    NEWS = []
    ARTICLES = []
    key = "f355c018b1474aef93c183aebcb3b845"

    api = 'https://newsapi.org/v2/top-headlines?sources=bbc-news,associated-press,abc-news,cbc-news,engadget,the-economist,the-guardian-au&apiKey=' + key

    if keyword:
        if len(keyword) > 1:
            api = 'https://newsapi.org/v2/everything?q='+ keyword +'&from=2017-12-15&to=2017-12-15&sortBy=popularity&apiKey=' + key

    data = requests.get(
        api,).json()

    size = len(data['articles'])

    for i in range(size):
        ARTICLES.insert(i, data['articles'][i])

    return ARTICLES

# ------------------------------- #

def main():
    print(NewsObjects("Artificial Intelligence"))

# ------------------------------- #

if __name__ == '__main__':
    main()
