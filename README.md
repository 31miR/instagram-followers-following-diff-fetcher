# IMPORTANT NOTICE
This software is provided "AS IS", without warranty of any kind, express or implied, including but not limited to the warranties of merchantability, fitness for a particular purpose and noninfringement. In no event shall the authors or copyright holders be liable for any claim, damages or other liability, whether in an action of contract, tort or otherwise, arising from, out of or in connection with the software or the use or other dealings in the software.

This code is provided for educational purposes only. Any usage of this code is the sole responsibility of the user.
Creator of this code provides no guarantees and does not take blame for any damages that are made.

# Instagram Friend Fetcher
Fetches followers / following data.

## Basic explanation of how this script works
This script sends get requests to instagram api in a way that frontend would send, in order to get the data about
profiles you follow / profiles that follow you back.

## How reliable is it?
Instagram API can change at any time and if that happens, this will probably not work.

Also, instagram API is private and as such, this code was more or less guesswork.

Furthermore, instagram API does not return all of the followers / following if you try to get the list of the profile that is
not your own.

Last but not least, most of the cookies/headers sent have been copied from the browser (with exception of the profile specific cookies) and there is no guarantee that they will be valid after some time.

## Is it safe?
Technically, no. You should not really use this script with your own profile as instagram does not condone the usage of API in this way.
If you do use this, there are almost no chances of anything bad happening, but this is **NOT A GUARANTEE**. You might get IP banned, profile locked or anything similar.

## How to use it?
You need to get your own csrftoken, sessionid and ds_user_id in order for this to work.

You can get all three of these values from the cookies:

```
inspect element on instagram page when logged in -> switch to Application -> cookies -> https://www.instagram.com
```

Create .env file at the root of this project and inside of it put those 3 cookies like this
```
csrftoken=
sessionid=
ds_user_id=
```
