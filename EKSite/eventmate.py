"""

 EventBrite.py
 By Leo N.
 An implementation of the EventBrite API.
 Requirements: Python 3+, Internet, EventBrite API Key.

"""

# Importing Python web modules
import random, json, urllib.parse, requests

# Developer API key
key = "PU66GQF3VVQ5HODZNZFH"


EVENTS = []
TITLES = []
CITIES = ['Dijon', 'Indianapolis', 'Chicago', 'Phoenix', 'Philadelphia',
          'Boulder', 'CapeTown', 'Luanda', 'Paris', 'Lisbon',
          'Porto', 'SaoPaulo', 'Portland', 'Seattle']

length = len(CITIES)

# API Endpoint: Querying events in a random city
api = "https://www.eventbriteapi.com/v3/events/search/?location.address="



def BuildObjects():
    rand = random.randint(0, length)
    city = CITIES[rand]
    API = api + city

    data = requests.get(
        API,
        headers = { "Authorization": "Bearer " + key,},
        verify = True,).json()

    size = len(data['events'])

    for index in range(size):
        title = data['events'][index]['name']['text']
        singleEvent = data['events'][index]

        EVENTS.insert(index, singleEvent)

        if title not in TITLES:
            TITLES.insert(index, title)

    return EVENTS, TITLES, city






# ------------------------------- #

def main():
    eventObjects = BuildObjects()
    for i in range(len(eventObjects[0])):
        print(eventObjects[0][i]['name']['text'])

# ------------------------------- #

if __name__ == '__main__':
    main()
