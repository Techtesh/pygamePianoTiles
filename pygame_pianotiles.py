# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 19:21:02 2020

@author: Hitesh
"""


import pygame,sys
from pygame.locals import *
import random,time
#pygame settings
pygame.init()
FPS=30
Framepersec=pygame.time.Clock()

#constants
BLUE=(0,0,255)
GREEN=(0,255,0)
RED=(255,0,0)
BLACK=(0,0,0)
WHITE=(255,255,255)

#more pygame settings
SCREEN_WIDTH=400
SCREEN_HEIGHT=400
SPEED=10
SCORE=5
font=pygame.font.SysFont("Verdana", 30)
font_small=pygame.font.SysFont("Verdana", 10)
game_over=font.render("GAME OVER",True,BLACK,None)
DISPLAYSURF=pygame.display.set_mode((SCREEN_HEIGHT,SCREEN_WIDTH))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("TILES")

class Background():
    def __init__(self):
        #setting background
        self.bgimage=python.image.load("C:\\Users\\Hitesh\\Desktop\\data\\project 12 pygame\\square_tile_pattern.jpg")
        self.rectBGimp=self.bgimage.get_rect()
        self.bgX1=0
        self.bgX2=0
        self.bgY1=0
        self.bgY2=self.rectBGimp.height
        self.updatespeed=5
    
    def update(self):
        self.bgY1=self.bgy1-self.updatespeed
        self.bgY2=self.bgy2-self.updatespeed
        if self.bgY1<= -self.rectBGimp.height:
            self.bgY1=self.rectBGimp.height
        if self.bgY2<= -self.rectBGimp.height:
            self.bgY2=self.rectBGimp.height    
        
    def render(self):
        DISPLAYSURF.blit(self.bgimage,(self.bgX1,self.bgY1))
        DISPLAYSURF.blit(self.bgimage,(self.bgX2,self.bgY2))
        
        
class Box():
    x=0
    y=-SCREEN_HEIGHT//5
    l=(SCREEN_WIDTH//4)-1
    h=SCREENHEIGHT//5
    enclick=True
    def pos(self,n):
        self.x=n*SCREEN_WIDTH//4
    def update(self,DISPLAYSURF):
        if seld.enclick:
            pygame.drawrect(DISPLAYSURF,BLACK,[self.x,self.y,self.h,self,y])
        
    
    
    pass
back_ground=Background()

INC_Speed=pygame.USEREVENT+1
pygame.time.set_timer(INC,Speed,1000)

while True:
    for event in pygame.event.get():
        if event.type == INC_Speed:
            SPEED+=1
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    Background.update()
    Background.render()
    
    scores=sont_small.render(str(SCORE),True,BLACk)
    DISPLAYSURF.blit(scores,(10,10))
    
    pygame.display.update()
    Framepersec.tick(FPS)