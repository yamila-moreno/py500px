Simple Python 3 application to use the 500px.com api

This is a little script to do some bulk editions on 500px photos. I have just started it with my own needs, but feel free to open a PR with a new functionality or just open an issue in this repository.

Authentication
==============

To use this library, you need to configurate the authentication, with oauth1. I have added a little script to help you.

First of all, rename the file called `settings.py.example` to `settings.py`

Then, you need to `Register` a new application here: https://500px.com/settings/applications. You'll find a form with the following mandatory fields:

* Application name. For instance: "My access"
* Description. You can write the same as the name or you can go original :)
* Application URL. This URL won't be used, so you can put whatever you want, or even `http://127.0.0.1`
* Developer's email. Your own email.

Once you have filled the form, you'll get two keys:
* customer key. Copy this key in the settings file, replacing the 'xxxx' of KEY variable.
* customer secret. Copy this key in the settings file, replacing the 'xxxx' of SECRET variable.

Now you have to execute `tokens.py` script and follow the instructions:

    $ python tokens.py

When finished, you wil obtain other two keys:
* oauth_token. Copy this key in the settings file, replacing the 'xxxx' of OAUTH_TOKEN variable.
* oauth_token_secret. Copy this key in the settings file, replacing the 'xxxx' of OAUTH_TOKEN_SECRET variable.

Well, that's all. Now you can use the script to edit your photos in 500px.

Usage
=====

Get collections
---------------

    $ python 500px.py --action collections


Add a tag to all the photos of one collection
---------------------------------------------

    $ python 500px.py --action set_tag --col_id ID --tag NEW_TAG


Set a name for all the photos in a collection
---------------------------------------------

If you upload a whole directory and you don't want to set the title to each photo, you may find useful to set one title for all the photos in a collection:

    $ python 500px.py --action set_name --col_id ID --name NAME


Note: the official documentation seems to be deprecated. Instead, the online api works fine, so this code follows that online console at: https://apigee.com/vova/embed/console/api500px
