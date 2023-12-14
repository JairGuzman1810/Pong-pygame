import pygame, sys

# Setup general
pygame.init()
clock = pygame.time.Clock()

# Configuraciones de la ventana principal
width = 1024
height = 768
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Pong')

# Game Rect, como se ponen objeto, dibujos en el juego
ball = pygame.Rect(width / 2 - 15, height / 2 - 15, 30, 30)
player = pygame.Rect(width - 20, height / 2 - 70, 10, 140)
opponent = pygame.Rect(10, height / 2 - 70, 10, 140)

#Ejemplos de como poner colores, hay dos formas
bg_color = pygame.Color('grey12')
light_grey = (200, 200, 200)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    #Visuales (El orden importa)
    #Color de fondo de la pantalla
    screen.fill(bg_color)
    #Colores de los elementos jugadores y la bola
    pygame.draw.rect(screen, light_grey, player)
    pygame.draw.rect(screen, light_grey, opponent)
    pygame.draw.ellipse(screen, light_grey, ball)
    #Linea de medio
    pygame.draw.aaline(screen, light_grey, (width / 2, 0), (width / 2, height))
    # Dibuja el contenido en la ventana
    pygame.display.flip()
    clock.tick(60)
