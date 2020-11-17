import pygame
import math
import sys
from Segment import Vector2, Bone
import random

width, height = 1920, 1080
black, white = (0, 0, 0), (255, 255,255)
fps = 60
screen = pygame.display.set_mode((width, height), pygame.FULLSCREEN);
clock = pygame.time.Clock()

Arm = Bone(width/2, height/2, 200, math.radians(-45))
Arm2 = Bone(Arm.GetEndX(), Arm.GetEndY(), 200, math.radians(-45))
Arm2.parent = Arm;
run = True
while run:
    clock.tick(fps)
    screen.fill(black)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    Arm.updateAngle(0.01)
    Arm.update()
    Arm2.update()
    Arm.Draw(screen, white)
    Arm2.Draw(screen, white)
    pygame.display.update()

pygame.quit()
