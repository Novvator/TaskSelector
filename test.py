import requests

try:
    response = requests.get("https://a.ltrbxd.com/resized/film-poster/5/1/3/6/0/51360-platoon-0-125-0-187-crop.jpg")
    print("URL is valid and exists on the internet")
except requests.ConnectionError as exception:
    print("URL does not exist on Internet")