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
# Moon Positions
moon_x_hayden = 200
inner_moon_x_hayden = 180
inner_moon_x_hayden2 = 220
moon_y_hayden = 50
inner_moon_y_hayden = 65
inner_moon_y_hayden2 = 25

# ---------------------
sun_x_anthony = 570
sun_y_anthony = random.randrange(70, 410)
moon_x_anthony = 600
moon_y_anthony = random.randrange(30, 451)
rock_x_anthony = 600
rock_y_anthony = random.randrange(20, 460)
radius_fire = 1

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
# ----------------------
circle_x_tren = 200
circle_y_tren = 200
direction_x = 1

#-------------------------------------
gloria_x = 640
gloria_y = 0
gloria_width = 640
gloria_height = 480
circle_x_gloria = gloria_x
circle_y_gloria = gloria_y 
crash_gloria = False
gloria_frames = 0
#---------------------------------------------
#ayda lava
ayda_amplitude = 10
ayda_frequency = 0.03
ayda_phase = 0

#ayda colours
AYDA_SKY = (250, 180, 150)
AYDA_LAVA = (255, 95, 0)
AYDA_BROWN = (94, 69, 54)
AYDA_RED = (200, 2, 2)
AYDA_GREY = (40, 60, 60)
AYDA_GREEN = (10, 150, 10)
AYDA_BLUE = (46,103,248)

#ayda text
ayda_font = pygame.font.Font('freesansbold.ttf', 40)
ayda_text = ayda_font.render("I HAVE THE HIGH GROUND.", True, AYDA_RED, AYDA_SKY)
ayda_textRect = ayda_text.get_rect()
ayda_textRect.topleft = (WIDTH // 2, HEIGHT // 2)
# ------------------

# ---------------------
circle_x_adeline = 500 
circle_y_adeline = 80 
ellipse_x_adeline = 200 
ellipse_y_adeline = 50 
line_x_adeline = 300 
line_y_adeline = 215 

# ----------------------------------------
w_henry = 1
bomb_henry = False
h_henry = 0
x_henry = 0
y_henry = 0
WIDTH_henry = 640
HEIGHT_henry = 480

rect_x_henry = 250
rect_y_henry = 200
circle_x_henry = 260
circle_y_henry = 150
bomb_x_henry = 262
bomb_y_henry = 70
bomb_stopped_henry = False
# -----------------------------------



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


    # -----------
    x = 640 * 5
    y = 480 * 4
    width = 640
    height = 480

    # Moving Moon
    moon_x_hayden += 6
    inner_moon_x_hayden += 6
    inner_moon_x_hayden2 += 6

    # Background Code
    pygame.draw.rect(screen, (0, 0, 140), (x, y, width, height))
    pygame.draw.rect(screen, (5, 107, 5), (x, y + 400, width, height - 400))

    for star in range (50):
        star_x_hayden = random.randint(1, 640)
        star_y_hayden = random.randint(1, 400)
        pygame.draw.circle(screen, (225, 225, 5), (x + star_x_hayden, y + star_y_hayden), 3)

    pygame.draw.circle(screen, (120, 120, 120), (x + moon_x_hayden, y + moon_y_hayden), 60)
    # Code for the inner parts of moon
    pygame.draw.circle(screen, (60, 60, 60), (x + inner_moon_x_hayden, y + inner_moon_y_hayden), 30)
    pygame.draw.circle(screen, (60, 60, 60), (x + inner_moon_x_hayden2, y + inner_moon_y_hayden2), 18)
    
    # Code for building in back
    pygame.draw.rect(screen, (40, 40, 40), (x + 450, y + 130, 130, 320))
    pygame.draw.rect(screen, (40, 40, 40), (x + 40, y + 150, 130, 320))
    
    
    # Code for buildings in front
    pygame.draw.rect(screen, (20, 20, 20), (x + 480, y + 280, 70, 150))
    pygame.draw.rect(screen, (20, 20, 20), (x + 560, y + 270, 70, 150))
    pygame.draw.rect(screen, (20, 20, 20), (x + 80, y + 280, 70, 150))
    pygame.draw.rect(screen, (20, 20, 20), (x + 0 , y + 270, 70, 150))
    
    # Code for person
    pygame.draw.circle(screen, (0, 0, 0), (x + 320, y + 300), 30)
    pygame.draw.rect(screen, (0, 0, 0), (x + 300, y + 325, 40, 75))
    pygame.draw.rect(screen, (0, 0, 0), (x + 290, y + 340, 10, 30))
    pygame.draw.polygon(screen, (0, 0, 0), [(x + 330, y + 330), (x + 350, y + 340), (x + 370, y + 300), (x + 360, y + 290)])

    # Looping Moon
    if moon_x_hayden > 640 - 60:
        moon_x_hayden = 0
        inner_moon_x_hayden = -20
        inner_moon_x_hayden2 = 20
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

    #----------------------------
    x = 3200
    y = 1440
    width = 640
    height = 480
    y_engine_anthony = 0
    number_of_engines_anthony = 3
    x_window_anthony = 300
    y_window_anthony = 275
    number_of_windows_anthony = 8
    count_anthony = 0
    moon_x_anthony -= 2
    sun_x_anthony -= 4
    rock_x_anthony -= 6
    
    # Background
    pygame.draw.rect(screen, (8, 23, 54), (x, y, width, height))

    # # Crazy Star Code
    for star in range(20):
        x_star_anthony = random.randrange(1, 640)
        y_star_anthony = random.randrange(1, 480)
        pygame.draw.circle(screen, (225, 225, 225), (x + x_star_anthony, y + y_star_anthony), 1)
 
    # Planet Code
    pygame.draw.circle(screen, (217, 106, 28), (x + sun_x_anthony, y + sun_y_anthony), 60)
    pygame.draw.circle(screen, (219, 167, 44), ((x + sun_x_anthony), y + sun_y_anthony), 55)
    pygame.draw.ellipse(screen, (92, 73, 28), ((x + sun_x_anthony) - 72, y + sun_y_anthony, 145, 10))
    if sun_x_anthony < 75:
        sun_x_anthony = 570
        sun_y_anthony = random.randrange(70, 410)

    pygame.draw.circle(screen, (137, 116, 116), (x + moon_x_anthony, y + moon_y_anthony), 30)
    pygame.draw.circle(screen, (105, 87, 87), ((x + moon_x_anthony) + 10, (y + moon_y_anthony) + 6), 10)
    pygame.draw.circle(screen, (105, 87, 87), ((x + moon_x_anthony) - 15, (y + moon_y_anthony) - 10), 7)
    if moon_x_anthony < 40:
        moon_x_anthony = 600
        moon_y_anthony = random.randrange(30, 451)
    
    pygame.draw.polygon(screen, (225, 0, 0), ((x + rock_x_anthony + 2, y + rock_y_anthony - 12), (x + rock_x_anthony + 2, y + rock_y_anthony + 12), (x + rock_x_anthony + 40, y + rock_y_anthony)))
    pygame.draw.circle(screen, (56, 56, 56), (x + rock_x_anthony, y + rock_y_anthony), 15)
    if rock_x_anthony < 20:
        rock_x_anthony = 600
        rock_y_anthony = random.randrange(20, 451)
    
    # # Spaceship Code
    while y_engine_anthony < (30 * number_of_engines_anthony):
        pygame.draw.ellipse(screen, (217, 215, 215), (x + ((width / 2) - 125),y + (((height / 2)+ y_engine_anthony) - 5), 100, 50))
        y_engine_anthony += 30
        
    pygame.draw.ellipse(screen, (225, 225, 225), (x + ((320) - 125),y + (height / 2), 350, 100))
    
    while count_anthony <= (28 * number_of_windows_anthony):
        pygame.draw.circle(screen, (0, 0, 0), ((x + x_window_anthony),(y + y_window_anthony)), 8)
        x_window_anthony += 20
        count_anthony += 28

    # # Fire Code
    pygame.draw.circle(screen, (225, 165, 0), (x + 135, y + 290), radius_fire)
    pygame.draw.circle(screen, (225, 0, 0), (x + 190, y + 270), radius_fire + 2)
    pygame.draw.circle(screen, (252, 0, 0), (x + 190, y + 310), radius_fire + 2)
    pygame.draw.circle(screen, (252, 102, 0), (x + 170, y + 300), radius_fire + 1)
    pygame.draw.circle(screen, (252, 102, 0), (x + 170, y + 280), radius_fire + 1)
    radius_fire += 2
    if radius_fire > 12:
        radius_fire = 1

    # Rock Hits Rocket
    if (y + rock_y_anthony) <= (y + 350) and (y + rock_y_anthony) >= (y + 230):
        rock_y_anthony = 290
        if (x + rock_x_anthony) < (x + 540):
            pygame.draw.circle(screen, (225, 0, 0), (x + 540, y + 290), 50)
            pygame.draw.circle(screen, (225, 100, 0), (x + 540, y + 290), 30)

    # ----------------------------------------------------------------------------------------

    x = 3200
    y = 2400

    pygame.draw.rect(screen, (63, 155, 11), (x, y, width, height))
    pygame.draw.rect(screen, (255, 255, 255), (x, y, width, 300))

    ellipse_x_adeline += 1

    if ellipse_x_adeline == x + width:
        ellipse_x_adeline = x

    # CLOUD 1 (dark blue)
    pygame.draw.ellipse(screen, (0, 0, 255), (ellipse_x_adeline + x, ellipse_y_adeline + y, 135, 65))
    pygame.draw.ellipse(screen, (0, 0, 255), (-85 + ellipse_x_adeline + x, ellipse_y_adeline + y, 135, 65))
    # SUN
    pygame.draw.circle(screen, (255, 255, 0), (circle_x_adeline + x, circle_y_adeline + y), 75)
    # CLOUD 2 (light blue)
    pygame.draw.ellipse(screen, (0, 150, 255), (-100 + ellipse_x_adeline + x, 80 + ellipse_y_adeline + y, 135, 65))
    pygame.draw.ellipse(screen, (0, 150, 255), (-200 + ellipse_x_adeline + x, 80 + ellipse_y_adeline + y, 135, 65))
    # FENCE (brown)
    fence_x = 100
    while fence_x < 550:
        pygame.draw.rect(screen, (150, 75, 0), (fence_x + x, y + 260, 15, 40))
        fence_x += 50
    # HEAD
    pygame.draw.circle(screen, (0, 0, 0), (-200 + circle_x_adeline + x, 100 + circle_y_adeline + y), 35, width = 5)
    # BODY
    pygame.draw.line(screen, (0, 0, 0), (line_x_adeline + x, line_y_adeline + y), (line_x_adeline + x, line_y_adeline + y + 50), width = 5)
    # ARM OVER HEAD
    pygame.draw.line(screen, (0, 0, 0), (line_x_adeline + x + 42, line_y_adeline + y - 40), (line_x_adeline + x, line_y_adeline + y + 30), width = 5)
    pygame.draw.line(screen, (0, 0, 0), (line_x_adeline + x + 42, line_y_adeline + y - 40), (line_x_adeline + x + 15, line_y_adeline + y - 50), width = 5)
    # OTHER ARM
    pygame.draw.line(screen, (0, 0, 0), (line_x_adeline + x - 40, line_y_adeline + y + 20), (line_x_adeline + x, line_y_adeline + y), width = 5)
    pygame.draw.line(screen, (0, 0, 0), (line_x_adeline + x - 40, line_y_adeline + y + 20), (line_x_adeline + x, line_y_adeline + y + 45), width = 5)
    # LEGS
    pygame.draw.line(screen, (0, 0, 0), (line_x_adeline + x, line_y_adeline + y + 50), (line_x_adeline + x + 30, line_y_adeline + y + 80), width = 5)
    pygame.draw.line(screen, (0, 0, 0), (line_x_adeline + x, line_y_adeline + y + 50), (line_x_adeline + x - 30, line_y_adeline + y + 80), width = 5)

    #in loop
    x = 640
    y = 1440
    if circle_x_tren >= x + 300:
        direction_x = -10
    elif circle_x_tren <= x + 50:
        direction_x = 10
    circle_x_tren += direction_x    
    
    stick_spawn = random.randrange(0, 640)
    horizontal_stick_spawn = random.randrange(0, 480)   
    
    
    pygame.draw.rect(screen, (0, 0, 0), (x, y, 640, 480))
    
    pygame.draw.circle(screen, (255, 255, 0), (x + circle_x_tren - 400, y + circle_y_tren), 35)
    pygame.draw.rect(screen, (0, 0, 0), (x + circle_x_tren - 422, y + circle_y_tren + 3, 27, 39))
    pygame.draw.rect(screen, (255, 0, 80), (x + circle_x_tren - 420, y + circle_y_tren + 5, 23, 35))
    pygame.draw.circle(screen, (0, 0, 0), (x + circle_x_tren - 420, y + circle_y_tren - 5), 5)
    pygame.draw.circle(screen, (0, 0, 0), (x + circle_x_tren - 395, y + circle_y_tren - 5), 5)
    pygame.draw.rect(screen, (0, 0, 0), (x + circle_x_tren - 440, y + circle_y_tren - 50, 80, 10))
    pygame.draw.rect(screen, (0, 0, 0), (x + circle_x_tren - 440, y + circle_y_tren - 50, 80, 10))
    pygame.draw.rect(screen, (255, 0, 0), (x + circle_x_tren - 438, y + circle_y_tren - 48, 76, 6))
    pygame.draw.rect(screen, (165, 42, 42), (x + stick_spawn, y, 10, 100))
    pygame.draw.rect(screen, (0, 255, 255), (x + stick_spawn, y + 100, 10, 380))
    pygame.draw.rect(screen, (165, 42, 42), (x, y + horizontal_stick_spawn, 100, 10))
    pygame.draw.rect(screen, (255, 0, 0), (x + 100, y + horizontal_stick_spawn, 540, 10))
    
    #-----------------------------------------------------------------------------------------

    if circle_y_gloria <= gloria_y + 190:
        circle_x_gloria += 1
        circle_y_gloria += 2
    gloria_frames += 1
    if gloria_frames % 130 == 0:
        circle_y_gloria = gloria_y
        circle_x_gloria = gloria_x
        crash_gloria = False

    pygame.draw.rect(screen, (255, 255, 255), (gloria_x, gloria_y, gloria_width, gloria_height))
    pygame.draw.rect(screen, (0, 0, 0), (gloria_x, gloria_y, gloria_width, gloria_height), 7)

    pygame.draw.circle(screen, (251, 236, 93), (circle_x_gloria, circle_y_gloria), 30)
    pygame.draw.circle(screen, (255, 0, 0), (gloria_x + 200, gloria_y + 40), 10)
    pygame.draw.circle(screen, (255, 0, 0), (gloria_x + 350, gloria_y + 70), 4)
    pygame.draw.circle(screen, (255, 0, 0), (gloria_x + 500, gloria_y + 200), 7)
    pygame.draw.circle(screen, (255, 0, 0), (gloria_x + 245, gloria_y + 200), 9)
    pygame.draw.circle(screen, (255, 0, 0), (gloria_x + 405, gloria_y + 275), 3)
    pygame.draw.circle(screen, (255, 0, 0), (gloria_x + 550, gloria_y + 55), 6)
    pygame.draw.circle(screen, (255, 0, 0), (gloria_x + 72, gloria_y + 50), 5)
    star = [
        (gloria_x + 422, gloria_y + 86),
        (gloria_x + 412, gloria_y + 99),
        (gloria_x + 403, gloria_y + 107),
        (gloria_x + 416, gloria_y + 117),
        (gloria_x + 427, gloria_y + 139),
        (gloria_x + 432, gloria_y + 112),
        (gloria_x + 449, gloria_y + 104),
        (gloria_x + 435, gloria_y + 99),
        (gloria_x + 422, gloria_y + 85)
    ]
    pygame.draw.polygon(screen, (255, 0, 0), (star))

    # skyscraper
    pygame.draw.rect(screen, (255, 255, 255), (gloria_x + 35, gloria_y + 200, 50, 300))
    pygame.draw.rect(screen, (0, 0, 0), (gloria_x + 35, gloria_y + 200, 50, 300), 5)

    #windows

    window1_x = gloria_x + 45
    spacing = 10
    number_of_bars = 5
    width1_window = 5
    while window1_x < (width1_window + spacing) * number_of_bars + gloria_x:
        pygame.draw.rect(screen, (0, 0, 0), (window1_x, gloria_y + 210, width1_window, 14))
        pygame.draw.rect(screen, (0, 0, 0), (window1_x, gloria_y + 240, width1_window, 14))
        pygame.draw.rect(screen, (0, 0, 0), (window1_x, gloria_y + 270, width1_window, 14))
        pygame.draw.rect(screen, (0, 0, 0), (window1_x, gloria_y + 300, width1_window, 14))
        pygame.draw.rect(screen, (0, 0, 0), (window1_x, gloria_y + 330, width1_window, 14))
        pygame.draw.rect(screen, (0, 0, 0), (window1_x, gloria_y + 360, width1_window, 14))
        pygame.draw.rect(screen, (0, 0, 0), (window1_x, gloria_y + 390, width1_window, 14))
        pygame.draw.rect(screen, (0, 0, 0), (window1_x, gloria_y + 420, width1_window, 14))
        pygame.draw.rect(screen, (0, 0, 0), (window1_x, gloria_y + 450, width1_window, 14))
        window1_x += spacing

    #meteor crash
    meteor_points = [
        (gloria_x + 72, gloria_y + 217),
        (gloria_x + 112,gloria_y + 211),
        (gloria_x + 85, gloria_y + 208),
        (gloria_x + 105, gloria_y + 190),
        (gloria_x + 83, gloria_y + 199),
        (gloria_x + 68, gloria_y + 185),
        (gloria_x + 72, gloria_y + 201),
        (gloria_x + 53, gloria_y + 203)

    ]
    if circle_y_gloria == gloria_y + 190:
        crash_gloria = True
    if crash_gloria == True:
        pygame.draw.polygon(screen, (255, 140, 0), (meteor_points))

    #----------------------
    #AYDA'S REIGN OF TERROR
    x = 640*4
    y = 480*3
    width = 640
    height = 480
    
    #BACKGROUND
    pygame.draw.rect(screen, (AYDA_SKY), (x, y, width, height))
        
    #LAND
    pygame.draw.ellipse(screen, AYDA_BROWN, (x + width // 4, y + height // 4, 300, 300), width=0)
    
    #SHREKI-WAN KENOBI
    pygame.draw.ellipse(screen, AYDA_GREEN, (x + width//2 - 30, y + height//2-140, 30, 40), width=0)
    xpoint = x + width//2-15
    pygame.draw.line(screen, AYDA_GREEN, (xpoint+15, y + height//2-140), (xpoint, y + height//2-120), width=3)
    pygame.draw.line(screen, AYDA_GREEN, (xpoint-15, y + height//2-140), (xpoint, y + height//2-120), width=3)
    
    #LIGHTSABER
    x1, y1 = x + width // 2 - 20, y + height // 2 - 120
    x2, y2 = x + width // 2 - 45, y + height // 2 - 140
    saber_x2 = x1 + (x2 - x1) / 4
    saber_y2 = y1 + (y2 - y1) / 4
    pygame.draw.line(screen, (AYDA_BLUE), (x1, y1), (x2, y2), width=3) #the laser
    pygame.draw.line(screen, (0, 0, 0), (x1, y1), (saber_x2, saber_y2), width=3) #the handle
    
    #WAVE
    wave_points = []
    for a in range(x, x + width, 5): 
        x_wave = a - x 
        y_wave = height // 2 + ayda_amplitude * math.sin(ayda_frequency * x_wave + ayda_phase)
        wave_points.append((x_wave + x, y_wave + y))
        pygame.draw.rect(screen, AYDA_LAVA, (x_wave + x, y_wave + y, 5, 5))
    
    wave_points.append((x + width, y + height))
    wave_points.append((x, y + height))
    pygame.draw.polygon(screen, AYDA_LAVA, wave_points)
    
    ayda_phase += 0.1
    
    #TEXT
    screen.blit(ayda_text, (x+width//2 - ayda_text.get_width()//2, y+20))

    # -------------------------------------------------------------------------
    x = 0
    y = 960

    # Draw the background
    pygame.draw.rect(screen, (135, 206, 235), (x , y, WIDTH_henry, HEIGHT_henry))

    # Draw the shapes
    pygame.draw.rect(screen, (150, 75, 0), (rect_x_henry + x + x_henry, rect_y_henry + 200 + y - y_henry, 20, 20))
    pygame.draw.circle(screen, (138, 30, 30), (circle_x_henry + x + x_henry, circle_y_henry + 200 + y - y_henry), 30)
    pygame.draw.rect(screen, (0, 0, 0), (rect_x_henry + x + 2 + x_henry, rect_y_henry + 200 + y - 20 - y_henry, 3, 20))
    pygame.draw.rect(screen, (0, 0, 0), (rect_x_henry + x + 15 + x_henry, rect_y_henry + + 200 + y - 20 - y_henry, 3, 20))
    pygame.draw.circle(screen, (255, 234, 0), (circle_x_henry + x - 180, circle_y_henry - 90 + y), 50)
    pygame.draw.rect(screen, (1, 50, 32), (x , y + 400, WIDTH_henry, HEIGHT_henry - 400))

    pygame.draw.rect(screen, (150, 21, 21), (x + rect_x_henry - 10, y + rect_y_henry - 50 + 200, 50, 50))
    pygame.draw.polygon(screen, (84, 8, 8), [(240 + x, 151 + y + 200), (260 + x, 115 + y + 200), (288 + x, 151 + y + 200)])
    pygame.draw.rect(screen, (217, 242, 29), (244 + x, 159 + y + 200, 10, 10))
    pygame.draw.rect(screen, (217, 242, 29), (272 + x, 159 + y + 200, 10, 10))
    pygame.draw.rect(screen, (0, 0, 0), (258 + x, 183 + y + 200, 10, 17))

    y_henry += 4
    x_henry += 3

    if y_henry >= 310:
        y_henry = 0
    if y_henry == 160:
        bomb_henry = True
    if x_henry == 15 or x_henry == 12 or x_henry == 9 or x_henry == 6:
        x_henry-= 6

    if bomb_henry and not bomb_stopped_henry:
        pygame.draw.circle(screen, (0, 0, 0), (bomb_x_henry + x, bomb_y_henry + 190 + y + h_henry), 5)
        h_henry += 10        
    if h_henry >= 160 and not bomb_stopped_henry:
        pygame.draw.circle(screen, (236, 146, 55), (x + 260, y + 400), w_henry)
        w_henry += 4
        bomb_henry = False
        if w_henry >= 100:
            bomb_stopped_henry = True

    if bomb_stopped_henry:
        h_henry = 0
        w_henry = 1
        x_henry = 0
        bomb_stopped_henry = False
    # ---------------------------------------------------------------------------
    x = 640 * 5 
    y = 480 * 1 
    width = 640
    height = 480

    # Points of spaghetti
    pygame.draw.rect(screen, (0, 0, 0), (x, y, width, height))
    points = [(x + 160, y + 325), (x + 449, y + 296)]
    pointsv2 = [(x + 155, y + 315), (x + 450, y + 255)]
    pointsv3 = [(x + 143, y + 303), (x + 420, y + 285)]
    pointsv4 = [(x + 147, y + 270), (x + 450, y + 328)]
    pointsv5 = [(x + 157, y + 260), (x + 450, y + 276)]
    pointsv6 = [(x + 127, y + 287), (x + 460, y + 309)]
    pointsv7 = [(x + 215, y + 273), (x + 375, y + 323)]
    pointsv8 = [(x + 150, y + 50), (x + 450, y + 93)]
    pointsv9 = [(x + 175, y + 54), (x + 435, y + 90)]

#The spaghetti
    pygame.draw.lines(screen, (227,207,87), False, points, 10)
    pygame.draw.lines(screen, (227,207,87), False, pointsv2, 10)
    pygame.draw.lines(screen, (227,207,87), False, pointsv4, 10)
    pygame.draw.lines(screen, (227,207,87), False, pointsv3, 11)
    pygame.draw.lines(screen, (227,207,87), False, pointsv5, 10)
    pygame.draw.lines(screen, (227,207,87), False, pointsv6, 10)
    pygame.draw.lines(screen, (227,207,87), False, pointsv7, 9)
    pygame.draw.lines(screen, (128,138,135), False, pointsv8, 80)
    pygame.draw.lines(screen, (255,255,0), False, pointsv9, 80)


  #The plate and meatballs
    pygame.draw.ellipse(screen, (255,0,0), (x + 240, y + 257, 120, 50))
    pygame.draw.ellipse(screen, (255, 255, 255,), (x + 150, y + 325, 310, 35))
    pygame.draw.ellipse(screen, (131, 139, 139), (x + 165, y + 325, 280, 20))
    pygame.draw.ellipse(screen, (255,0,0), (x + 160, y + 280, 90, 40))
    pygame.draw.ellipse(screen, (255,0,0), (x + 350, y + 280, 90, 40))
    pygame.draw.circle(screen, (128,138,135), (x + 312, y + 87,), 10)
    pygame.draw.circle(screen, (128,138,135), (x + 362, y + 95,), 10)
    pygame.draw.circle(screen, (128,138,135), (x + 252, y + 86,), 9)
    pygame.draw.circle(screen, (128,138,135), (x + 392, y + 95,), 15)
    pygame.draw.circle(screen, (128,138,135), (x + 230, y + 50,), 13)
    pygame.draw.circle(screen, (128,138,135), (x + 296, y + 57,), 18)
    pygame.draw.circle(screen, (128,138,135), (x + 336, y + 70,), 10)
    pygame.draw.circle(screen, (128,138,135), (x + 262, y + 67,), 10) 
    pygame.draw.circle(screen, (128,138,135), (x + 210, y + 57,), 7)
    pygame.draw.circle(screen, (128,138,135), (x + 360, y + 57,), 7)
    pygame.draw.circle(screen, (128,138,135), (x + 399, y + 63,), 14)
    pygame.draw.circle(screen, (128,138,135), (x + 219, y + 85,), 10)
      #More meatballs
    x_meatballs_nicholas = x-3315

    while x_meatballs_nicholas < 138:
      pygame.draw.circle(screen, (138, 54, 15), (x + x_meatballs_nicholas + 277, y + 300 ), 25)
      pygame.draw.circle(screen, (138, 54, 15,), (x +  x_meatballs_nicholas + 326, y + 300 ), 25)
      pygame.draw.circle(screen, (138, 54, 15,), (x +  x_meatballs_nicholas + 301, y + 257 ), 25)
      pygame.draw.circle(screen, (0, 0, 0,), (x +  x_meatballs_nicholas + 320, y + 290 ), 5)
      pygame.draw.circle(screen, (0, 0, 0,), (x +  x_meatballs_nicholas + 280, y + 295 ), 5)
      pygame.draw.circle(screen, (0, 0, 0,), (x +  x_meatballs_nicholas + 269, y + 310 ), 5)
      pygame.draw.circle(screen, (0, 0, 0,), (x +  x_meatballs_nicholas + 340, y + 305 ), 5)
      pygame.draw.circle(screen, (0, 0, 0,), (x +  x_meatballs_nicholas + 290, y + 247 ), 5)
      pygame.draw.circle(screen, (0, 0, 0,), (x +  x_meatballs_nicholas + 312, y + 263 ), 5)
      x_meatballs_nicholas += 24 + 63 + 25

#Cheese curds
    cheese_curds = []

    for i in range(40):
        
        cheese_x = random.randint(155, 449) 
        cheese_y = random.randint(100, 305) 
        cheese_curds.append([cheese_x, cheese_y])

    for curd in cheese_curds:
        curd[1] += 1  
        pygame.draw.circle(screen, (255, 255, 0), (x+curd[0], y+curd[1]), 5) 

        if curd[1] > 325:  
            curd[1] = random.randint(-100, -10)
            curd[0] = random.randint(x + 155, x + 449)
    # ----------------------------------------------------------------------------------------
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
