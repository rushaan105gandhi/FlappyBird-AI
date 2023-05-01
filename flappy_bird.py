import pygame
import neat
import time
import os
import random

WIN_WIDTH=600
WIN_HEIGHT=800

BIRD_IMGS = [pygame.transform.scale2x(pygame.image.load(os.path.join("media", "bird1.png"))),pygame.transform.scale2x(pygame.image.load(os.path.join("media", "bird2.png"))),pygame.transform.scale2x(pygame.image.load(os.path.join("media", "bird3.png")))]
PIPE_IMG = pygame.transform.scale2x(pygame.image.load(os.path.join("media", "pipe.png")))
BASE_IMG = pygame.transform.scale2x(pygame.image.load(os.path.join("media", "base.png")))
BG_IMG = pygame.transform.scale2x(pygame.image.load(os.path.join("media", "bg.png")))

class Bird: 
    IMGS = BIRD_IMGS
    MAX_ROTATION = 25
    ROT_VEL = 20
    ANIMATION_TIME = 5

    def __init__(self, x, y):

        self.x = x
        self.y = y
        self.tilt = 0  # degrees to tilt
        self.tick_count = 0
        self.vel = 0
        self.height = self.y
        self.img_count = 0
        self.img = self.IMGS[0]

    def jump(self):
        
        self.vel = -10.5
        self.tick_count = 0
        self.height = self.y
    
    def move(self):

        self.tick_count += 1

        # for downward acceleration
        displacement = self.vel*(self.tick_count) + 0.5*(3)*(self.tick_count)**2  # calculate displacement

        # terminal velocity
        if displacement >= 16:
            displacement = 16

        if displacement < 0:
            displacement -= 2
        
        self.y = self.y + displacement

        if displacement < 0 or self.y < self.height + 50:  # tilt up
            if self.tilt < self.MAX_ROTATION:
                self.tilt = self.MAX_ROTATION
        else:  # tilt down
            if self.tilt > -90:
                self.tilt -= self.ROT_VEL