# -*- coding: utf-8 -*-
"""
Created on Sat Apr 27 16:34:42 2019

@author: ucapfas
"""

from numpy import *
import matplotlib.pyplot as plt
import matplotlib.image as im
from argparse import ArgumentParser as AP


# =============================================================================
# cx = 0.7
# cy = 0.27015
# x_dim = 800
# y_dim = 600
# 
# x_scaling = 1.5/(0.5*1*x_dim)
# y_scaling = 1.0/(0.5*1*y_dim)
# 
# panel = zeros([y_dim,x_dim])
# =============================================================================

# =============================================================================
# from argparse import ArgumentParser
# if __name__ == "__main__":
#     parser = ArgumentParser(description = "Generate appropriate greetings")
#     parser.add_argument('--title', '-t')
#     parser.add_argument('--polite','-p', action="store_true")
#     parser.add_argument('personal')
#     parser.add_argument('family')
#     arguments= parser.parse_args()
#     
#     greeting= "How do you do, " if arguments.polite else "Hey, "
#     if arguments.title:
#         greeting+=arguments.title+" "
#     greeting+= arguments.personal + " " + arguments.family +"."
#     print(greeting)
# 
# =============================================================================



    









def scaled_norm(zx,zy):
    norm = zx*zx + zy*zy
    return norm

def scaled_diff(zx,zy):
    diff = zx*zx - zy*zy
    return diff


def zx_generator(x,x_dim):
    central_x = x - x_dim/2
    x_scaling = 1.5/(0.5*1*x_dim)
    zx = x_scaling*central_x
    return zx

def zy_generator(y,y_dim):
    central_y = y - y_dim/2
    y_scaling = 1.0/(0.5*1*y_dim)
    zy = y_scaling*central_y
    return zy
    
def pixel_modifier(x_dim, y_dim, panel, cx, cy):
      
    for x in range(x_dim):
        for y in range(y_dim):
            
            zx = zx_generator(x,x_dim)
            zy = zy_generator(y,y_dim)
            
            pixel = 255
            
            while scaled_norm(zx,zy)<4 and pixel>1:
                zx_temp = scaled_diff(zx,zy) - cx
                zy = 2*zx*zy + cy
                zx = zx_temp
                pixel = pixel - 1
                panel[y][x] = pixel
                
#    plt.imshow(panel)
    im.imsave('Julia.png',panel)
#    plt.show()
    
    
def process():
    parser = AP(description = "Refactoring of Julia code")
    parser.add_argument('cx',default = 0.7)
    parser.add_argument('cy',default = 0.27015)
    parser.add_argument('x_dim',default = 800)
    parser.add_argument('y_dim',default = 600)
    
    arguments = parser.parse_args()
    
    cx = float(arguments.cx)
    cy = float(arguments.cy)
    x_dim = int(arguments.x_dim)
    y_dim = int(arguments.y_dim)
    
    
    

    panel = zeros([y_dim,x_dim])
    
    pixel_modifier(x_dim,y_dim,panel,cx,cy)

       


if __name__ == "__main__":
    process()