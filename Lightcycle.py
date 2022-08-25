from turtle import back
import pygame
import enum

from Direction import *

class LightcycleStatus(Enum):
    OK = 1
    OUT_OF_BOUNDS = 2
    COLLISION = 3

class Lightcycle:
    SIZE = 10
    VELOCITY = 10

    def __init__(self, window, backgroundColor, color, x, y, direction, up_key, down_key, left_key, right_key) -> None:
        self.window = window
        self.window_width, self.window_height = 700, 700 # window.get_size()
        self.backgroundColor = backgroundColor
        self.color = color
        self.x = x
        self.y = y
        self.direction = direction
        self.up_key = up_key
        self.down_key = down_key
        self.left_key = left_key
        self.right_key = right_key
    
    def draw(self) -> LightcycleStatus:
        if self.direction == Direction.UP:
            self.y -= self.VELOCITY
        if self.direction == Direction.DOWN:
            self.y += self.VELOCITY
        if self.direction == Direction.LEFT:
            self.x -= self.VELOCITY
        if self.direction == Direction.RIGHT:
            self.x += self.VELOCITY

        status = LightcycleStatus.OK
        if self.x <= 0 or self.x >= self.window_width or self.y <= 0 or self.y >= self.window_height:
            status = LightcycleStatus.OUT_OF_BOUNDS
        elif self.window.get_at((self.x, self.y)) != self.backgroundColor:
            status = LightcycleStatus.COLLISION

        pygame.draw.rect(self.window, self.color, pygame.Rect(self.x, self.y, self.SIZE, self.SIZE))

        return status

    def handle_key_press(self, keys_pressed):
        if keys_pressed[self.up_key] and self.direction != Direction.DOWN:
            self.direction = Direction.UP
        if keys_pressed[self.down_key] and self.direction != Direction.UP:
            self.direction = Direction.DOWN
        if keys_pressed[self.left_key] and self.direction != Direction.RIGHT:
            self.direction = Direction.LEFT
        if keys_pressed[self.right_key] and self.direction != Direction.LEFT:
            self.direction = Direction.RIGHT
