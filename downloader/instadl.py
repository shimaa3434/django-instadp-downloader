import requests

url = "https://instagram40.p.rapidapi.com/account-info"


def get_insta_user_data(username):
    querystring = {"username": username}

    headers = {
        'x-rapidapi-key': "0c8a0f1269msh55c1b3929770a46p12c5cdjsn80e59a973e98",
        'x-rapidapi-host': "instagram40.p.rapidapi.com"
    }
    r = requests.request(
        "GET", url, headers=headers, params=querystring).json()
    user_data = {
        'full_name': r['full_name'],
        'bio': r['biography'],
        'following': r['edge_follow']['count'],
        'follower': r['edge_followed_by']['count'],
        'pic_url': r['profile_pic_url_hd']
    }
    return user_data
