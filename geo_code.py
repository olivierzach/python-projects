# -*- coding: utf-8 -*-
"""
Created on Thu Apr  5 15:34:46 2018

@author: zolivier
"""
# install mechanical soup by using the pip operator
# we need to use ! in order to send the command outside of Ipython

#!pip install mechanicalsoup

#https://github.com/googlemaps/google-maps-services-python

import requests    
    
url = 'https://www.latlong.net/convert-address-to-lat-long.html'
caption = 'lat coordinate:'

form_data = {
        'address': '3323 east casselle orange CA',
        'find': 'find',
    }


response = requests.post(url = url, data=form_data)

print(response.status_code, response.reason)

print(response.text)


    