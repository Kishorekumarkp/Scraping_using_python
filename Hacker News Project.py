import requests
from bs4 import BeautifulSoup
import pprint

res = requests.get('https://news.ycombinator.com/news')
soup = BeautifulSoup(res.text, "html.parser")
#print(soup.select('.score'))   #grabs all the span having a class=score (if a = b. then, select(.b))
links = soup.select('.storylink') #grabs all the storylink class
subtext = soup.select('.subtext')#grabs all the score

def sort_by_votes(hnlist):
    return sorted(hnlist, key= lambda k: k["votes"])

def create_custom_hn(links , subtext):
    hn = []
    for idx,item in enumerate(links):
        title =  item.getText()
        href = item.get("href" , None)
        vote = subtext[idx].select('.score')
        if len(vote): # means when voten != 0
            point = int(vote[0].getText().replace('points' , ''))
            if point>99:
                hn.append({'title' : title , 'link' : href, 'votes' : point})
    return sort_by_votes(hn)

pprint.pprint(create_custom_hn(links, subtext))