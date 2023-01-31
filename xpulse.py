import pygame
import time

# Inicializa Pygame
pygame.init()

# Define el tamaño de la ventana
window_size = (450,450)

# Crea una ventana con el tamaño especificado
screen = pygame.display.set_mode(window_size)

# Define el tamaño de cada cuadro en la matriz
square_size = 50

# Define el color negro
black = (0,0,0)

# Define el color grisáceo
light_grey = (100,100,100)

# Dibuja la matriz de 9x9
for i in range(9):
    for j in range(9):
        pygame.draw.rect(screen, black, (j*square_size,i*square_size,square_size,square_size),1)

# Mostrar la ventana
pygame.display.update()

# Recorrer la matriz y resaltar la posición actual
for i in range(9):
    for j in range(9):
        # Resaltar la posición actual
        pygame.draw.rect(screen, light_grey, (j*square_size,i*square_size,square_size,square_size),0)
        pygame.display.update()
        # Esperar 1 segundo
        time.sleep(1)
        # Volver a dibujar el cuadro en negro
        pygame.draw.rect(screen, black, (j*square_size,i*square_size,square_size,square_size),1)
        pygame.display.update()

# Cierra Pygame
pygame.quit()
