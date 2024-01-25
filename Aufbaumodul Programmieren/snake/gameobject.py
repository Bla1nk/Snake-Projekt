# snake/gameobject.py
import json

class GameObject:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def to_json(self):
        return json.dumps({"x": self.x, "y": self.y})

    def from_json(self, data):
        obj_data = json.loads(data)
        self.x = obj_data["x"]
        self.y = obj_data["y"]
