#
# ps8pr4.py  (Problem Set 8, Problem 4)
#
# Images as 2-D lists  
#
# Computer Science 111
# 

from hmcpng import *

def create_uniform_image(height, width, pixel):
    """ creates and returns a 2-D list of pixels with height rows and
        width columns in which all of the pixels have the RGB values
        given by pixel
        inputs: height and width are non-negative integers
                pixel is a 1-D list of RBG values of the form [R,G,B],
                     where each element is an integer between 0 and 255.
    """
    pixels = []
    
    for r in range(height):
        row = [pixel] * width
        pixels += [row]

    return pixels

def blank_image(height, width):
    """ creates and returns a 2D list of pixels with height rows and width
        columns in which all of the pixels are green"""
    green = [0, 255, 0]
    return create_uniform_image(height, width, green)

def flip_horiz(pixels):
    """ takes 2D list pixels containing pixels for an image and creates/
        returns a new 2D list of pixels for an image in which the
        original image is flipped horizontally """
    height = len(pixels)
    width = len(pixels[0])
    midpoint = width//2
    new_image = blank_image(height, width)
    for r in range(height):
        for c in range(width):
            pos_x_coordinate = c - midpoint
            neg_x_coordinate = midpoint - pos_x_coordinate
            pixel = pixels[r][neg_x_coordinate]
            new_image[r][c] = pixel
        if width % 2 == 0:
            first_column = pixels[r][0]
            new_image[r][width-1] = first_column
    return new_image

def transpose(matrix):
    """ takes n x m matrix and creates and returns a m x n matrix """
    new_grid = blank_image(len(matrix[0]), len(matrix))
    for r in range(len(matrix)):
        for c in range(len(matrix[0])):
            element = matrix[r][c]
            new_grid[c][r] = element
    return new_grid
