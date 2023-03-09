# Project imports
from credentials import get_client_id, get_client_secret

# For all imports, sort `import` first then `from`s, in alphabetical order
# Python standard library imports
import json
import base64
from urllib.parse import urlencode

# Third-party imports
import requests


# Query Parameters // Set Client ID and Client Secret
CLIENT_ID = get_client_id()
CLIENT_SECRET = get_client_secret()


def get_access_token(CLIENT_ID, CLIENT_SECRET) -> json:
    # auth_code for header
    auth_code = base64.b64encode(
        (CLIENT_ID + ":" + CLIENT_SECRET).encode("ascii")
    ).decode("ascii")

    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
        "Authorization": "Basic " + auth_code,
    }
    # payload
    payload = {"grant_type": "client_credentials"}

    # post request
    response = requests.post(
        "https://accounts.spotify.com/api/token", data=payload, headers=headers
    )
    # json data
    data = response.json()
    formatted_data = json.dumps(
        response.json(), indent=4
    )  # formats into example from Spotify documentation
    # access token
    token = data["access_token"]
    return token


access_token = get_access_token(CLIENT_ID, CLIENT_SECRET)
