import requests
import json
header_data = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36"
}


def get_insta_user_data(usrname):
    url = f"https://www.instagram.com/{usrname.lower()}/?__a=1"
    res = requests.get(url, headers=header_data)
    r = json.loads(res.content)
    insta_user_data = {
        'full_name': r['graphql']['user']['full_name'],
        'follower': r['graphql']['user']['edge_followed_by']['count'],
        'following': r['graphql']['user']['edge_follow']['count'],
        'bio': r['graphql']['user']['biography'],
        'pic_url': r['graphql']['user']['profile_pic_url_hd'],
    }
    return insta_user_data


print(get_insta_user_data('sunny._.shankar'))
