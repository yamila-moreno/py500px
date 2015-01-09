from settings import (
    KEY, SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET,
    ENDPOINT)
import requests
from requests_oauthlib import OAuth1Session

# ENDPOINTS
COLLECTIONS = ''.join([ENDPOINT, 'collections'])
# ENDPOINTS

oauth = OAuth1Session(KEY,
                      client_secret=SECRET,
                      resource_owner_key=OAUTH_TOKEN,
                      resource_owner_secret=OAUTH_TOKEN_SECRET)

r = oauth.get(COLLECTIONS)
print(r.content)
