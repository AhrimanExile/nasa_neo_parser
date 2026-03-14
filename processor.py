from statistics import mean

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
        return max(DataProcessor.get_asteroids(data), key=lambda x: float(x["close_approach_data"][0]["relative_velocity"]["kilometers_per_second"]))
    
    @staticmethod
    def get_largest(data):
        return max(DataProcessor.get_asteroids(data), key=lambda x: x["estimated_diameter"]["meters"]["estimated_diameter_max"])

    @staticmethod
    def get_closest(data):
        return min(DataProcessor.get_asteroids(data), key=lambda x: float(x["close_approach_data"][0]["miss_distance"]["astronomical"]))
    
    @staticmethod
    def get_asteroids(data):
        return [asteroid for value in data["near_earth_objects"].values() for asteroid in value]
    
    @staticmethod
    def get_statistics(data):
        number_asteroids = len(DataProcessor.get_asteroids(data))
        number_dangers = len(DataProcessor.get_dangerous(data))
        average_speed = mean(float(asteroid["close_approach_data"][0]["relative_velocity"]["kilometers_per_second"]) for asteroid in DataProcessor.get_asteroids(data))
        average_diameter = mean(asteroid["estimated_diameter"]["meters"]["estimated_diameter_max"] for asteroid in DataProcessor.get_asteroids(data))
        return {"number_of_asteroids": number_asteroids, 
                "number_of_dangers": number_dangers, 
                "average_speed": average_speed, 
                "average_diameter": average_diameter, 
                "closest_approach_astronomical": DataProcessor.get_closest(data)["close_approach_data"][0]["miss_distance"]["astronomical"]}