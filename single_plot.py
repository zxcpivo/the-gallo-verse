import pygame


pygame.init()

WIDTH = 640
HEIGHT = 480
SIZE = (WIDTH, HEIGHT)

screen = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()

# ---------------------------
# Initialize global variables for animation
# These must have your name in there

circle_x_gallo = 200
circle_y_gallo = 200

# ---------------------------

running = True
while running:
    # EVENT HANDLING
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # GAME STATE UPDATES
    # All game math and comparisons happen here
    circle_x_gallo += 1

    # DRAWING
    # Must have these coordinates
    x = 0
    y = 0
    width = 640
    height = 480

    # Rather than screen.fill, draw a rectangle
    pygame.draw.rect(screen, (255, 255, 255), (x, y, width, height))

    # Must draw with reference to that coordinate
    pygame.draw.circle(screen, (0, 0, 255), (x + circle_x_gallo, y + circle_y_gallo), 30)

    # Must be the last two lines
    # of the game loop
    pygame.display.flip()
    clock.tick(30)
    #---------------------------


pygame.quit()
