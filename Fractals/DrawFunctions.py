import time
import PIL.Image
import pygame

from numba import njit

# --------------------------------

paths = [                                                                               # List of paths to gradients
    'D:\\PyCharm\\Projects\\Fractals\\Draw\\Fractals\\img\\Gradient_Mandelbrot_Colored.png',
    'D:\\PyCharm\\Projects\\Fractals\\Draw\\Fractals\\img\\Gradient_Mandelbrot_Decolorized.png',
    'D:\\PyCharm\\Projects\\Fractals\\Draw\\Fractals\\img\\Gradient_Julia_Colored.png',
    'D:\\PyCharm\\Projects\\Fractals\\Draw\\Fractals\\img\\Gradient_Julia_Decolorized.png'
]

gradient_colored = PIL.Image.open(paths[0])
gradient_decolorized = PIL.Image.open(paths[1])
pixels_mandelbrot = [gradient_colored.load(), gradient_decolorized.load()]  # Loading image pixel data into a list

gradient_colored = PIL.Image.open(paths[2])
gradient_decolorized = PIL.Image.open(paths[3])
pixels_julia = [gradient_colored.load(), gradient_decolorized.load()]  # Loading image pixel data into a list

'''
Two different lists are due to the fact that for the Mandelbrot set and for the Julia set different gradients are used. 
'''

# --------------------------------


@njit
def Mandelbrot(Re, Im, n_iter, scale1, scale2):
    a = Re / scale1
    b = Im / scale2
    c = complex(a, b)
    z = complex(0)
    for n in range(n_iter):
        z = z * z + c
        if abs(z) > 2:
            break
    return n


def DrawMandelbrot(P1, P2, window, scale1, scale2, n_iter, grad):
    tic = time.time()
    for y in range(-P2, P2):
        for x in range(-P1, P1):
            n = Mandelbrot(x, y, n_iter, scale1, scale2)
            choice = pixels_mandelbrot[grad]
            color = choice[n, 0]

            pygame.draw.circle(window, color, (x + P1, y + P2), 1)
    toc = time.time()
    print('used {:.5} sec'.format(toc - tic))


# --------------------------------


@njit
def Julia(Re, Im, n_iter, scale1, scale2, c):
    a = Re / scale1
    b = Im / scale2
    z = complex(a, b)
    for n in range(n_iter):
        z = z * z + c
        if abs(z) > 2:
            break
    return n


def DrawJulia(P1, P2, window, scale1, scale2, n_iter, c, grad):
    tic = time.time()
    for y in range(-P2, P2):
        for x in range(-P1, P1):
            n = Julia(x, y, n_iter, scale1, scale2, c)
            choice = pixels_julia[grad]
            color = choice[n, 0]

            pygame.draw.circle(window, color, (x + P1, y + P2), 1)
    toc = time.time()
    print('used {:.5} sec'.format(toc - tic))
