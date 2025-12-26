import os
from dotenv import load_dotenv

load_dotenv()

headers = {"accept": "*/*",
    "accept-language": "en-US,en;q=0.9,bs;q=0.8,hr;q=0.7",
    "priority": "u=1, i",
    "sec-ch-prefers-color-scheme": "light",
    "sec-ch-ua": "\"Chromium\";v=\"142\", \"Google Chrome\";v=\"142\", \"Not_A Brand\";v=\"99\"",
    "sec-ch-ua-full-version-list": "\"Chromium\";v=\"142.0.7444.176\", \"Google Chrome\";v=\"142.0.7444.176\", \"Not_A Brand\";v=\"99.0.0.0\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-model": "\"\"",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-ch-ua-platform-version": "\"19.0.0\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "x-csrftoken": os.getenv("csrftoken"),
    "x-ig-app-id": "936619743392459",
    "x-requested-with": "XMLHttpRequest"
}
