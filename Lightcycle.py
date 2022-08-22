import pygame

from Direction import *

class Lightcycle:
    SIZE = 10
    VELOCITY = 10

    def __init__(self, window, color, x, y, direction, up_key, down_key, left_key, right_key) -> None:
        self.window = window
        self.window_width, self.window_height = 700, 700 # window.get_size()
        self.color = color
        self.x = x
        self.y = y
        self.direction = direction
        self.up_key = up_key
        self.down_key = down_key
        self.left_key = left_key
        self.right_key = right_key
    
    def draw(self):
        pygame.draw.rect(self.window, self.color, pygame.Rect(self.x, self.y, self.SIZE, self.SIZE))
        if self.direction == Direction.UP and self.y - self.VELOCITY > 0:
            self.y -= self.VELOCITY
        if self.direction == Direction.DOWN and self.y + self.VELOCITY + self.SIZE < self.window_height:
            self.y += self.VELOCITY
        if self.direction == Direction.LEFT and self.x - self.VELOCITY > 0:
            self.x -= self.VELOCITY
        if self.direction == Direction.RIGHT and self.x + self.VELOCITY + self.SIZE < self.window_width:
            self.x += self.VELOCITY


    def handle_key_press(self, keys_pressed):
        if keys_pressed[self.up_key] and self.direction != Direction.DOWN:
            self.direction = Direction.UP
        if keys_pressed[self.down_key] and self.direction != Direction.UP:
            self.direction = Direction.DOWN
        if keys_pressed[self.left_key] and self.direction != Direction.RIGHT:
            self.direction = Direction.LEFT
        if keys_pressed[self.right_key] and self.direction != Direction.LEFT:
            self.direction = Direction.RIGHT
