import requests
import json
from config import API_KEY, BASE_URL

class NASAParser:
    def __init__(self, api_key, base_url):
        self.api_key = api_key
        self.base_url = base_url
    
    def get_asteroids(self, start_date, end_date):
        url = f"{self.base_url}?start_date={start_date}&end_date={end_date}&api_key={self.api_key}"
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