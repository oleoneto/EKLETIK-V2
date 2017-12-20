import spotipy
import spotipy.util as util
import json, urllib, requests

cid = 'de8419b6b859449eb41e4d375de68c97'
cst = '15ee8c93cfc54889b95658c58140bc49'
token = util.oauth2.SpotifyClientCredentials(client_id=cid, client_secret=cst)
cache_token = token.get_access_token()
spotify = spotipy.Spotify(cache_token)
alt = 'https://gist.github.com/oleoneto/61b223b68ca65092032ed3e8bee60d72'
api = 'https://api.spotify.com/v1/users/1292741452/playlists/6LBfB2JA0u3YyHY0mAVjc3/tracks'
alt2 = 'https://gist.githubusercontent.com/oleoneto/61b223b68ca65092032ed3e8bee60d72/raw/4c42444309827d3de06506aef194cdcd15fb4c5a/spotify.json'
# ---------------
# user:1292741452
# playlist:6LBfB2JA0u3YyHY0mAVjc3


def PrintTracks(AUDIOS, i):
    print(AUDIOS[i]['name'])
    print(AUDIOS[i]['album']['name'])
    print(AUDIOS[i]['artists'][0]['name'])
    print(AUDIOS[i]['album']['images'][0]['url'])
    print(AUDIOS[i]['preview_url'])
    print(AUDIOS[i]['duration_ms'])
    print("-----------------------------")

def BuildTracks():

    # Make sure this array remains inside the function...
    AUDIOS = []

    data = requests.get(
        api,
        headers={"Authorization": "Bearer " + cache_token, },
        verify=True,
    ).json()

    if not data:
        data = requests.get(alt).json()

    try:
        size = len(data['items'])
    except KeyError:
        size = 0

    for i in range(size):
        audio = data['items'][i]['track']
        audio['name'] = audio['name'].replace("(Ao Vivo)", "")
        audio['name'] = audio['name'].replace("Live", "")
        audio['name'] = audio['name'].replace("(Faixa Bônus)", "")
        AUDIOS.append(audio)
        PrintTracks(AUDIOS, i)
    return AUDIOS

# ----------------------------


def main():
    BuildTracks()
    variable = 1


if __name__ == "__main__":
    main()
