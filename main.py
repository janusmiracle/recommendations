from credentials import get_client_id, get_client_secret
from authorization import authorization
# Other
import webbrowser
from urllib.parse import urlencode
import requests
import json
import urllib.request

# Query Parameters // Set Client ID and Client Secret
CLIENT_ID = get_client_id()
CLIENT_SECRET = get_client_secret()
BASE_URL = 'https://api.spotify.com/v1/search'

# Get access token
access_token = authorization(CLIENT_ID, CLIENT_SECRET)

# Inputs
search_query = input("Enter song/album name: ")
url_query = input("Enter track or album (case sensitive): ")
output = int(input("""Enter number of images -->

                    1 outputs a single image, 2 outputs 3 images of differing sizes.
                    
                    More than 2 determines the number of results (e.g. 3 gives the first 2 track results images): """))


# Obtain search data
def get_cover(search_query, url_query, output, access_token):
    
    # Obtain search data
    headers = {
                "Authorization": "Bearer {}".format(access_token) # header parameter w/ authorization
            }


    data = urlencode({"q": search_query, "type": url_query.lower()}) # query & type parameter // url_query must be undercase

    url = "{}?{}".format(BASE_URL, data)
    # run request (uses GET this time rather than POST)
    response = requests.get(url, headers=headers)

    # search data
    search_data = response.json()
    # indicates status (200 is ok, 404 is not found and 400 is a 'bad request')

    # initalize count
    count = 1

    # Obtain cover art
    for i in search_data["tracks"]["items"]:
        print("")
        print("Track Name: {}".format(i["name"]))
        print("----------------------------------")

        for j in i["album"]["images"]:
            cover_url = j["url"]
            
            # open image
            webbrowser.open(cover_url)
            #print("""Cover Art: {}x{}
                    
    #{}""".format(j["height"], j["width"], j["url"]))#j["name"],, ["url"]))
            #print("")
            
        count += 1
        if count == output:
            break

    return cover_url

# Call function
get_cover(search_query, url_query, output, access_token)
#print(cover_url)

