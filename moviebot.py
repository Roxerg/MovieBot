from bs4 import BeautifulSoup
from urllib.parse import urlparse

import praw
import time
import re
import requests
import bs4
import os

path = os.path.dirname(os.path.realpath(__file__))

print (path)


firstline = ("The movie %s (%s) is rated:" %(title, date))

def auth():

    print("Authenticating...\n")
    reddit = praw.Reddit("moviebot", user_agent = "web:movie-bot:v0.1 (by /u/Roxerg)")
    print("Authenticated as {}\n".format(reddit.user.me()))

    return reddit

def fetchdata(title):

    title =  re.sub(r'[^a-zA-Z0-9\s]+', '', title)
    tomatourl = "https://www.rottentomatoes.com/m/" + title.replace(" ", "_")
    metacriticurl = "http://www.metacritic.com/movie/" + title.replace(" ", "-")

    r = requests.get(tomatourl)
    soup = BeautifulSoup(r.content, 'html.parser')

    tag = soup.find(class = "meter-value")
    audience = soup.tag.get_text()

    tag = soup.find(class = "critic-score meter")
    critic = soup.tag.get_text()

def moviebot(reddit):

    for comment in reddit.subreddit('test').comments(limit = 1000000):
        request = re.findall("[a-z]*[A-Z]*[0-9]*moviebot", comment.body)
        if request:
            print('request found in comment with comment ID: ' + comment.id)
            movie = match[0]
            print('Movie: ' + movie)

            # try reading movie titles separated by ; maybe?




            #<div class="meter-value">
            #                <span class="superPageFontColor" style="vertical-align:top">82%</span>
            #            </div>

            #<div class="critic-score meter">
            #            <a href="#contentReviews" class="unstyled articleLink" id="tomato_meter_link">
            #            <span class="meter-tomato icon big medium-xs certified_fresh pull-left"></span>
            #                <span class="meter-value superPageFontColor"><span>92</span>%</span>
            #            </a>
            #            </div>

def main():
    reddit = authenticate()
    while True:
        run_explainbot(reddit)


if __name__ == '__main__':
    main()