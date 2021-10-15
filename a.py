import requests
#"https://cdn.intra.42.fr/users/mhussein.jpg"
str="https://cdn.intra.42.fr/users/"
test = "almarzouqi"
end = ".jpg"

for a in range(97,123):
    link = str + chr(a) + test + end
    #print(link)
    request_output = requests.get(link)
    if request_output.status_code == 200:
        print(link)
