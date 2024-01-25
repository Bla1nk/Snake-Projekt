# snake/snake.py
from gameobject import GameObject
import json

class Snake(GameObject):
    def __init__(self):
        super().__init__(0, 0)  # Startposition
        self.length = 1
        self.body = [(self.x, self.y)]  # Startposition
        self.direction = "RIGHT"

    def move(self):
        head = self.body[0]
        if self.direction == "UP":
            new_head = (head[0], head[1] - 1)
        elif self.direction == "DOWN":
            new_head = (head[0], head[1] + 1)
        elif self.direction == "LEFT":
            new_head = (head[0] - 1, head[1])
        elif self.direction == "RIGHT":
            new_head = (head[0] + 1, head[1])

        if len(self.body) > self.length:
            self.body.pop()

        self.body.insert(0, new_head)

    def grow(self):
        self.length += 1

    def check_collision(self, screen_width, screen_height):
        head = self.body[0]

        # Überprüfe, ob die Schlange mit sich selbst kollidiert
        if head in self.body[1:]:
            return True

        # Überprüfe, ob die Schlange über den Rand hinausgeht
        if (
            head[0] < 0
            or head[0] >= screen_width // 20
            or head[1] < 0
            or head[1] >= screen_height // 20
        ):
            return True

        return False

    def change_direction(self, new_direction):
        if new_direction == "UP" and self.direction != "DOWN":
            self.direction = "UP"
        elif new_direction == "DOWN" and self.direction != "UP":
            self.direction = "DOWN"
        elif new_direction == "LEFT" and self.direction != "RIGHT":
            self.direction = "LEFT"
        elif new_direction == "RIGHT" and self.direction != "LEFT":
            self.direction = "RIGHT"

    def to_json(self):
        return json.dumps({"length": self.length, "body": self.body, "direction": self.direction})

    def from_json(self, data):
        snake_data = json.loads(data)
        self.length = snake_data["length"]
        self.body = snake_data["body"]
        self.direction = snake_data["direction"]
