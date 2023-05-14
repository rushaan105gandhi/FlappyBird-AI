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

    def draw(self, win):
       
        self.img_count += 1

        # For animation of bird, loop through three images
        if self.img_count <= self.ANIMATION_TIME:
            self.img = self.IMGS[0]
        elif self.img_count <= self.ANIMATION_TIME*2:
            self.img = self.IMGS[1]
        elif self.img_count <= self.ANIMATION_TIME*3:
            self.img = self.IMGS[2]
        elif self.img_count <= self.ANIMATION_TIME*4:
            self.img = self.IMGS[1]
        elif self.img_count == self.ANIMATION_TIME*4 + 1:
            self.img = self.IMGS[0]
            self.img_count = 0

        #when bird is nose diving it isn't flapping
        if self.tilt <= -80:
            self.img = self.IMGS[1]
            self.img_count = self.ANIMATION_TIME*2
        
        # tilt the bird
        rotated_image = pygame.transform.rotate(self.img, self.tilt)
        new_rect = rotated_image.get_rect(center=self.img.get_react(topLeft = (self.x, self.y)).center)
        win.blit(rotated_image, new_rect.topleft)
    
    def get_mask(self):
        # """
        # gets the mask for the current image of the bird
        # :return: None
        # """
        return pygame.mask.from_surface(self.img)
    
class Pipe():
    #represents a pipe object
    GAP = 200
    VEL = 5

    def __init__(self, x):
        self.x = x
        self.height = 0
        self.gap = 100

        # where the top and bottom of the pipe is
        self.top = 0
        self.bottom = 0

        self.PIPE_TOP = pygame.transform.flip(PIPE_IMG, False, True)
        self.PIPE_BOTTOM = PIPE_IMG 

        self.passed = False

        self.set_height()
    
    def set_height(self):
        # set the height of the pipe, from the top of the screen
        # :return: None
        
        self.height = random.randrange(50, 450)
        self.top = self.height - self.PIPE_TOP.get_height()
        self.bottom = self.height + self.GAP

    def move(self):
        # """
        # move pipe based on vel
        # :return: None
        # """
        self.x -= self.VEL

    def draw(self, win):
        
        # draw both the top and bottom of the pipe
        # :param win: pygame window/surface
        # :return: None
        # draw top

        win.blit(self.PIPE_TOP, (self.x, self.top))

        # draw bottom
        win.blit(self.PIPE_BOTTOM, (self.x, self.bottom))

    def collide(self, bird, win):
        # """
        # returns if a point is colliding with the pipe
        # :param bird: Bird object
        # :return: Bool
        # """

        bird_mask = bird.get_mask()
        top_mask = pygame.mask.from_surface(self.PIPE_TOP)
        bottom_mask = pygame.mask.from_surface(self.PIPE_BOTTOM)
        top_offset = (self.x - bird.x, self.top - round(bird.y)) #how far the masks are from each other
        bottom_offset = (self.x - bird.x, self.bottom - round(bird.y))

        b_point = bird_mask.overlap(bottom_mask, bottom_offset) #find point of collision
        t_point = bird_mask.overlap(top_mask,top_offset)

        #check if the points exist or not
        if b_point or t_point:
            return True
        
        return False
    



    
    


