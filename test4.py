'''Exercise 4: Scraping Test'''
import requests
from bs4 import BeautifulSoup

def get_twitter_followers(url):
    page= requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    abonnes = list(soup.find(class_="ProfileNav-item ProfileNav-item--followers").children)[1]
    detail=list(abonnes.children)[5]
    return(detail['data-count'])

print(get_twitter_followers('https://twitter.com/zidaneofficial_?lang=fr'))
