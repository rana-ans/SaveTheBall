import pygame
pygame.init()

win_w = 800
win_h = 560
win = pygame.display.set_mode((win_w, win_h))
pygame.mouse.set_visible(False)                         # Hides Mouse Cursor in Window
bg = pygame.image.load('bg1.jpg')                       # Background
pygame.display.set_caption("Save The Ball - Game")      # Window Name

clock = pygame.time.Clock()

# Writing on Screen
black = (0, 0, 0)
white = (255, 255, 255)
red = (0, 0, 0)
f = pygame.font.SysFont('Courier', 32)

vel = [5, 5]
FPS = 60
score = 0

# Ball Initial Coordinates
bar = pygame.image.load('bar.png')
bar_vel = 5
x = 320
y = 490

# Object Initial Coordinates
obj_x = 20
obj_y = 20
obj = pygame.draw.circle(win, black, [obj_x, obj_y], 10)

isdead = False


def update_score(text, cord):
    font = pygame.font.Font('freesansbold.ttf', 32)
    t = font.render(text, True, white)
    win.blit(t, cord)       # for score (320, 10)
    pass


run = True
while run:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # Display
    win.blit(bg, (0, 0))        # Displaying background in loop so the ball wont leave its track
    win.blit(bar, (x, y))

    # Key Check
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT] and x <= 670:       # Moves the bar left and right
        x += bar_vel
    if keys[pygame.K_LEFT] and x >= 0:
        x -= bar_vel

    # Ball Motion
    obj_x += vel[0]
    obj_y += vel[1]

    # Border Check
    if obj_x + 10 > win_w or obj_x < 0:
        vel[0] = -vel[0]
    if obj_y < 0:   # or obj_y > win_h:       # Collision Detection of Ball with Bar
        vel[1] = -vel[1]

    # Bar Collision Check
    if x < obj_x < x + 130 and 530 < obj_y < 550:
        vel[1] = -vel[1]
        score += 10

    # Check if ball dropped down the screen
    if obj_y > 570:
        update_score('YOU LOSE!', (300, 240))
        update_score('Your Score: ' + str(score), (280, 280))

    pygame.draw.circle(win, black, [obj_x, obj_y], 10)
    update_score('Score: ' + str(score), (320, 10))
    pygame.display.update()

pygame.quit()
