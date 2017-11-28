import sys
import spotipy
import spotipy.util as util
import json, urllib, requests

cid = 'de8419b6b859449eb41e4d375de68c97'
cst = '15ee8c93cfc54889b95658c58140bc49'
token = util.oauth2.SpotifyClientCredentials(client_id=cid, client_secret=cst)
cache_token = token.get_access_token()
spotify = spotipy.Spotify(cache_token)

def SampleCall():
    username = '1292741452'
    if len(username) > 1:
        username = username
    else:
        print("Whoops, need your username!")
        print("usage: python user_playlists.py [username]")
        sys.exit()

    if username:
        sp = spotify
        playlists = sp.user_playlists(username)
        for playlist in playlists['items']:
            print(playlist['tracks'])
    else:
        print("Can't get token for", username)

# ----------------------------

# spotify:user:1292741452:playlist:6LBfB2JA0u3YyHY0mAVjc3

def BuildTracks():
    api = 'https://api.spotify.com/v1/users/1292741452/playlists/6LBfB2JA0u3YyHY0mAVjc3/tracks'
    data = requests.get(
        api,
        headers={"Authorization": "Bearer " + cache_token, },
        verify=True,
    ).json()

    size = len(data['items'])

    # Make sure this array remains here...
    AUDIOS = []

    for i in range(size):
        audio = data['items'][i]['track']
        AUDIOS.insert(i, audio)
        # print(AUDIOS[i]['name'])
        # print(AUDIOS[i]['album']['name'])
        # print(AUDIOS[i]['artists'][0]['name'])
        # print(AUDIOS[i]['album']['images'][0]['url'])
        # print(AUDIOS[i]['preview_url'])
        # print(AUDIOS[i]['duration_ms'])
        # print("-----------------------------")

    a = AUDIOS
    return a

# ----------------------------

def main():
    BuildTracks()


if __name__ == "__main__":
    main()
