# test_snake.py
import unittest
from snake.snake import Snake

class TestSnake(unittest.TestCase):
    def test_initialization(self):
        snake = Snake()
        self.assertEqual(snake.length, 1)
        self.assertEqual(snake.body, [(0, 0)])
        self.assertEqual(snake.direction, "RIGHT")

    def test_move(self):
        snake = Snake()
        snake.move()
        self.assertEqual(snake.body, [(1, 0)])

    def test_grow(self):
        snake = Snake()
        snake.grow()
        self.assertEqual(snake.length, 2)

    def test_check_collision(self):
        snake = Snake()
        self.assertFalse(snake.check_collision(10, 10))
        snake.body = [(0, 0), (0, 1), (1, 1), (1, 0)]
        self.assertTrue(snake.check_collision(10, 10))

    def test_change_direction(self):
        snake = Snake()
        snake.change_direction("UP")
        self.assertEqual(snake.direction, "UP")

if __name__ == "__main__":
    unittest.main()
