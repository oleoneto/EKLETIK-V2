import soundcloud

cid = 'oleoneto'

# create a client object with your app credentials
client = soundcloud.Client(client_id=cid)

# get a tracks oembed data
track_url = 'http://soundcloud.com/oleoneto/a-voz'
embed_info = client.get('/oembed', url=track_url)

# print the html for the player widget
print(embed_info['html'])