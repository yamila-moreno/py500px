from settings import (
    KEY, SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET,
    ENDPOINT)
from requests_oauthlib import OAuth1Session
import requests
import argparse
import json

# ENDPOINTS
COLLECTIONS_URL = ENDPOINT + 'collections/'
COLLECTION_URL = ENDPOINT + 'collections/{col_id}/'
PHOTO_URL = ENDPOINT, 'photos/{photo_id}/'
PHOTO_UPLOAD_URL = ENDPOINT + 'photos/upload/'
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

def create_collection(oauth, name, path):
    url = COLLECTIONS_URL + '?kind=2&title={}&path={}'.format(name, path)
    r = oauth.post(url)
    print(json.loads(r.text)['id'])
    print('ok!')
    return(json.loads(r.text))

def upload_photo_from_url(oauth, photo_url, name):
    files = {
        'file': requests.get(url).content
        }
    url = PHOTO_UPLOAD_URL + '?name=' + name
    r = oauth.post(url, files=files)
    print('ok!')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--action', help='Action',
                        choices=['collections', 'set_tag',
                                 'set_name', 'create_collection',
                                 'upload_photo'])
    parser.add_argument('--col_id', help='Collection id')
    parser.add_argument('--tag', help='Tag')
    parser.add_argument('--name', help='Name')
    parser.add_argument('--path', help='Path or slug')
    parser.add_argument('--photo_url', help='Photo url')
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

    elif args.action == 'create_collection':
        name = args.name
        path = args.path
        create_collection(oauth, name, path)

    elif args.action == 'upload_photo':
        upload_photo(oauth, '', 'kitten')

