#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 27 14:46:34 2019

@author: mackenziemitchell
"""

import streamlit as st
import spotipy
import spotipy.util as util
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy.oauth2 as oauth2

market = [ "AD", "AR", "AT", "AU", "BE", "BG", "BO", "BR", "CA", "CH", "CL", "CO", "CR", "CY", 
      "CZ", "DE", "DK", "DO", "EC", "EE", "ES", "FI", "FR", "GB", "GR", "GT", "HK", "HN", "HU", 
      "ID", "IE", "IS", "IT", "JP", "LI", "LT", "LU", "LV", "MC", "MT", "MX", "MY", "NI", "NL", 
      "NO", "NZ", "PA", "PE", "PH", "PL", "PT", "PY", "SE", "SG", "SK", "SV", "TH", "TR", "TW", 
      "US", "UY", "VN" ]
CLIENT_ID ='d93af13f2f6343c4b7d9e81ba8f29663' 
CLIENT_SECRET = '96842fd0fdc74a739bd6d82c176b090b'

credentials = oauth2.SpotifyClientCredentials(
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET)

token = credentials.get_access_token()
sp = spotipy.Spotify(auth=token)

def get_seeds():
    seeds=st.text_input("Type a few of your favorite artists:")
    seeds=seeds.split(',')
    return seeds

seeds=get_seeds()

def ids(seeds):
    seed_ids=[]
    for seed in seeds:
        try:
            seed_ids.append(sp.search(q='artist: '+ seed, type='artist')['artists']['items'][0]['id'])
        except:
            continue
    return seed_ids

def get_recs(seeds,seed_ids):
    recs=sp.recommendations(seed_artists=seed_ids)
    artists=[]
    rec_uris=[]
    for r in recs['tracks']:
        for i in r['artists']:
            if i['name'].lower() not in seeds and i['name'] not in artists:
                print(i['name'].lower())
                artists.append(i['name'])
                rec_uris.append(i['id'])
    return artists
                
def print_recs(artists):
    st.write(artists)

#seeds=get_seeds()
seed_ids=ids(seeds)
artists=get_recs(seeds,seed_ids)
get_recs(artists)


