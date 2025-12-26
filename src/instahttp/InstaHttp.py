import requests

from .cookiesConstant import cookies
from .headersConstant import headers

def fetch_follower_list(profile_id, max_id=None):
    request_link = "https://www.instagram.com/api/v1/friendships/" + str(profile_id) + "/followers/?count=12&search_surface=follow_list_page"
    if (max_id):
        request_link += "&max_id=" + max_id
    return requests.get(request_link, cookies=cookies, headers=headers).content

def fetch_all_followers(profile_id):
    return