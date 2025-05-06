# NO API KEY REQUIRED, thanks icanhazdadjoke :)
import requests
joke_data = requests.get('https://icanhazdadjoke.com/')
print(joke_data.status_code)
