import os
from dotenv import load_dotenv

load_dotenv()

cookies = {
  "csrftoken": os.getenv("csrftoken"),
  "sessionid": os.getenv("sessionid"),
  "ds_user_id": os.getenv("ds_user_id"),
  "wd": "720x695",
  "dpr": "1.25",
  "ps_l": "1",
  "ps_n": "1"
}