import requests
for a in range(97,97+26):
    #print(chr(a))
    f=requests.get(f"https://cdn.intra.42.fr/users/ali{chr(a)}.jpg")
    if(str(f)=="<Response [200]>"):
        print(f, chr(a))
    