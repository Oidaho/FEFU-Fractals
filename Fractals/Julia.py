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


def PrintCurrentConst(screen, const, pos, const_list):
    font = pygame.font.SysFont('Arial', 30)
    text = font.render('{0}  [{1}/{2}]'.format(const, pos + 1, len(const_list)), False, WHITE)
    screen.blit(text, (10, 10))


def DrawGradientMode(screen, x, y, grad):
    font = pygame.font.SysFont('Times New Roman', 30)
    text = font.render('None mode', False, WHITE)
    if grad == 0:
        text = font.render('Colored mode', False, WHITE)
    if grad == 1:
        text = font.render('Decolorized mode', False, WHITE)
    screen.blit(text, (x, y))


# --------------------------------------------------------------------

def StartJulia():
    constant = [
        complex(0, 0),
        complex(-1, 0),
        complex(-0.74543, 0.11301),
        complex(0.28, 0.0113),
        complex(-0.549653, 0.003),
        complex(-0.2, 0.75),
        complex(-0.1244, 0.756),
        complex(-0.1194, 0.6289),
        complex(-0.7382, 0.0827),
        complex(0.377, -0.248),
        complex(0.7382, -0.0827),
        complex(0.77282, 0.0812427)
    ]

    P1 = resolution_center[0]  # complex fild [2*P1+1 x 2*P2+1]
    P2 = resolution_center[1]
    coefficient = 2
    scale1 = P1 / coefficient  # scale coefficient
    scale2 = P1 / coefficient
    n_iter = 100  # number of iterations
    a = 0
    grad = 0
    c = constant[a]  # current constant
    # --------------------------------------------------------------------

    DrawFunctions.DrawJulia(P1, P2, window, scale1, scale2, n_iter, c, grad)

    while True:
        PrintCurrentConst(window, c, a, constant)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    if a - 1 != -1:
                        a -= 1
                        c = constant[a]
                        DrawFunctions.DrawJulia(P1, P2, window, scale1, scale2, n_iter, c, grad)

                if event.key == pygame.K_RIGHT:
                    if a + 1 != len(constant):
                        a += 1
                        c = constant[a]
                        DrawFunctions.DrawJulia(P1, P2, window, scale1, scale2, n_iter, c, grad)

                if event.key == pygame.K_1:
                    grad = 0
                    DrawFunctions.DrawJulia(P1, P2, window, scale1, scale2, n_iter, c, grad)

                if event.key == pygame.K_2:
                    grad = 1
                    DrawFunctions.DrawJulia(P1, P2, window, scale1, scale2, n_iter, c, grad)

        DrawCoordinateLines(window, resolution)
        DrawGradientMode(window, 10, 45, grad)

        pygame.display.update()
        clock.tick(FPS)

