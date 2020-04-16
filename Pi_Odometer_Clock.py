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
hournow = str(now.hour).zfill(2)
minsnow = str(now.minute).zfill(2)
secsnow = str(now.second).zfill(2)
digit1 = data[int(str(hournow)[0:1])]
digit2 = data[int(str(hournow)[1:2])]
digit3 = data[int(str(minsnow)[0:1])]
digit4 = data[int(str(minsnow)[1:2])]
digit5 = data[int(str(secsnow)[0:1])]
digit6 = data[int(str(secsnow)[1:2])]

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
    hournow = str(now.hour).zfill(2)
    minsnow = str(now.minute).zfill(2)
    secsnow = str(now.second).zfill(2)
    digit1 = data[int(str(hournow)[0:1])]
    digit2 = data[int(str(hournow)[1:2])]
    digit3 = data[int(str(minsnow)[0:1])]
    digit4 = data[int(str(minsnow)[1:2])]
    digit5 = data[int(str(secsnow)[0:1])]
    digit6 = data[int(str(secsnow)[1:2])]
    digit1u = int(str(hournow)[0:1]) + 1
    digit2u = int(str(hournow)[1:2]) + 1
    digit3u = int(str(minsnow)[0:1]) + 1
    digit4u = int(str(minsnow)[1:2]) + 1
    digit5u = int(str(secsnow)[0:1]) + 1
    digit6u = int(str(secsnow)[1:2]) + 1
    if digit1u > 2:
        digit1u = 0
    digit1v = data[digit1u]
    if (digit2u > 9 and digit1u == 2) or (digit2u > 3 and digit1u == 0):
        digit2u = 0
    digit2v = data[digit2u]
    if digit3u > 5:
        digit3u = 0
    digit3v = data[digit3u]
    if digit4u > 9:
        digit4u = 0
    digit4v = data[digit4u]
    if digit5u > 5:
        digit5u = 0
    digit5v = data[digit5u]
    if digit6u > 9:
        digit6u = 0
    digit6v = data[digit6u]
    seconds = float(now.strftime('%S.%f'))
    digit7 = (seconds) - int(seconds)
    h1 = 0
    h2 = 0
    m1 = 0
    m2 = 0
    s1 = 0
    if seconds > 10:
        seconds -= int(seconds/10) * 10
    if  seconds> 9.5:
        s1 += digit7 * 107
        windowSurfaceObj.blit(digitbl,(300,0))
        digit5.set_colorkey(0, pygame.RLEACCEL)
        windowSurfaceObj.blit(digit5,(300, s1))
        digit5v.set_colorkey(0, pygame.RLEACCEL)
        windowSurfaceObj.blit(digit5v,(300, s1-107))
        if digit5u == 0:
            m2 += digit7 * 107
            windowSurfaceObj.blit(digitbl,(222,0))
            digit4.set_colorkey(0, pygame.RLEACCEL)
            windowSurfaceObj.blit(digit4,(222, m2))
            windowSurfaceObj.blit(digit4v,(222, m2-107))
            if digit4u == 0:
                m1 +=  digit7 * 107
                windowSurfaceObj.blit(digitbl,(150,0))
                digit3.set_colorkey(0, pygame.RLEACCEL)
                windowSurfaceObj.blit(digit3,(150, m1))
                windowSurfaceObj.blit(digit3v,(150, m1-107))
                if digit3u == 0:
                    h2 +=  digit7 * 107
                    windowSurfaceObj.blit(digitbl,(72,0))
                    digit2.set_colorkey(0, pygame.RLEACCEL)
                    windowSurfaceObj.blit(digit2,(72, h2))
                    windowSurfaceObj.blit(digit2v,(70, h2-107))
                    if digit2u == 0:
                        h1 +=  digit7 * 107
                        windowSurfaceObj.blit(digitbl,(0,0))
                        digit1.set_colorkey(0, pygame.RLEACCEL)        
                        windowSurfaceObj.blit(digit1,(0, h1))
                        windowSurfaceObj.blit(digit1v,(0, h1-107))
    
    windowSurfaceObj.blit(digitbl,(372,0))
    digit6.set_colorkey(0, pygame.RLEACCEL)
    windowSurfaceObj.blit(digit6,(372,digit7 * 107))
    digit6v.set_colorkey(0, pygame.RLEACCEL)
    windowSurfaceObj.blit(digit6v,(372,(digit7 * 107)-107))
    pygame.display.update()
    time.sleep(0.025)
   
