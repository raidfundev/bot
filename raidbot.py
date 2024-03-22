import telepot
from pprint import pprint
import time
from telepot.loop import MessageLoop
from urllib.parse import urlparse
import requests
from bs4 import BeautifulSoup

key = "7101011836:AAGz3j2moDqsuqkWk0uvn91k9T229ndsSqw"

bot = telepot.Bot(key)

blimp = -1001136714808
test = -4169947111

def handle(msg):
    # change test to blimp to make it work on the blimp channel
    if msg['chat']['id'] == test:
        print(msg['text'])
        url = urlparse(msg['text'])
        if url.netloc == 'x.com' or url.netloc == 'twitter.com':
            if 'status' in url.path:
                tweet_id = url.path.split('/')[-1]
                if tweet_id.isdigit():
                    # Get metadata from URL
                    response_url = 'https://eoj06hx7rfcysvo.m.pipedream.net?id=' + tweet_id
                    response = requests.get(response_url)
                    if response.status_code == 200:
                        print(f'Response from {response_url}: {response.text}')
                    else:
                        print(f'Failed to get response from {response_url}. Status code: {response.status_code}')

                else:
                    print(f"I don't know how to read that tweet {url.path}")

bot.message_loop(handle)

while 1:
    time.sleep(10)

