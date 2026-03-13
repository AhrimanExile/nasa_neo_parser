import parser
import processor
from config import API_KEY, BASE_URL

neo = parser.NASAParser(API_KEY, BASE_URL)
data = neo.get_asteroids("2026-03-06", "2026-03-13")
neo.save_to_json(data, "NEO_asteroids.json")
print(processor.DataProcessor.get_fastest(data))