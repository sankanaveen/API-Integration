
# coding: utf-8

# ...
# NYTimes API call - Most Popular API
# You can get most popular articles based on - Views, Shared and Emailed
# 
# Weblink - https://developer.nytimes.com/
# Get API_KEY from above link.
# ...

# In[ ]:

import json
import codecs
import requests

URL_MAIN = "http://api.nytimes.com/svc/"
URL_POPULAR = URL_MAIN + "mostpopular/v2/"
API_KEY = { "popular": ""}    #API_KEY to be placed here

def get_popular(url, kind, days, section="all-sections", offset=0):
    # This function will construct the query according to the requirements of the site
    # and return the data, or print an error message if called incorrectly
    if days not in [1,7,30]:
        print("Time period can be 1,7, 30 days only")
        return False
    if kind not in ["viewed", "shared", "emailed"]:
        print("kind can be only one of viewed/shared/emailed")
        return False

    url += "most{0}/{1}/{2}.json".format(kind, section, days)
    data = query_site(url, "popular", offset)

    return data

def query_site(url, target, offset):
    # This will set up the query with the API key and offset
    # Web services often use offset paramter to return data in small chunks
    # NYTimes returns 20 articles per request, if you want the next 20
    # You have to provide the offset parameter
    if API_KEY["popular"] == "":
        print("You need to register for NYTimes Developer account to run this program.")
        print("See Intructor notes for information")
        return False
    params = {"api-key": API_KEY[target], "offset": offset}
    r = requests.get(url, params = params)

    if r.status_code == requests.codes.ok:
        return r.json()
    else:
        r.raise_for_status()

get_popular(URL_POPULAR,"viewed",30)

