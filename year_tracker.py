from mastodon import Mastodon
import asyncio
import time
from dotenv import load_dotenv
import os

load_dotenv()

mastodon = Mastodon(
    client_id=os.getenv("CLIENT_ID"),
    client_secret=os.getenv("CLIENT_SECRET"),
    access_token=os.getenv("ACCESS_TOKEN"),
    api_base_url="https://mastodon.social"
)
lastYearProgress = 0
ProgressBar = ""
while True:
    date = time.strftime("%Y/%m/%d", time.localtime())
    day_month = time.strftime("%m/%d", time.localtime())
    yearProgress = time.strftime("%j", time.localtime())
    yearProgress = int(yearProgress) / 365 * 100
    yearProgress = int(yearProgress)
    if yearProgress != lastYearProgress:
        #mastodon.toot(date + " " + str(yearProgress) + "%")
        lastYearProgress = yearProgress
        ProgressBar = ""
        #ProgressBar = "▓" * int(yearProgress / 10)
        ProgressBar = "▓" * int(yearProgress / 5)
        ProgressBar = ProgressBar + "░" * (20 - len(ProgressBar))
        ProgressBar = "[" + ProgressBar + "]"
        ProgressBar = date + " " + ProgressBar + " " + str(yearProgress) + "%" + " "
        # if the day is christmas day then add a christmas tree any year
        if day_month == "12/25":
            ProgressBar = ProgressBar + "🎄"
        if yearProgress == 100:
            ProgressBar = ProgressBar + "🎉"
        if day_month == "01/01":
            ProgressBar = ProgressBar + "🎉 🍾 🎆"
        if day_month == "10/31":
            ProgressBar = ProgressBar + "🎃"
            
        print(ProgressBar)
        mastodon.toot(ProgressBar)
        
    time.sleep(86400)

