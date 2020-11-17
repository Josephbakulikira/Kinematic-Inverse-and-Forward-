import pygame
from math import sin, cos, radians
class Vector2:
    def __init__(self, x=0, y=0):
        self.x = x;
        self.y = y;
    def ParsedTuple(self):
        return (int(self.x), int(self.y))

class Bone:
    def __init__(self, x, y, length, angle):
        self.origin = Vector2(x, y)
        self.end = Vector2()
        self.length = length
        self.angle = angle
        self.temp = self.angle
        self.parent = None
        self.updateEnd()

    def updateAngle(self, offset):

        self.temp = self.temp + offset

    def updateEnd(self):
        dx = self.length * cos(self.angle)
        dy = self.length * sin(self.angle)
        self.end = Vector2(self.origin.x + dx, self.origin.y + dy)

    def update(self):
        self.angle = self.temp
        if self.parent is not None:
            self.origin = Vector2(self.parent.GetEndX(), self.parent.GetEndY())
            self.angle += self.parent.angle
        self.updateEnd()

    def GetEndX(self):
        return self.end.x
    def GetEndY(self):
        return self.end.y

    def Draw(self, screen, color):
        pygame.draw.line(screen, color, self.origin.ParsedTuple(), self.end.ParsedTuple(), 10)
        pygame.draw.circle(screen, (225, 41, 22), self.origin.ParsedTuple(), 10)
