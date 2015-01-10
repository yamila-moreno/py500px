from settings import (
    KEY, SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET,
    ENDPOINT)
from requests_oauthlib import OAuth1Session
import requests
import argparse
import json

# ENDPOINTS
COLLECTIONS_URL = ENDPOINT + 'collections/'
COLLECTION_URL = ENDPOINT + 'collections/{col_id}'
PHOTO_URL = ENDPOINT, 'photos/{photo_id}'
ADD_TAG_TO_PHOTO_URL = ENDPOINT + 'photos/{photo_id}/tags?tags={tag}'
SET_NAME_TO_PHOTO_URL = ENDPOINT + 'photos/{photo_id}/?name={name}'

def get_collections(oauth):
    r = oauth.get(COLLECTIONS_URL)
    collections = json.loads(r.text)['collections']
    for c in collections:
        print('id: {}, title: {}'.format(c['id'], c['title']))

def set_name_for_photos_in_a_collection(oauth, col_id, name):
    r = oauth.get(COLLECTION_URL.format(col_id=col_id))
    photos = json.loads(r.text)['photos']
    for photo in photos:
        r = oauth.put(SET_NAME_TO_PHOTO_URL.format(photo_id=photo['id'], name=name))
    print('ok!')


def set_tag_for_collection(oauth, col_id, tag):
    r = oauth.get(COLLECTION_URL.format(col_id=col_id))
    photos = json.loads(r.text)['photos']
    for photo in photos:
        r = oauth.post(ADD_TAG_TO_PHOTO_URL.format(photo_id=photo['id'], tag=tag))
    print('ok!')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--action', help='Action',
                        choices=['collections', 'set_tag', 'set_name'])
    parser.add_argument('--col_id', help='Collection id')
    parser.add_argument('--tag', help='Tag')
    parser.add_argument('--name', help='Name')
    args = parser.parse_args()

    oauth = OAuth1Session(KEY,
                          client_secret=SECRET,
                          resource_owner_key=OAUTH_TOKEN,
                          resource_owner_secret=OAUTH_TOKEN_SECRET)

    if args.action == 'collections':
        get_collections(oauth)

    elif args.action == 'set_tag':
        col_id = args.col_id
        tag = args.tag
        set_tag_for_collection(oauth, col_id, tag)

    elif args.action == 'set_name':
        col_id = args.col_id
        name = args.name
        set_name_for_photos_in_a_collection(oauth, col_id, name)


