from re import X
import sys, pygame
import math
import random

from tkinter import *
from tkinter import messagebox
pygame.init()


black = 0, 0, 0
white = 255, 255, 255
yellow = 255,255,204
clock = pygame.time.Clock()
vez = random.randint(1, 2)
size = width, height = 192, 192
screen = pygame.display.set_mode(size)
data = [0,0,0,0,0,0,0,0,0]
pygame.display.set_caption('Primeiro jogo')
screen.fill(white)
font = pygame.font.Font('freesansbold.ttf', 32)
xImage = pygame.image.load("x.png")


def verVitoria():
    for y in range(3):
        if(data[(y*3)] == data[1+(y*3)] and data[1+(y*3)]==data[2+(y*3)]):
            if(data[(y*3)] != 0):
                if(data[(y*3)] == 1):
                    Tk().wm_withdraw() #to hide the main window
                    messagebox.showinfo('Resultado','Bola venceu!')
                    pygame.quit()
                else:
                    Tk().wm_withdraw() #to hide the main window
                    messagebox.showinfo('X venceu','X venceu!')
                    pygame.quit()
                #Verificação de vitoria horizontal
    for y in range(3):
        if(data[y] == data[3+y] and data[3+y]==data[6+y]):
            if(data[y] != 0):
                if(data[0] == 1):
                    Tk().wm_withdraw() #to hide the main window
                    messagebox.showinfo('Resultado','Bola venceu!')
                    pygame.quit()
                else:
                    Tk().wm_withdraw() #to hide the main window
                    messagebox.showinfo('X venceu','X venceu!')
                    pygame.quit()

    if(data[0] == data[4] and data[4] == data[8]):
        if(data[0] != 0):
            if(data[0] == 1):
                Tk().wm_withdraw() #to hide the main window
                messagebox.showinfo('Resultado','Bola venceu!')
                pygame.quit()
            else:
                Tk().wm_withdraw() #to hide the main window
                messagebox.showinfo('X venceu','X venceu!')
                pygame.quit()
    if(data[2] == data[4] and data[4] == data[6]):
        if(data[2] != 0):
            if(data[2] == 1):
                Tk().wm_withdraw() #to hide the main window
                messagebox.showinfo('Resultado','Bola venceu!')
                pygame.quit()
            else:
                Tk().wm_withdraw() #to hide the main window
                messagebox.showinfo('X venceu','X venceu!')
                pygame.quit()

while True:
    (mouseX,mouseY) = pygame.mouse.get_pos()
    screen.fill(white)
    cordX = math.floor(mouseX/64)*64
    cordY = math.floor(mouseY/64)*64
    xID = int(cordX/64)+1
    yID = int(cordY/64)+1
    #print(f"Cord X: {xID}  Cord Y: {yID}")
    pygame.draw.line(screen,black,[0,64],[width,64])
    pygame.draw.line(screen,black,[0,128],[width,128])
    pygame.draw.line(screen,black,[64,0],[64,height])
    pygame.draw.line(screen,black,[128,0],[128,height])
    pygame.draw.rect(screen,yellow,[cordX,cordY,64,64])
    for i in range(3):
        for y in range(3):
            if(data[i+(y*3)] == 1):
                pygame.draw.circle(screen,black,[32+(64*i),32+(64*y)],16,3)
            if(data[i+(y*3)] == 2):
                screen.blit(xImage,[16+(64*i),16+(64*y)])
    pygame.display.update()
    verVitoria()
    clock.tick(60)
    #print(clock.get_fps())
    for event in pygame.event.get():

        if event.type == pygame.QUIT: sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            for i in range(3):
                for y in range(3):
                    if(xID == i+1 and yID == y+1):
                        print(f"Mouse sobre: {i+1} {y}")
                        if(data[i+(y*3)] == 0):
                            print("Vazio")
                            if(vez == 1):
                                data[i+(y*3)] = 1
                                vez = 2
                            else:
                                data[i+(y*3)] = 2
                                vez = 1
                        else:
                            print("Possui valor")
                print(data)
         
    
                    
        
        
   
