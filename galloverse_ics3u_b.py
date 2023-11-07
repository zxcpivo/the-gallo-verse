# pygame template
import math
import random
import pygame

def linear_interpolation(x, x0, x1, y0, y1):
    return y0 + (x - x0) * (y1 - y0) / (x1 - x0)


pygame.init()
pygame.font.init()


WIDTH = 1920
HEIGHT = 1080
SIZE = (WIDTH, HEIGHT)

window = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()

num_students = 33
MAP_SIZE = math.ceil(math.sqrt(num_students))
MAP_SIZE += 1 - MAP_SIZE % 2
MID = MAP_SIZE//2
PLOT_WIDTH = 640
PLOT_HEIGHT = 480
MIN_SCALE = HEIGHT/(MAP_SIZE*PLOT_HEIGHT)
MAX_SCALE = 1
screen = pygame.Surface((PLOT_WIDTH * MAP_SIZE, PLOT_HEIGHT * MAP_SIZE))
camera_x = screen.get_width()//2
camera_y = screen.get_height()//2
zoom_level_gallo = 1 # 1-10
grid_font = pygame.font.SysFont('Arial', 20)


# ---------------------------
# Initialize global variables for animation
# These must have your name in there

font_gallo = pygame.font.SysFont('Arial', 120)
welcome_font_gallo = pygame.font.SysFont('Arial', 40)
bg_color_gallo = "#E15E03"
# fg_color_gallo = "#FF9142"
fg_color_gallo = "#FEC661"
text_gallo = font_gallo.render("The Gallo-verse", True, fg_color_gallo)
welcome_text_gallo = welcome_font_gallo.render("Welcome to", True, fg_color_gallo)
frames_gallo = 0
bg_start = pygame.Color("#E05F02")
bg_end = pygame.Color("#6B2D01")
bg_gallo_large = pygame.Surface((1000, 1000))
bg_gallo_large.fill((0, 0, 0))
for x in range(1000):
    pygame.draw.line(bg_gallo_large, bg_end.lerp(bg_start, x/1000), (x, 0), (x, 1000))
bg_gallo_large = pygame.transform.rotate(bg_gallo_large, -45)
bg_gallo = pygame.Surface((640, 480))
bg_gallo.blit(bg_gallo_large, (-500, -500))
welcome_text_buffer = {}
# ---------------------------

circle_x_michael = 200
circle_y_michael = 50

rect_x_michael = 10
rect_y_michael = 20

michael_frames_1 = 0
michael_frames_2 = 0


# ------------------

tank_x_oscar = 0
tank_y_oscar = 0

oscar_shell_x_offset = 340
oscar_shell_y_offset = 330

oscar_shell_x = oscar_shell_x_offset
oscar_shell_y = oscar_shell_y_offset

oscar_shell_v_y_original = 10
oscar_shell_v_x = 80
oscar_shell_v_y = oscar_shell_v_y_original

oscar_shell_fired = False
oscar_exploded = False
oscar_player_controlled = False

# -------------------
ryan_x = 0
ryan_y = 0
triy1 = 190
triy2 = 290
ryan_closed = True
# ---------
# Conditional Variables
daniel_scan = False
daniel_blink = False
daniel_blink_close = False
daniel_blink_open = False
daniel_stare = False
daniel_stare_count = 150
daniel_action_selection = True
daniel_look_left = False
daniel_look_right = False
daniel_look_center = False

# Dimensional Variables
# Sclera
daniel_sclera_width = 550
daniel_sclera_height = 200
daniel_sclera_x = (640 - daniel_sclera_width) / 2
daniel_sclera_y = (480 - daniel_sclera_height) / 2
# Eyelid: Back
daniel_eyelid_back_width = daniel_sclera_width + 10
daniel_eyelid_back_height = daniel_sclera_height + 40
daniel_eyelid_back_x = daniel_sclera_x - 5
daniel_eyelid_back_y = daniel_sclera_y - 20
# Eyelid: Front
daniel_eyelid_front_width = daniel_eyelid_back_width - 90
daniel_eyelid_front_height = daniel_eyelid_back_height - 130
daniel_eyelid_front_x = daniel_eyelid_back_x + 45
daniel_eyelid_front_y = daniel_eyelid_back_y + 10

# Pupil
daniel_pupil_radius = 150
daniel_pupil_x = (640 - daniel_pupil_radius) / 2
daniel_pupil_y = (480 - daniel_pupil_radius) / 2


colour_lucas = (0, 0, 255)

car_lucas_x = 50
car_lucas_y = 380

circle_palmar_x = 340
circle_palmar_y = 440
car_go_back = False

bomb_lucas_x = 160
bomb_lucas_y = 430

sun_lucas_x = 0
sun_lucas_y = 350


font_lucas = pygame.font.SysFont('Raider', 50)
text_lucas = font_lucas.render("Lucas P is the Best", True, (0, 0, 0))
text_lucas_x = 160
text_lucas_y = 100




running = True
while running:
    # GALLO VERSE SPECIFIC ----------------------------------------------------------------
    scale = linear_interpolation(zoom_level_gallo, 10, 1, MIN_SCALE, MAX_SCALE)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEWHEEL:
            direction = event.y
            zoom_level_gallo -= direction
            zoom_level_gallo = max(min(zoom_level_gallo, 10), 1)
        elif event.type == pygame.MOUSEMOTION:
            click, _, _ = event.buttons
            if click:
                dx, dy = event.rel
                camera_x += -dx/scale
                camera_y += -dy/scale

    # DRAWING
    screen.fill((255, 255, 255))
    window.fill((100, 100, 100))

    # Draw Plot points
    for x in range(0, MAP_SIZE * PLOT_WIDTH, PLOT_WIDTH):
        for y in range(0, MAP_SIZE * PLOT_HEIGHT, PLOT_HEIGHT):
            pygame.draw.circle(screen, (30, 30, 200), (x, y), 5)
            coord_text = grid_font.render(f"({x}, {y})", False, (0, 0, 0))
            screen.blit(coord_text, (x, y))
    # --------------------------
        # GAME STATE UPDATES
    if daniel_action_selection is True:
        daniel_blink_or_scan = random.randint(1, 100)
        if daniel_blink_or_scan % 2 == 0:
            daniel_stare = True
            daniel_stare_count = 60
            daniel_action_selection = False
        elif daniel_blink_or_scan % 2 !=0:
            if daniel_blink_or_scan < 60:
                daniel_scan = True
                daniel_look_left = True
                daniel_action_selection = False
            elif daniel_blink_or_scan >= 60:
                daniel_blink = True
                daniel_blink_close = True
                daniel_action_selection = False
    
    

    # DRAWING
    x = 3 * 640
    y = 1 * 480
    width = 640
    height = 480

    # Rather than screen.fill, draw a rectangle
    pygame.draw.rect(screen, (125, 0, 0), (x, y, width, height))
    # Drawings & Animations
    # Eyelid: Back
    pygame.draw.ellipse(screen, (75, 0, 0), (x + daniel_eyelid_back_x, 
                                            y + daniel_eyelid_back_y, 
                                            daniel_eyelid_back_width, 
                                            daniel_eyelid_back_height))
    # Sclera
    pygame.draw.ellipse(screen, (240, 240, 240), (x + daniel_sclera_x, 
                                                  y + daniel_sclera_y,
                                                  daniel_sclera_width, 
                                                  daniel_sclera_height))
    # Pupil
    # Stare
    if daniel_blink is True:
        pygame.draw.ellipse(screen, (0, 0, 0), (x + daniel_pupil_x, 
               y + daniel_pupil_y, 
                daniel_pupil_radius, 
                daniel_pupil_radius))
    
    elif daniel_stare is True:
        pygame.draw.ellipse(screen, (0, 0, 0), (x + daniel_pupil_x, 
                                               y + daniel_pupil_y, 
                                                daniel_pupil_radius, 
                                                daniel_pupil_radius))
        if daniel_stare_count == 0:
            daniel_stare = False
            daniel_action_selection = True
        daniel_stare_count -= 1
    # Look Left
    elif daniel_scan is True:
        if daniel_look_left is True:
            pygame.draw.ellipse(screen, (0, 0, 0), (x + daniel_pupil_x, 
                   y + daniel_pupil_y, 
                    daniel_pupil_radius, 
                    daniel_pupil_radius))
            if daniel_pupil_x == 145:
                daniel_look_left = False
                daniel_look_right = True
            daniel_pupil_x -= 1
    # Look Right
        elif daniel_look_right is True:
            pygame.draw.ellipse(screen, (0, 0, 0), (x + daniel_pupil_x, 
                   y + daniel_pupil_y, 
                    daniel_pupil_radius, 
                    daniel_pupil_radius))
            if daniel_pupil_x == 345:
                daniel_look_right = False
                daniel_look_center = True
            daniel_pupil_x += 1
        # Look Center
        elif daniel_look_center is True:
            pygame.draw.ellipse(screen, (0, 0, 0), (x + daniel_pupil_x, 
                   y + daniel_pupil_y, 
                    daniel_pupil_radius, 
                    daniel_pupil_radius))
            if daniel_pupil_x == 245:
                daniel_look_center = False
                daniel_scan = False
                daniel_action_selection = True
            daniel_pupil_x -= 1

    #  Blink Not True
    if daniel_blink is False:
        pygame.draw.ellipse(screen, (75, 0, 0), (x + daniel_eyelid_front_x,
                                                y+ daniel_eyelid_front_y,
                                                daniel_eyelid_front_width,
                                                daniel_eyelid_front_height))
    # Blink True
    if daniel_blink is True:
        if daniel_blink_close is True:
            pygame.draw.ellipse(screen, (75, 0, 0), (x + daniel_eyelid_front_x,
                y + daniel_eyelid_front_y,
                daniel_eyelid_front_width,
                daniel_eyelid_front_height))
            daniel_eyelid_front_height += 4
            daniel_eyelid_front_width += 3.2
            daniel_eyelid_front_x -= 1.6
            if daniel_eyelid_front_height >= 230:
                daniel_blink_close = False
                daniel_blink_open = True
        elif daniel_blink_open is True:
            pygame.draw.ellipse(screen, (70, 0, 0), (x + daniel_eyelid_front_x,
                y + daniel_eyelid_front_y,
                daniel_eyelid_front_width,
                daniel_eyelid_front_height))
            daniel_eyelid_front_height -= 4
            daniel_eyelid_front_width -= 3.2
            daniel_eyelid_front_x += 1.6
            if daniel_eyelid_front_height == 110:
                daniel_blink_open = False
                daniel_blink = False
                daniel_action_selection = True
    # -------------------
    if triy1 < 240 and triy2 > 240 and ryan_closed is True:
        triy1 += 5
        triy2 -= 5
        if triy1 == 240 and triy2 == 240:
            ryan_closed = False
    elif not ryan_closed:
        triy1 -= 5
        triy2 += 5
        if triy1 == 190 and triy2 == 290:
            ryan_closed = True

    # DRAWING
    pygame.draw.rect(screen, (0, 0, 0), (ryan_x, ryan_y, width, height))    
        # Pac-Man
    pygame.draw.ellipse(screen, (255, 255, 0), (ryan_x + 100, ryan_y + 140, 200, 200))
    pygame.draw.polygon(screen,(0, 0, 0),[(ryan_x+200, ryan_y+240),
                                        (ryan_x+300,ryan_y+triy1), (ryan_x+300,
                                                                    ryan_y+triy2)])
        # Pellets
    pygame.draw.ellipse(screen, (255,255, 255), (ryan_x + 335, ryan_y + 227.5, 25, 25))
    pygame.draw.ellipse(screen, (255,255, 255), (ryan_x + 410, ryan_y + 227.5, 25, 25))
    pygame.draw.ellipse(screen, (255,255, 255), (ryan_x + 485, ryan_y + 227.5, 25, 25))
    pygame.draw.ellipse(screen, (255,255, 255), (ryan_x + 560, ryan_y + 227.5, 25, 25))

    #-------------
    # DRAWING
    # Must have these coordinates
    x = 640 * 2
    y = 480 * 4
    width = 640
    height = 480
    font = pygame.font.Font('freesansbold.ttf', 32)
    font2 = pygame.font.Font('freesansbold.ttf', 100)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        oscar_player_controlled = True
        tank_x_oscar -= 5
    if keys[pygame.K_RIGHT]:
        oscar_player_controlled = True
        tank_x_oscar += 5
    if keys[pygame.K_UP]:
        oscar_player_controlled = True
        tank_y_oscar -= 5
    if keys[pygame.K_DOWN]:
        oscar_player_controlled = True
        tank_y_oscar += 5
    if keys[pygame.K_SPACE]:
        oscar_player_controlled = True
        oscar_shell_fired = True
        oscar_exploded = False
    if keys[pygame.K_r]:
        oscar_player_controlled = True
        oscar_shell_fired = False
        oscar_exploded = False
    if keys[pygame.K_b] and oscar_shell_fired:
        oscar_player_controlled = True
        oscar_shell_fired = False
        oscar_exploded = (oscar_shell_x + x + tank_x_oscar, oscar_shell_y + y + tank_y_oscar)

    if oscar_shell_fired:
        oscar_shell_x += oscar_shell_v_x
        # inverted
        oscar_shell_y -= oscar_shell_v_y
        oscar_shell_v_y -= 2
    else:
        oscar_shell_x = oscar_shell_x_offset + x
        oscar_shell_y = oscar_shell_y_offset + y
        oscar_shell_v_y = oscar_shell_v_y_original

    if not oscar_player_controlled:
        tank_x_oscar += random.randint(-5, 5)
        tank_y_oscar += random.randint(-5, 5)

    # Rather than screen.fill, draw a rectangle
    pygame.draw.rect(screen, (255, 255, 255), (x, y, width, height))

    # Drawings
    tank = pygame.draw.polygon(screen, (0, 0, 0),
                               [(x + tank_x_oscar + 29, y + tank_y_oscar + 383),
                                (x + tank_x_oscar + 54, y + tank_y_oscar + 449),
                                (x + tank_x_oscar + 184, y + tank_y_oscar + 453),
                                (x + tank_x_oscar + 218, y + tank_y_oscar + 384)])
    pygame.draw.polygon(screen, (0, 0, 0),
                        [(x + tank_x_oscar + 53, y + tank_y_oscar + 369),
                         (x + tank_x_oscar + 184, y + tank_y_oscar + 369),
                         (x + tank_x_oscar + 170, y + tank_y_oscar + 326),
                         (x + tank_x_oscar + 68, y + tank_y_oscar + 326)])
    pygame.draw.polygon(screen, (0, 0, 0),
                        [(x + tank_x_oscar + 172, y + tank_y_oscar + 334),
                         (x + tank_x_oscar + 338, y + tank_y_oscar + 330),
                         (x + tank_x_oscar + 333, y + tank_y_oscar + 346),
                         (x + tank_x_oscar + 177, y + tank_y_oscar + 353)])
    pygame.draw.circle(screen, (255, 255, 255), (79 + tank_x_oscar + x, 420 + tank_y_oscar + y), 25)
    pygame.draw.circle(screen, (255, 255, 255), (151 + tank_x_oscar + x, 420 + tank_y_oscar + y), 25)

    if oscar_shell_fired:
        pygame.draw.circle(screen, (23, 25, 79), (x + tank_x_oscar + oscar_shell_x, y + tank_y_oscar + oscar_shell_y),
                           25)
    if oscar_exploded:
        pygame.draw.circle(screen, (181, 114, 27), oscar_exploded, random.randint(50, 60))
        bombtext = font2.render('OSCAR WAS HERE', True, (0, 0, 0))
        screen.blit(bombtext, (oscar_exploded[0], oscar_exploded[1] - 200))

    text = font.render('Oscar\'s Tile: U/D/L/R = arrow keys', True, (0, 0, 0))
    text2 = font.render('Fire = SPACE | Reset = R | Detonate = B', True, (0, 0, 0))
    screen.blit(text, (x, y))
    screen.blit(text2, (x, y + 35))
    
    # -----------
    x = 1280
    y = 960
    width = 640
    height = 480
    michael_frames_1 += 150
    michael_frames_2 -= 150

    pygame.draw.rect(screen, (23, 255, 100), (x, y + 280, 640, 200))
    pygame.draw.rect(screen, (135, 206, 235), (x, y, 640, 280))


    x_trees_michael = 0
    while x_trees_michael < 672:
        pygame.draw.rect(screen, (139, 69, 19), (x + x_trees_michael + 0, y + 230, 20, 50))
        pygame.draw.polygon(screen, (0, 140, 0), ((x + x_trees_michael - 19, y + 240), (x + x_trees_michael + 16, y + 122), (x + x_trees_michael + 39, y + 237)))
        pygame.draw.polygon(screen, (0, 150, 0), ((x + x_trees_michael - 19, y + 220), (x + x_trees_michael + 16, y + 102), (x + x_trees_michael + 39, y + 227)))
        pygame.draw.polygon(screen, (0, 200, 0), ((x + x_trees_michael - 19, y + 200), (x + x_trees_michael + 16, y + 92), (x + x_trees_michael + 39, y + 217)))
        x_trees_michael += 84

    x_people_michael = 0
    while x_people_michael < 270:
        pygame.draw.circle(screen, (0, 25, 0), (x + 200 + x_people_michael, y + 202), 20)
        pygame.draw.rect(screen, (0, 25, 0), (x + 195 + x_people_michael, y + 210, 10, 80))
        pygame.draw.circle(screen, (255, 255, 255), (x + 200 + x_people_michael, y + 202), 10)
        pygame.draw.circle(screen, (255, 20, 147), (x + 200 + x_people_michael, y + 202), 7)
        pygame.draw.circle(screen, (0, 25, 0), (x + 200 + x_people_michael, y + 202), 5)
        pygame.draw.polygon(screen, (240, 240, 240), ((x + 200 + x_people_michael, y + 272), (x + 165 + x_people_michael, y + 222), (x + 225 + x_people_michael, y + 222)))
        pygame.draw.rect(screen, (170, 170, 170), (x + 195 + x_people_michael, y + 222, 10, 51))
        y_button_michael = 0
        while y_button_michael < 40:
            pygame.draw.circle(screen, (100, 100, 100), (x + 200 + x_people_michael, y + 230 + y_button_michael), 3)
            y_button_michael += 10

        x_people_michael += 90
        x = 1920
    y = 1920
    width = 640
    height = 480
    pygame.draw.rect(screen, (0, 0, 255), (x, y, width, height))
    initial_bomb_x = x -  1900
    
    if not car_go_back:
        car_lucas_x += 4
        if car_lucas_x >= 400:
            car_go_back = True
    elif car_go_back:
        car_lucas_x -= 4
        car_go_back = True
        if car_lucas_x <= 0:
            car_go_back = False
    
    if sun_lucas_x <= 444:
        sun_lucas_x += 4
        sun_lucas_y -= 2
    elif sun_lucas_x == 800:
        sun_lucas_x = 0
        sun_lucas_y = 350
    else:
        sun_lucas_x += 4
        sun_lucas_y += 2

    pygame.draw.rect(screen, (0, 0 , 0), ( x + car_lucas_x + 200, y + car_lucas_y, 100, 20))
    pygame.draw.rect(screen, (20, 20 , 20), ( x + 50, y + 250, 100, 200))
    pygame.draw.rect(screen, (20, 20 , 20), ( x + 500, y + 250, 100, 200))
    pygame.draw.rect(screen, (20, 20 , 20), ( x + 300, y + 250, 100, 200))
    pygame.draw.rect(screen, (0, 255 , 0), ( x + car_lucas_x, y + car_lucas_y, 200, 100))
    pygame.draw.circle(screen, (0, 255, 0), (x + car_lucas_x + 50, y + car_lucas_y), 60)
    pygame.draw.circle(screen, (200, 230, 0), (x + sun_lucas_x, y + sun_lucas_y), 60)
    pygame.draw.rect(screen, (20, 20 , 20), ( x + 40, y + 250, 100, 200))
    pygame.draw.rect(screen, (20, 80 , 20), ( x + 40, y + 420, 200, 50))
    pygame.draw.rect(screen, (250, 250 , 250), ( x + 25, y + 50, 150, 50))
    pygame.draw.rect(screen, (250, 250 , 250), ( x + 65, y + 30, 50, 50))
    pygame.draw.rect(screen, (250, 250 , 250), ( x + 300, y + 50, 150, 50))
    pygame.draw.rect(screen, (250, 250 , 250), ( x + 35, y + 30, 50, 50))
    screen.blit(text_lucas, (x + text_lucas_x, y + text_lucas_y))

    if car_lucas_x >= 90:
        pygame.draw.circle(screen, (0, 0, 0), (x + bomb_lucas_x, y + bomb_lucas_y), 60)
        bomb_lucas_x += 25
        if bomb_lucas_x >= 2500:
            bomb_lucas_x = initial_bomb_x
    # ----------------------------------------------------------------------------------------

    # Must have these coordinates
    x = 1920
    y = 1440
    width = 640
    height = 480

    frames_gallo += 1
    text_scale_gallo = abs((math.sin(frames_gallo / 30) - 3) / 3)
    

    # Rather than screen.fill, draw a rectangle
    screen.blit(bg_gallo, (x, y))

    screen.blit(welcome_text_gallo, (x + width//2 - welcome_text_gallo.get_width()//2, y + height//3 - welcome_text_gallo.get_height()//2))
    scaled_text = pygame.transform.scale(text_gallo, (text_gallo.get_width() * text_scale_gallo, text_gallo.get_height() * text_scale_gallo))
    screen.blit(scaled_text, (x + width//2 - scaled_text.get_width()//2, y + height//2 - scaled_text.get_height()//2))
    


    # LEAVE HERE --------------------------------------------
    screen_width, screen_height = screen.get_size()
    scaled_screen = pygame.transform.scale(screen, (int(screen_width * scale), int(screen_height * scale)))
    window.blit(scaled_screen, (-camera_x*scale+WIDTH//2, -camera_y*scale+HEIGHT//2))

    pygame.display.flip()
    clock.tick(30)
    #---------------------------------------------------------


pygame.quit()
