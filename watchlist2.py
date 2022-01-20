from operator import ge
import requests
import random
from bs4 import BeautifulSoup

x = 1
i = 1
movies = []
genres = ['action','adventure', 'animation', 'comedy', 'crime', 'documentary', 'drama', 'family',
'fantasy', 'history', 'horror', 'music', 'mystery', 'romance', 'science-fiction', 'thriller', 'tv-movie', 'war', 'western']

username = (input('Type your username: ')).lower()
inp = input('Choose genre or random: ')
if(inp == 'random'):
    inp = genres[random.randrange(19)]
genre = ('genre/' + inp).lower()

#while(i!=0):
i = 0
URL = "https://letterboxd.com/" + username + "/watchlist/" + genre + "/page/" + str(x)
page = requests.get(URL)

#for local html file
#URL = "D:\\Users\\Senpaiorigin\\Documents\\TaskSelector\\watchlist.html"
#page = open(URL,encoding='utf-8')
#page.read()

soup = BeautifulSoup(page.content,features="html.parser")

results = soup.find_all("img", {'class' : 'image'})

for movie in results:
    try:
        print(movie['alt'])
    except KeyError:
        pass
   # i=i+1


#for movie in results:
#    try:
#        #print(movie['data-film-name'])
#        movies.append(movie['data-film-name'])
#    except KeyError:
#        #print(movie['data-film-slug'])
#        movies.append(movie['data-film-slug'][6:][:-1].replace("-"," ").title())
#    i=i+1
#x += 1

#print(soup)
#print(i)
#print(len(movies))
#if(len(movies) != 0):
#    print(movies)
#else:
#    print("You have no " + inp.title() +  " movies in your watchlist.")
#print(soup)

