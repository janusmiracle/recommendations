from authorization import get_access_token
from credentials import get_client_id, get_client_secret
import json
import requests
import urllib.request
from urllib.parse import urlencode
import webbrowser

endpoint = "https://api.spotify.com/v1/"

class Client:
    _base_url: str
    _access_token: None

    def __init__(self, *, base_url: str = endpoint) -> None:
        self._base_url = base_url

    def _ensure_access_token(self) -> None:
        client_id = get_client_id()
        client_secret = get_client_secret()

        self._access_token = get_access_token(client_id, client_secret)

    def _api_get(self, endpoint: str, params: dict) -> None:
        self._ensure_access_token()

        headers = {"Authorization": "Bearer {}".format(self._access_token)}

        query = urlencode(params)

        url = f"{self._base_url}{endpoint}?{query}"

        data = requests.get(url, headers=headers)

        return data

    def search(self, search_query: str, type_query: str) -> None:
        data = self._api_get("search", {"q": search_query, "type": type_query})

        return data

    def get_cover(self, data) -> None:
        search_data = data.json()

        for track in search_data["tracks"]["items"]:
            print("")
            print("Track Name: {}".format(track["name"]))
            print("----------------------------------")

            for image in track["album"]["images"]:
                cover_url = image["url"]

                # open image
                webbrowser.open(cover_url)
                
            break

client = Client()
data = client.search("song name", "track")
client.get_cover(data)
