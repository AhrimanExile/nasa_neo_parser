import requests
import json

API_KEY = "QujXMHOAw9xfWcAS0EkCovysVE3AKsQkckF9n9Gm"

class NASAParser:
    def __init__(self, api_key):
        self.api_key = api_key
    
    def get_asteroids(self, start_date, end_date):
        url = f"https://api.nasa.gov/neo/rest/v1/feed?start_date={start_date}&end_date={end_date}&api_key={self.api_key}"
        response = requests.get(url)
        data = response.json()
        return data
    
    def print_asteroids(self, data):
        for day, value in data["near_earth_objects"].items():
            print(f"----------{day}----------")
            for asteroin in value:
                print(f"Name: {asteroin["name"]}")
                print(f"Danger level: { "not dangerous" if asteroin["is_potentially_hazardous_asteroid"] == False else "potentially dangerous"}")
                print(f"Speed: {asteroin["close_approach_data"][0]["relative_velocity"]["kilometers_per_hour"]} km/h")
                print("------------------------------")
            print()
    
    def save_to_json(self, data, filename):
        with open(filename, "w") as f:
            json.dump(data, f, indent=2)


asteroids = NASAParser(API_KEY)
data = asteroids.get_asteroids("2024-01-01", "2024-01-07")
asteroids.print_asteroids(data)
asteroids.save_to_json(data, "NEO_asteroids.json")