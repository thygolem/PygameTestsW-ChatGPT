import pygame
import time

# Inicializa Pygame
pygame.init()

# Define el tamaño de la ventana
window_size = (450,450)

# Crea una ventana con el tamaño especificado
screen = pygame.display.set_mode(window_size)

# Define el título de la ventana
pygame.display.set_caption('Eye-Hand Coordination Game')



# Define el tamaño de cada cuadro en la matriz
square_size = 50

# Define el color negro
black = (0,0,0)

# Definir color del botón y posición
button_color = (255, 0, 0)
button_x = 150
button_y = 150
button_width = 100
button_height = 50

# Define el color grisáceo
light_grey = (100,100,100)

# Dibuja la matriz de 9x9
for i in range(3):
    for j in range(3):
        pygame.draw.rect(screen, black, (j*square_size,i*square_size,square_size,square_size),1)


# Dibujar el botón en la pantalla
pygame.draw.rect(screen, button_color, (button_x, button_y, button_width, button_height))




# Mostrar la ventana
pygame.display.update()

# Recorrer la matriz y resaltar la posición actual
for i in range(3):
    for j in range(3):
        # Resaltar la posición actual
        pygame.draw.rect(screen, light_grey, (j*square_size,i*square_size,square_size,square_size),0)
        pygame.display.update()
        # Esperar 1 segundo
        time.sleep(1)
        # Volver a dibujar el cuadro en negro
        pygame.draw.rect(screen, black, (j*square_size,i*square_size,square_size,square_size),1)
        pygame.display.update()

# Bucle de eventos
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Obtener posición del cursor
            mouse_x, mouse_y = pygame.mouse.get_pos()
            # Verificar si el cursor está dentro del botón
            if button_x <= mouse_x <= button_x + button_width and button_y <= mouse_y <= button_y + button_height:
                print("Botón presionado")

# Cierra Pygame
pygame.quit()
