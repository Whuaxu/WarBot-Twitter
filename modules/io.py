import json

def readJson(filepath):
    with open(filepath, "r", encoding="utf-8") as file:
        return json.load(file)

# Function to write a JSON file
def writeJson(filepath, data):
    with open(filepath, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)