import instahttp.InstaHttp as instagram
import time

followers = instagram.fetch_all_followers()
follower_usernames = [follower["username"] for follower in followers]

time.sleep(0.5) #I'm scared of instagram api

followings = instagram.fetch_all_followings()
following_usernames = [following["username"] for following in followings]

followers_not_following = [follower for follower in follower_usernames if follower not in following_usernames]
followings_not_followers = [following for following in following_usernames if following not in follower_usernames]

def writeLine(file, text):
    file.write(text+"\n")

with open("result.txt", "w") as file:
    writeLine(file, "{")

    writeLine(file, "  \"follower_count\": " + str(len(followers)) + ",")
    writeLine(file, "  \"following_count\": " + str(len(followings)) + ",")
    writeLine(file, "  \"followers_not_following_count\": " + str(len(followers_not_following)) + ",")
    writeLine(file, "  \"followings_not_followers_count\": " + str(len(followings_not_followers)) + ",")
    

    writeLine(file, "  \"following:\"[")
    for following in following_usernames:
        writeLine(file, "    "+following+",")
    writeLine(file, "  ],")

    
    writeLine(file, "  \"followers:\"[")
    for follower in follower_usernames:
        writeLine(file, "    "+follower+",")
    writeLine(file, "  ],")

    writeLine(file, "  \"followers_not_following_count:\"[")
    for follower in followers_not_following:
        writeLine(file, "    "+follower+",")
    writeLine(file, "  ],")

    writeLine(file, "  \"followings_not_followers_count:\"[")
    for following in followings_not_followers:
        writeLine(file, "    "+following+",")
    writeLine(file, "  ],")
    
    writeLine(file, "}")