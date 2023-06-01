import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import json

songlist=[]
trackUris = []

class Song:
        def __init__(self, name, uri, artistName, package):
            self.name = name
            self.uri = uri
            self.artist = artistName
            self.package = package

"""
Gets the data for each song in the playlist and adds it to songlist.
"""
def getPlayList(playlistURL, songlist):
    playlist_uri = playlistURL.split("/")[-1].split("?")[0]
    curPlaylistUris = [x["track"]["uri"] for x in sp.playlist_tracks(playlist_uri)["items"]]
    trackUris.append(curPlaylistUris) # records each playlist as URI

    for song in sp.playlist_tracks(playlist_uri)["items"]:
        track_uri = song["track"]["uri"]
        track_name = song["track"]["name"]
        artist_name = song["track"]["artists"][0]["name"]
        audio_features = sp.audio_features(track_uri)[0]

        eachSong = Song(track_name, track_uri, artist_name, audio_features)
        songlist.append(eachSong)

"""
Converts data to JSON format and outputs to file "data.json"
"""
def convertJSON(songlist):
    dict = {}
    for i in range(len(songlist)):
        dict[songlist[i].name + "*" + songlist[i].artist] = songlist[i].package
    with open("data.json", "w") as outfile:
        json.dump(dict, outfile, indent=4)

"""
Prompts user to enter playlist URLs and populates songlist
with songs from the given playlists
"""
if __name__ == "__main__":
    sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())
    while(1):
        playlistLink = input("enter playlist URL: ")
        print("Loading...")
        getPlayList(playlistLink, songlist)
        finish = input(" More playlists? n for no, y for yes: ")
        if finish == "n":
            break
    convertJSON(songlist)
    print("data.json file created with songs from user playlists")
