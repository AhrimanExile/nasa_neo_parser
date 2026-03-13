class DataProcessor:
    @staticmethod
    def get_dangerous(data):
        dangerous_asteroid = []
        for value in data["near_earth_objects"].values():
            for asteroid in value:
               if asteroid["is_potentially_hazardous_asteroid"]:
                   dangerous_asteroid.append(asteroid)
        return dangerous_asteroid
    
    @staticmethod
    def get_fastest(data):
        asteroids = [asteroid for value in data["near_earth_objects"].values() for asteroid in value]
        return max(asteroids, key=lambda x: float(x["close_approach_data"][0]["relative_velocity"]["kilometers_per_second"]))