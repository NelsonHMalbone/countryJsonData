import requests

# create a response
url = 'https://restcountries.com/v3.1/all'
response = requests.get(url) # shows a active 200 response
content = response.json() #structure list

# getting a input using a hard code word for now
# later will get user input
country = input("Enter a Country: ")

# acccss data
for c in content:
    country_name = c['name']['common']
    if country_name == country:
        capital = c['capital'][0]
        print(capital)

