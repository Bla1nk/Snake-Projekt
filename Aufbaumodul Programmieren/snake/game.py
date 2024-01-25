# snake/game.py
import pygame
import sys
import random
from snake import Snake

class Game:
    def __init__(self, width=800, height=600):
        pygame.init()
        self.width = width
        self.height = height
        self.snake = Snake()
        self.food = self.generate_food()
        # Initialisiere Pygame-Fenster
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Snake Game")

    def generate_food(self):
        # Generiere zufällige Position für die Nahrung
        return (random.randint(0, self.width // 20 - 1), random.randint(0, self.height // 20 - 1))

    def start(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    self.handle_input(event.key)

            self.update()
            self.render()
            pygame.display.flip()
            pygame.time.delay(100)  # Füge eine kleine Verzögerung hinzu, um die Bewegung sichtbar zu machen

    def handle_input(self, key):
        if key == pygame.K_UP and self.snake.direction != "DOWN":
            self.snake.change_direction("UP")
        elif key == pygame.K_DOWN and self.snake.direction != "UP":
            self.snake.change_direction("DOWN")
        elif key == pygame.K_LEFT and self.snake.direction != "RIGHT":
            self.snake.change_direction("LEFT")
        elif key == pygame.K_RIGHT and self.snake.direction != "LEFT":
            self.snake.change_direction("RIGHT")

    def update(self):
        self.snake.move()

        # Überprüfe, ob die Schlange die Nahrung erreicht hat
        if self.snake.body[0] == self.food:
            self.snake.grow()
            self.food = self.generate_food()

        # Überprüfe, ob die Schlange die Wand berührt hat
        head = self.snake.body[0]
        if (
            head[0] < 0
            or head[0] >= self.width // 20
            or head[1] < 0
            or head[1] >= self.height // 20
        ):
            # Ändere die Richtung der Schlange, um auf der anderen Seite des Spielfelds zu erscheinen
            if head[0] < 0:
                self.snake.body[0] = (self.width // 20 - 1, head[1])
            elif head[0] >= self.width // 20:
                self.snake.body[0] = (0, head[1])
            elif head[1] < 0:
                self.snake.body[0] = (head[0], self.height // 20 - 1)
            elif head[1] >= self.height // 20:
                self.snake.body[0] = (head[0], 0)

        # Überprüfe, ob die Schlange mit sich selbst kollidiert
        if self.snake.check_collision(self.width, self.height):
            pygame.quit()
            sys.exit()

        # Überprüfe, ob die Schlange die Nahrung erreicht hat
        if self.snake.body[0] == self.food:
            self.snake.grow()
            self.food = self.generate_food()

    def render(self):
        self.screen.fill((0, 0, 0))  # Hintergrundfarbe

        # Zeichne die Schlange
        for segment in self.snake.body:
            pygame.draw.rect(self.screen, (255, 255, 255), pygame.Rect(segment[0] * 20, segment[1] * 20, 20, 20))

        # Zeichne die Nahrung
        pygame.draw.rect(self.screen, (255, 0, 0), pygame.Rect(self.food[0] * 20, self.food[1] * 20, 20, 20))

def main():
    game = Game()
    game.start()

if __name__ == "__main__":
    main()
