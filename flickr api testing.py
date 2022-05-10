# -*- coding: utf-8 -*-
"""
Created on Tue May 10 10:42:25 2022

@author: immom
"""

import requests
response = requests.get("https://www.flickr.com/services/rest/?method=flickr.photos.getPopular&api_key=cdc486273ea3c974d500510354e97ace&user_id=195555550%40N05&format=json&nojsoncallback=1")
print(response.json())
print(response.status_code)
