import enum


class Head:
    class MoveDirection(enum.IntEnum):
        left = -1
        stay = 0
        right = 1

    def __init__(self, position=0):
        self.initial_position = position
        self.__position = position

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        self.__position = value

    def move(self, step):
        self.position += step
