import requests
from bs4 import BeautifulSoup
import pprint

# Be ethical - check the /robots.txt from the website before use the data

res = requests.get('https://news.ycombinator.com/news')
res2 = requests.get('https://news.ycombinator.com/news?p=2')
soup = BeautifulSoup(res.text, 'html.parser')
soup2 = BeautifulSoup(res2.text, 'html.parser')
links = soup.select('.storylink')
links2 = soup2.select('.storylink')
subtext = soup.select('.subtext')
subtext2 = soup2.select('.subtext')

all_links = links + links2
all_subtexts = subtext + subtext2


def sort_news_by_votes(hn_list):
    #sorting dictionaries using lambda
    return sorted(hn_list, key= lambda k: k['votes'], reverse=True)


def create_custom_news(links, subtext):
    hn = []
    for index, item in enumerate(links):
        title = item.getText()
        href = item.get('href', None)
        vote = subtext[index].select('.score')
        if len(vote):
            points = int(vote[0].getText().replace(' points', ''))
            if points > 99:
                hn.append({'title': title, 'link': href, 'votes': points})
    return sort_news_by_votes(hn)

pprint.pprint(create_custom_news(all_links, all_subtexts))