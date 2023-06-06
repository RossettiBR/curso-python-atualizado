import requests

url = 'https://www.youtube.com/watch?v=Qd8JT0bnJGs'
request = requests.get(url)
print(request)