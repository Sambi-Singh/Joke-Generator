# NO API KEY REQUIRED, thanks icanhazdadjoke :)
import requests
Headers = {'Accept': 'application/json'}
joke_data = requests.get('https://icanhazdadjoke.com/', headers=Headers) #Remeber to pass in header to specify right format
#print(joke_data.status_code)
joke = joke_data.json()['joke']
print(joke)