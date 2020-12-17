import re
import requests
import json


header_data = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36"
}


def get_profile_pic_url(usrname):
    url = f"https://www.instagram.com/{usrname}/?__a=1"
    r = requests.get(url, headers=header_data).json()
    return r["graphql"]["user"]["profile_pic_url_hd"]
