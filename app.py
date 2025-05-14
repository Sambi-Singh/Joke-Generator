# NO API KEY REQUIRED, thanks icanhazdadjoke :)
import requests
Headers = {'Accept': 'application/json'}
#print(joke_data.status_code)
#joke = joke_data.json()['joke']
#print(joke)
getNumJokes = int(input("How many jokes do you want to laugh at?: "))
for joke in range(getNumJokes):
    joke_data = requests.get('https://icanhazdadjoke.com/', headers=Headers) #Remeber to pass in header to specify right format
    joke = joke_data.json()['joke']
    print(f"{joke}\n")


