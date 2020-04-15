#!/usr/bin/env python3
import os
import pygame, sys
import datetime
import time
from pygame.locals import *
pygame.init()
pygame.display.set_caption('Pi-Odometer-Clock')
windowSurfaceObj = pygame.display.set_mode((442, 107), pygame.NOFRAME, 24)
digit1a = pygame.image.load('/home/pi/Documents/1a.png').convert()
digit2a = pygame.image.load('/home/pi/Documents/2a.png').convert()
digit3a = pygame.image.load('/home/pi/Documents/3a.png').convert()
digit4a = pygame.image.load('/home/pi/Documents/4a.png').convert()
digit5a = pygame.image.load('/home/pi/Documents/5a.png').convert()
digit6a = pygame.image.load('/home/pi/Documents/6a.png').convert()
digit7a = pygame.image.load('/home/pi/Documents/7a.png').convert()
digit8a = pygame.image.load('/home/pi/Documents/8a.png').convert()
digit9a = pygame.image.load('/home/pi/Documents/9a.png').convert()
digit0a = pygame.image.load('/home/pi/Documents/0a.png').convert()
digitbl = pygame.image.load('/home/pi/Documents/bl.png').convert()

data = [digit0a,digit1a,digit2a,digit3a,digit4a,digit5a,digit6a,digit7a,digit8a,digit9a]
now = datetime.datetime.now()
digit1 = data[int(str(now)[11:12])]
digit2 = data[int(str(now)[12:13])]
digit3 = data[int(str(now)[14:15])]
digit4 = data[int(str(now)[15:16])]
digit5 = data[int(str(now)[17:18])]
digit6 = data[int(str(now)[18:19])]
windowSurfaceObj.blit(digitbl,(0,0))
digit1.set_colorkey(0, pygame.RLEACCEL)
windowSurfaceObj.blit(digit1,(0, 0))
windowSurfaceObj.blit(digitbl,(72,0))
digit2.set_colorkey(0, pygame.RLEACCEL)
windowSurfaceObj.blit(digit2,(72, 0))
windowSurfaceObj.blit(digitbl,(150,0))
digit3.set_colorkey(0, pygame.RLEACCEL)
windowSurfaceObj.blit(digit3,(150, 0))
windowSurfaceObj.blit(digitbl,(222,0))
digit4.set_colorkey(0, pygame.RLEACCEL)
windowSurfaceObj.blit(digit4,(222, 0))
windowSurfaceObj.blit(digitbl,(300,0))
digit5.set_colorkey(0, pygame.RLEACCEL)
windowSurfaceObj.blit(digit5,(300, 0))
windowSurfaceObj.blit(digitbl,(372,0))
digit6.set_colorkey(0, pygame.RLEACCEL)
windowSurfaceObj.blit(digit6,(372,0))

while True:
    now = datetime.datetime.now()
    digit1 = data[int(str(now)[11:12])]
    digit1u = int(str(now)[11:12]) + 1
    if digit1u > 2:
        digit1u = 0
    digit1v = data[digit1u]
    digit2 = data[int(str(now)[12:13])]
    digit2u = int(str(now)[12:13]) + 1
    if (digit2u > 9 and digit1u == 2) or (digit2u > 3 and digit1u == 0):
        digit2u = 0
    digit2v = data[digit2u]
    digit3 = data[int(str(now)[14:15])]
    digit3u = int(str(now)[14:15]) + 1
    if digit3u > 5:
        digit3u = 0
    digit3v = data[digit3u]
    digit4 = data[int(str(now)[15:16])]
    digit4u = int(str(now)[15:16]) + 1
    if digit4u > 9:
        digit4u = 0
    digit4v = data[digit4u]
    digit5 = data[int(str(now)[17:18])]
    digit5u = int(str(now)[17:18]) + 1
    if digit5u > 5:
        digit5u = 0
    digit5v = data[digit5u]
    digit6 = data[int(str(now)[18:19])]
    digit6u = int(str(now)[18:19]) + 1
    if digit6u > 9:
        digit6u = 0
    digit6v = data[digit6u]
    digit7 = float(str(now)[18:21])
    h1 = 0
    h2 = 0
    m1 = 0
    m2 = 0
    s1 = 0
    if digit7 > 9.5:
        s1 += (float(str(now)[20:22])* 1.1)
        windowSurfaceObj.blit(digitbl,(300,0))
        digit5.set_colorkey(0, pygame.RLEACCEL)
        windowSurfaceObj.blit(digit5,(300, s1))
        digit5v.set_colorkey(0, pygame.RLEACCEL)
        windowSurfaceObj.blit(digit5v,(300, s1-107))
        if int(str(now)[17:18]) == 5:
            m2 += (float(str(now)[20:22]) * 1.1)
            windowSurfaceObj.blit(digitbl,(222,0))
            digit4.set_colorkey(0, pygame.RLEACCEL)
            windowSurfaceObj.blit(digit4,(222, m2))
            windowSurfaceObj.blit(digit4v,(222, m2-107))
            if int(str(now)[15:16]) == 9:
                m1 += (float(str(now)[20:22])* 1.1)
                windowSurfaceObj.blit(digitbl,(150,0))
                digit3.set_colorkey(0, pygame.RLEACCEL)
                windowSurfaceObj.blit(digit3,(150, m1))
                windowSurfaceObj.blit(digit3v,(150, m1-107))
                if int(str(now)[14:15]) == 5:
                    h2 += (float(str(now)[20:22])* 1.1)
                    windowSurfaceObj.blit(digitbl,(72,0))
                    digit2.set_colorkey(0, pygame.RLEACCEL)
                    windowSurfaceObj.blit(digit2,(72, h2))
                    windowSurfaceObj.blit(digit2v,(70, h2-107))
                    if int(str(now)[12:13]) == 9:
                        h1 += (float(str(now)[20:22])* 1.1)
                        windowSurfaceObj.blit(digitbl,(0,0))
                        digit1.set_colorkey(0, pygame.RLEACCEL)        
                        windowSurfaceObj.blit(digit1,(0, h1))
                        windowSurfaceObj.blit(digit1v,(0, h1-107))
    
    windowSurfaceObj.blit(digitbl,(372,0))
    digit6.set_colorkey(0, pygame.RLEACCEL)
    windowSurfaceObj.blit(digit6,(372,float(str(now)[20:22])))
    digit6v.set_colorkey(0, pygame.RLEACCEL)
    windowSurfaceObj.blit(digit6v,(372,float(str(now)[20:22])-107))
    
   
    pygame.display.update()
    time.sleep(0.1)
   
