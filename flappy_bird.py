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