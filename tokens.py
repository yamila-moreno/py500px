from settings import KEY, SECRET, CALLBACK_URL, ENDPOINT
from requests_oauthlib import OAuth1Session
import requests

request_token_url = ''.join([ENDPOINT, 'oauth/request_token'])
authorization_base_url = ''.join([ENDPOINT, 'oauth/authorize'])
access_token_url = ''.join([ENDPOINT, 'oauth/access_token'])

# 2. Fetch a request token
dpx = OAuth1Session(KEY,
                    client_secret=SECRET,
                    callback_uri=CALLBACK_URL)
dpx.fetch_request_token(request_token_url)

# 3. Redirect user to 500px for authorization
authorization_url = dpx.authorization_url(authorization_base_url)
print('Please go here and authorize,', authorization_url)

# 4. Get the authorization verifier code from the callback url
redirect_response = input('Paste the full redirect URL here:')
dpx.parse_authorization_response(redirect_response)

# 5. Fetch the access token
response = dpx.fetch_access_token(access_token_url)
print('Save those tokens in the settings.py file')
print('oauth_token:', response.get('oauth_token'))
print('oauth_token_secret:', response.get('oauth_token_secret'))
