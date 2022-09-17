import pygame
from Draw.Fractals import DrawFunctions

# --------------------------------------------------------------------

pygame.init()
pygame.font.init()

# --------------------------------------------------------------------

WHITE = pygame.Color(255, 255, 255)
RED = pygame.Color(255, 0, 0)
BLACK = pygame.Color(0, 0, 0)

# --------------------------------------------------------------------

W = 1920  # weight
H = 1080  # height
FPS = 10  # frames per second

resolution = (W, H)
resolution_center = (W // 2, H // 2)

# --------------------------------------------------------------------

window = pygame.display.set_mode(resolution)
pygame.display.set_caption("Множество Мандельброта")

clock = pygame.time.Clock()

ctrls = pygame.image.load("Fractals/img/MBControls.png")

# --------------------------------------------------------------------


def DrawCoordinateLines(screen, screen_resolution):
    x1, x2 = 0, screen_resolution[0]
    y1, y2 = screen_resolution[1] // 2, screen_resolution[1] // 2
    pygame.draw.line(screen, WHITE, (x1, y1), (x2, y2), 1)
    x1, x2 = screen_resolution[0] // 2, screen_resolution[0] // 2
    y1, y2 = 0, screen_resolution[1]
    pygame.draw.line(screen, WHITE, (x1, y1), (x2, y2), 1)
    x1, x2 = screen_resolution[0] // 2 - 70, screen_resolution[0] - 70
    y1, y2 = 0, screen_resolution[1] // 2
    font = pygame.font.SysFont('Times New Roman', 30)
    text1 = font.render('Im[c]', False, WHITE)
    text2 = font.render('Re[c]', False, WHITE)
    screen.blit(text1, (x1, y1))
    screen.blit(text2, (x2, y2))


def DrawGradientMode(screen, x, y, grad):
    font = pygame.font.SysFont('Times New Roman', 30)
    text = font.render('None mode', False, WHITE)
    if grad == 0:
        text = font.render('Colored mode', False, WHITE)
    if grad == 1:
        text = font.render('Decolorized mode', False, WHITE)
    screen.blit(text, (x, y))


# --------------------------------------------------------------------


def StartMandelbrot():
    P1 = resolution_center[0]  # размер [2*P1+1 x 2*P2+1]
    P2 = resolution_center[1]
    cof = 2
    scale1 = P1 / cof  # масштабный коэффициент
    scale2 = P1 / cof
    n_iter = 100  # число итераций для проверки принадлежности к множеству Мандельброта
    grad = 0
    DrawFunctions.DrawMandelbrot(P1, P2, window, scale1, scale2, n_iter, grad)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    exit()

                if event.key == pygame.K_1:
                    grad = 0
                    DrawFunctions.DrawMandelbrot(P1, P2, window, scale1, scale2, n_iter, grad)

                if event.key == pygame.K_2:
                    grad = 1
                    DrawFunctions.DrawMandelbrot(P1, P2, window, scale1, scale2, n_iter, grad)

        DrawCoordinateLines(window, resolution)
        DrawGradientMode(window, 10, 10, grad)

        pygame.display.update()
        clock.tick(FPS)


