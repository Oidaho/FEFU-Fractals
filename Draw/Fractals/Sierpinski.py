import random

import pygame

# --------------------------------------------------------------------

WHITE = pygame.Color(255, 255, 255)
RED = pygame.Color(255, 0, 0)
BLACK = pygame.Color(0, 0, 0)
GREY = pygame.Color(30, 30, 30)

# --------------------------------------------------------------------

pygame.init()

# --------------------------------------------------------------------

W = 1920  # weight
H = 1080  # height
FPS = 20000  # frames per second

resolution = (W, H)
resolution_center = (W // 2, H // 2)

# --------------------------------------------------------------------

window = pygame.display.set_mode(resolution)
pygame.display.set_caption("Треугольник Серпинского")

clock = pygame.time.Clock()
ctrls = pygame.image.load("Fractals/img/SKControls.png")
# --------------------------------------------------------------------


def FindMiddlePoint(current, desired):
    xl1, yl1 = current[0], current[1]
    xl2, yl2 = desired[0], desired[1]
    xl3 = (xl1 + xl2) // 2
    yl3 = (yl1 + yl2) // 2
    point = (xl3, yl3)
    return point


def StartSierpinski():
    window.fill(WHITE)

    x1, y1 = random.randint(0, W), random.randint(0, H)
    point1 = (x1, y1)
    x2, y2 = random.randint(0, W), random.randint(0, H)
    point2 = (x2, y2)
    x3, y3 = random.randint(0, W), random.randint(0, H)
    point3 = (x3, y3)

    window.fill(GREY)

    pygame.draw.circle(window, WHITE, point1, 5)
    pygame.draw.circle(window, WHITE, point2, 5)
    pygame.draw.circle(window, WHITE, point3, 5)

    last = point1
    target = (0, 0)
    n = 0
    while True:
        window.blit(ctrls, (W - 200, H - 200))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    window.fill(WHITE)
                    x1, y1 = random.randint(0, W), random.randint(0, H)
                    point1 = (x1, y1)
                    x2, y2 = random.randint(0, W), random.randint(0, H)
                    point2 = (x2, y2)
                    x3, y3 = random.randint(0, W), random.randint(0, H)
                    point3 = (x3, y3)

                    window.fill(GREY)

                    pygame.draw.circle(window, WHITE, point1, 5)
                    pygame.draw.circle(window, WHITE, point2, 5)
                    pygame.draw.circle(window, WHITE, point3, 5)
                    last = point1
                    target = (0, 0)
                    n = 0

        if n < 100:
            dice = random.randint(1, 6)
            if 1 <= dice <= 2:
                target = point1
            if 3 <= dice <= 4:
                target = point2
            if 5 <= dice <= 6:
                target = point3

            pp = FindMiddlePoint(last, target)
            pygame.draw.circle(window, RED, last, 2)
            n += 0.001
            last = pp

        pygame.display.update()
        clock.tick(FPS)
