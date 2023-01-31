import pygame
import time

pygame.init()

# Definir tamaño de la ventana
screen = pygame.display.set_mode((300, 300))

# Definir tamaño de los cuadrados
square_size = 100

# Crear una matriz de 3x3 con cuadrados grises
squares = [[(127, 127, 127) for j in range(3)] for i in range(3)]

# Crear un botón en la esquina superior derecha y cambiarle el color a verde
button_width = 100
button_height = 50
button_x = 200
button_y = 0
button_color = (0, 255, 0)

# Bucle de eventos
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Obtener posición del cursor
            mouse_x, mouse_y = pygame.mouse.get_pos()
            # Verificar si se clicó el botón
            if (
                button_x <= mouse_x <= button_x + button_width and
                button_y <= mouse_y <= button_y + button_height
            ):
                # Iniciar iteración sobre la matriz en orden de filas y columnas
                for i in range(3):
                    for j in range(3):
                        # Mostrar la posición actual
                        squares[i][j] = (min(squares[i][j][0] + 10, 255), min(squares[i][j][1] + 10, 255), min(squares[i][j][2] + 10, 255))
                        pygame.draw.rect(screen, squares[i][j], (j * square_size, i * square_size, square_size, square_size))
                        pygame.display.update()
                        time.sleep(1)
                        # Volver al color original
                        squares[i][j] = (127, 127, 127)
    # Dibujar los cuadrados y el botón en la pantalla
    for i in range(3):
        for j in range(3):
            pygame.draw.rect(screen, squares[i][j], (j * square_size, i * square_size, square_size, square_size))
    pygame.draw.rect(screen, button_color, (button_x, button_y, button_width, button_height))

    # Actualizar la pantalla
    pygame.display.update()

# Salir de Pygame
pygame.quit()
