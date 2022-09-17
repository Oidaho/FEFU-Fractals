import pygame
from Draw.Fractals import Julia, Mandelbrot, Dragon, Sierpinski

# --------------------------------------------------------------------

WHITE = pygame.Color(255, 255, 255)
RED = pygame.Color(255, 0, 0)
BLACK = pygame.Color(0, 0, 0)

# --------------------------------------------------------------------

pygame.init()
pygame.font.init()

# --------------------------------------------------------------------

W = 1920  # weight
H = 1080  # height
FPS = 60  # frames per second

resolution = (W, H)

# --------------------------------------------------------------------

window = pygame.display.set_mode(resolution)
pygame.display.set_caption("Фракталы")

clock = pygame.time.Clock()

# --------------------------------------------------------------------

background = pygame.image.load("Fractals/img/Background.png")
dragon_img = pygame.image.load("Fractals/img/Dragon.png")
dragon_img_pressed = pygame.image.load("Fractals/img/Dragon_pressed.png")
julia_img = pygame.image.load("Fractals/img/Julia.png")
julia_img_pressed = pygame.image.load("Fractals/img/Julia_pressed.png")
mandelbrot_img = pygame.image.load("Fractals/img/Mandelbrot.png")
mandelbrot_img_pressed = pygame.image.load("Fractals/img/Mandelbrot_pressed.png")
sierpinski_img = pygame.image.load("Fractals/img/Sierpinski.png")
sierpinski_img_pressed = pygame.image.load("Fractals/img/Sierpinski_pressed.png")


# --------------------------------------------------------------------


def StartFractal(act):
    if act == 'StartDragon':
        Dragon.StartDragon()
        pygame.display.set_caption("Кривая Дракона")
    if act == 'StartMandelbrot':
        Mandelbrot.StartMandelbrot()
        pygame.display.set_caption("Множество Мандельброта")
    if act == 'StartJulia':
        Julia.StartJulia()
        pygame.display.set_caption("Множество Жюлиа")
    if act == 'StartSierpinski':
        Sierpinski.StartSierpinski()
        pygame.display.set_caption("Треугольник Серпинского")


class Button:
    def __init__(self, width, height, img, img_pressed):
        self.width = width
        self.height = height
        self.img = img
        self.img_pressed = img_pressed

    def draw(self, x, y, action=None):
        mouse_position = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        if x < mouse_position[0] < x + self.width:
            if y < mouse_position[1] < y + self.height:
                window.blit(self.img_pressed, (x, y))

                if click[0] == 1 and action is not None:
                    StartFractal(action)

            else:
                window.blit(self.img, (x, y))
        else:
            window.blit(self.img, (x, y))


# --------------------------------------------------------------------


button_dragon = Button(451, 101, dragon_img, dragon_img_pressed)
button_julia = Button(451, 101, julia_img, julia_img_pressed)
button_mandelbrot = Button(451, 101, mandelbrot_img, mandelbrot_img_pressed)
button_sierpinski = Button(451, 101, sierpinski_img, sierpinski_img_pressed)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                pass

    window.blit(background, (0, 0))

    button_dragon.draw(132, 388, action='StartDragon')

    button_julia.draw(132, 523, action='StartJulia')

    button_mandelbrot.draw(132, 658, action='StartMandelbrot')

    button_sierpinski.draw(132, 793, action='StartSierpinski')

    pygame.display.update()
    clock.tick(FPS)
