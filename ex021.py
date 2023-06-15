# Exercício Python 021: Faça um programa em python que abra e reproduza
# o áudio de um arquivo mp3

import pygame
pygame.mixer.init()
pygame.mixer.music.load('nome_do_arquivo.mp3')
pygame.mixer.music.play()
input()
pygame.event.wait()
