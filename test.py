import requests

url = 'https://127.0.0.1:8000'
myjson = {'somekey': 'somevalue'}

x = requests.get(url, json = myjson)

#print the response text (the content of the requested file):

print(x.text)