import json


class JSONStorage:
    def __init__(self):
        self.name = "data.json"

    def save(self, data):
        with open("data.json", "w") as json_file:
            json.dump(data, json_file)
        json_file.close()

    def load(self):
        with open('data.json', "r") as json_file:
            data = json.load(json_file)
        return data
