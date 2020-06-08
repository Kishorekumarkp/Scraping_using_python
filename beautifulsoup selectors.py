import requests
from bs4 import BeautifulSoup

res = requests.get('https://news.ycombinator.com/news')
soup = BeautifulSoup(res.text, "html.parser")
#print(soup.select('.score'))   #grabs all the span having a class=score (if a = b. then, select(.b))
links = soup.select('.storylink') #grabs all the storylink class
votes = soup.select('.score')#grabs all the score
print(votes[0].get('id')) #gives the id present in the first item of the votes

