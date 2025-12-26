import requests
import time
import random

from .cookiesConstant import cookies
from .headersConstant import headers

def fetch_follower_small_list(profile_id, max_id=None):
    request_link = "https://www.instagram.com/api/v1/friendships/" + str(profile_id) + "/followers/?count=12&search_surface=follow_list_page"
    if (max_id):
        request_link += "&max_id=" + max_id
    return requests.get(request_link, cookies=cookies, headers=headers).json()

def fetch_all_followers(profile_id=cookies["ds_user_id"]):
    """
    Fetches the list of all followers on the given profile id. If no profile_id is provided, it will attempt to find
    all of the followers for the profile whose ds_user_id is given in the .env file.
    
    Parameters:
    profile_id(string): user_id of the profile for which the followers are requested

    Returns:
    One big response from instagram hopefully
    """
    responses = []
    response = fetch_follower_small_list(profile_id)
    if (response):
        responses.append(response)
    while response["has_more"] == True:
        time.sleep(0.4 + random.random())
        response = fetch_follower_small_list(profile_id, response["next_max_id"])
        if (response):
            responses.append(response)
    users = []
    for response in responses:
        for user in response.users:
            users.append(user)
    return users