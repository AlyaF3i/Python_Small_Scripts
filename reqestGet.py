import requests
test = str(requests.get('https://cdn.intra.42.fr/users/0010.jpg'))
for a in range(10000):
    link=f"https://cdn.intra.42.fr/users/{str(a).zfill(4)}.jpg"
    response =requests.get(link)
    if str(response) != test:
        print(link)
