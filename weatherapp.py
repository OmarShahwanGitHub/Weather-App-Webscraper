import requests #allows for simulating the website and retreiving contents from its json file

#Ensure the API key is correctly loaded from the file
try:
    with open('api_key.txt', 'r') as file: #check for errors when reading the api_key file
        api_key = file.read().strip()
except FileNotFoundError:
    print("Error: 'api_key.txt' file not found.")
    exit()
except Exception as e:
    print(f"Error: {e}")
    exit()

location = input("Enter city: ")

#searches for location using api key and the units of the temperatures are set to metric
result = requests.get(f'http://api.openweathermap.org/data/2.5/weather?q={location}&units=metric&appid={api_key}') 
response_json = result.json() #json method to retreive data instead of response message (i.e. 200 or 404)

if result.status_code == 401:  #status code 401 means the API key is invalid, be sure to change it in the text file
    print("Error: Invalid API key. Please check your API key in the text file and try again.")
    exit()

if result.status_code != 200: #response 200 means there are no errors
    print(f"Error: {response_json.get('message', 'Unknown error')}")
    exit()

if 'weather' not in response_json: #error message if the data retreiving process is unable to find "weather" and its attributes
    print("Error: 'weather' key not found in the response")
    print("Response:", response_json)

#filters exact data points to store from the json file
description = response_json['weather'][0]['description']
temperature = round(response_json['main']['temp'])
feels_like = round(response_json['main']['feels_like'])
high = round(response_json['main']['temp_max'])
low = round(response_json['main']['temp_min'])

#Unicode for the degree symbol
degree_symbol = '\u00B0'

print(f"The weather in {location[0].upper()}{location[1:]} is {temperature}{degree_symbol}C with {description}.")
print(f"It feels like {feels_like}{degree_symbol}C.")
print(f"Today's high is {high}{degree_symbol}C and today's low is {low}{degree_symbol}C.")