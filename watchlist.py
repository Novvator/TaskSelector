from operator import ge
import requests
import random
from bs4 import BeautifulSoup

movieid = []


x = 1
i = 1
y=0
movies = []
genres = ['action','adventure', 'animation', 'comedy', 'crime', 'documentary', 'drama', 'family',
'fantasy', 'history', 'horror', 'music', 'mystery', 'romance', 'science-fiction', 'thriller', 'tv-movie', 'war', 'western']

username = (input('Type your username: ')).lower()
inp = input('Choose genre or random or all: ')
if(inp == 'random'):
    inp = genres[random.randrange(19)]
    print('Genre is: ' + inp)


genre = ('genre/' + inp + '/').replace(" ","-").lower()

if(inp == 'all'):
    genre = ''

while(i!=0):
    i = 0
    URL = "https://letterboxd.com/" + username + "/watchlist/" + genre + "page/" + str(x)
    page = requests.get(URL)

    #for local html file
    #URL = "D:\\Users\\Senpaiorigin\\Documents\\TaskSelector\\watchlist.html"
    #page = open(URL,encoding='utf-8')
    #page.read()

    soup = BeautifulSoup(page.content,features="html.parser")

    #results = soup.find("div", {"class":"film-poster"})
    results = soup.find_all("img", {"class" : "image"})
    results2 = soup.find_all("div", {"class" : "film-poster"})

    for movie in results:
        try:
            #print(movie['data-film-name'])
            movies.append(movie['alt'])
        except KeyError:
            #print(movie['data-film-slug'])
            #movies.append(movie['data-film-slug'][6:][:-1].replace("-"," ").title())
            pass
        i=i+1

    for movie in results2:
        movieid.append(movie['data-film-id'])
    x += 1

    

#print(i)
print(len(movies))
print(len(movieid))
if(len(movies) != 0):
    print(movies)
else:
    print("You have no " + inp.title() +  " movies in your watchlist.")

#movid = [int(x) for x in str(movieid[10])]
imagelinks = []
for mov in movieid:
    link = 'https://a.ltrbxd.com/resized/film-poster/'
    for number in mov:
        link += str(number) + '/'
    link += str(movieid[1])+'-'+movies[1].replace(" ","-").lower()+'-0-125-0-187-crop.jpg'
    imagelinks.append(link)

print(*imagelinks, sep = '\n')
