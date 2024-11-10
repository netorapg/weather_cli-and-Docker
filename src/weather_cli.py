import requests
import os
import sys
from colorama import Fore, Style, init
from tabulate import tabulate

init(autoreset=True)

API_KEY = os.getenv('WEATHER_API_KEY')
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

def get_weather(city):
    params = {
        'q': city,
        'appid': API_KEY,
        'units': 'metric'
    }
    response = requests.get(BASE_URL, params=params)
    if response.status_code == 200:
        data = response.json()
        temp = data["main"]["temp"]
        feels_like = data["main"]["feels_like"]
        humidity = data["main"]["humidity"]
        description = data["weather"][0]["description"]

        table_data = [
            ["Temperature", f"{temp}°C"],
            ["Feels Like", f"{feels_like}°C"],
            ["Humidity", f"{humidity}%"],
            ["Description", description.capitalize()]
        ]
        
        print(Fore.CYAN + f"\nWeather in {city.capitalize()}:")
        print(tabulate(table_data, headers=[Fore.YELLOW + "Attribute", Fore.YELLOW + "Value"], tablefmt="grid"))
    else:
        print(Fore.RED + "City not found or API error.")

def main_menu():
    print(Fore.GREEN + Style.BRIGHT + "\nWeather CLI - Main Menu")
    print("1. Check Current Weather")
    print("2. Exit")

def main():
    if not API_KEY:
        print(Fore.RED + "Error: API key is not set.")
        sys.exit(1)

    while True:
        main_menu()
        choice = input(Fore.YELLOW + "\nChoose an option: ")

        if choice == '1':
            city = input(Fore.CYAN + "Enter city name: ")
            get_weather(city)
        elif choice == '2':
            print(Fore.MAGENTA + "Goodbye!")
            break
        else:
            print(Fore.RED + "Invalid option. Please try again.")

if __name__ == "__main__":
    main()
