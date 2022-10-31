from re import X
import sys, pygame
import math
import random

from tkinter import *
from tkinter import messagebox
pygame.init()


black = 0, 0, 0 #DEFINIÇÃO DA COR PRETA (RGB)
white = 255, 255, 255 #DEFINIÇÃO DA COR BRANCA (RGB)
yellow = 255,255,204 #DEFINIÇÃO DA COR AMARELA (RGB)
clock = pygame.time.Clock()
vez = random.randint(1, 2) #DEFINDO QUEM VAI JOGAR PRIMEIRO COM UM VALOR RANDOMICO ENTRE 1 E 2
size = width, height = 192, 192 #DEFININDO TAMANHO DA TELA
screen = pygame.display.set_mode(size) #COLOCANDO A TELA DO JOGO EM UMA VARIAVEL
data = [0,0,0,0,0,0,0,0,0] #ARRAY LISTA PARA SALVAR OS DADOS DE CADA BLOCO DO JOGO, 0 = NADA, 1 = BOLA, 2 = X
pygame.display.set_caption('TIC TAC TOE') #TITULO DO JOGO 
screen.fill(white) #COR DO BACKGROUND
xImage = pygame.image.load("x.png") #PEGANDO UMA IMAGEM DO DIRETORIO E A COLOCANDO EM UMA VARIAVEL

def desenharJogo(): #METODO PARA DESENHAR AS LINHAS DO JOGO DA VELHA
    pygame.draw.line(screen,black,[0,64],[width,64])
    pygame.draw.line(screen,black,[0,128],[width,128])
    pygame.draw.line(screen,black,[64,0],[64,height])
    pygame.draw.line(screen,black,[128,0],[128,height])
    pygame.draw.rect(screen,yellow,[cordX,cordY,64,64])
def verVitoria(): #METODO PARA VERIFICAR SE ALGUEM GANHOU
    for y in range(3):
        if(data[(y*3)] == data[1+(y*3)] and data[1+(y*3)]==data[2+(y*3)]):
            if(data[(y*3)] != 0):
                if(data[(y*3)] == 1):
                    Tk().wm_withdraw() 
                    messagebox.showinfo('Resultado','Bola venceu!')
                    pygame.quit()
                else:
                    Tk().wm_withdraw() 
                    messagebox.showinfo('X venceu','X venceu!')
                    pygame.quit()
                #Verificação de vitoria horizontal
    for y in range(3):
        if(data[y] == data[3+y] and data[3+y]==data[6+y]):
            if(data[y] != 0):
                if(data[0] == 1):
                    Tk().wm_withdraw() 
                    messagebox.showinfo('Resultado','Bola venceu!')
                    pygame.quit()
                else:
                    Tk().wm_withdraw() 
                    messagebox.showinfo('X venceu','X venceu!')
                    pygame.quit()

    if(data[0] == data[4] and data[4] == data[8]):
        if(data[0] != 0):
            if(data[0] == 1):
                Tk().wm_withdraw() 
                messagebox.showinfo('Resultado','Bola venceu!')
                pygame.quit()
            else:
                Tk().wm_withdraw() 
                messagebox.showinfo('X venceu','X venceu!')
                pygame.quit()
    if(data[2] == data[4] and data[4] == data[6]):
        if(data[2] != 0):
            if(data[2] == 1):
                Tk().wm_withdraw() 
                messagebox.showinfo('Resultado','Bola venceu!')
                pygame.quit()
            else:
                Tk().wm_withdraw() 
                messagebox.showinfo('X venceu','X venceu!')
                pygame.quit()
def desenharNoBloco(): #METODO PARA DESENHAR A BOLINHA OU O X CONFORME O VALOR PRESENTE NA ARRAY
    for i in range(3):
        for y in range(3):
            if(data[i+(y*3)] == 1):
                pygame.draw.circle(screen,black,[32+(64*i),32+(64*y)],16,3)
            if(data[i+(y*3)] == 2):
                screen.blit(xImage,[16+(64*i),16+(64*y)])
while True:
    (mouseX,mouseY) = pygame.mouse.get_pos() #COLOCANDO A CORDENADA X E Y DO MOUSE NA TELA DENTRO DE UMA VARIAVEL RESPECTIVAMENTE
    screen.fill(white) #COR DO BACKGROUND
    cordX = math.floor(mouseX/64)*64 #DEFININDO UMA MOVIMENTAÇÃO EM GRID 64X64 PARA O MOUSE NO EIXO X
    cordY = math.floor(mouseY/64)*64    #DEFININDO UMA MOVIMENTAÇÃO EM GRID 64X64 PARA O MOUSE NO EIXO Y
    xID = int(cordX/64)+1 #SIMPLIFICANDO AS CORDENADAS POR UM ID 
    yID = int(cordY/64)+1   #SIMPLIFICANDO AS CORDENADAS POR UM ID 
    #print(f"Cord X: {xID}  Cord Y: {yID}")
    desenharJogo()
    desenharNoBloco()
    pygame.display.update() #ATUALIZAR AS INFORMAÇÕES DE TELA A CADA FRAME
    verVitoria()
    clock.tick(60) #QUANTAS VEZES ESSE CODIGO VAI SE REPETIR POR SEGUNDO
    #print(clock.get_fps())
    for event in pygame.event.get():

        if event.type == pygame.QUIT: sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN: #SE O USUARIO CLICAR COM O MOUSE
            for i in range(3):
                for y in range(3):
                    if(xID == i+1 and yID == y+1):#VERIFICANDO SE O CURSOR DO MOUSE ESTA ENCIMA DE RESPECTIVO BLOCO COM ID DELTA 
                        #print(f"Mouse sobre: {i+1} {y}")
                        if(data[i+(y*3)] == 0): #CASO SIM, VERIFICANDO ESSE BLOCO ESTA VAZIO (VALOR: 0)
                            if(vez == 1): #SE VAZIO E SE A VEZ FOR DO 1(BOLA), COLOCAR VALOR 1 NO BLOCO
                                data[i+(y*3)] = 1
                                vez = 2
                            else: #SE NÃO, COLOCAR VALOR 2(X)
                                data[i+(y*3)] = 2
                                vez = 1
         
    
                    
        
        
   
