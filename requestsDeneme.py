import requests
r = requests.get('https://api.github.com/events', stream=True)
r.raw
r.raw.read(10)

with open('ResultHeaders.txt', 'rb') as fd:
        fd.write(r)