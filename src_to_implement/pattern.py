import copy

import numpy as np
import matplotlib.pyplot as plt


class Checker:
    output = np.zeros(0)

    def __init__(self, resolution: int, tile_size: int):
        if not isinstance(resolution, int):
            raise TypeError("resolution must be set to an int")
        self.resolution = resolution
        if not isinstance(tile_size, int):
            raise TypeError("tile_size must be set to an int")
        self.tile_size = tile_size
        if resolution % (tile_size * 2) == 0:
            self.tile_number = int(resolution / (tile_size * 2))
        else:
            raise TypeError("Your Tile number is incorrect")

    def draw(self):
        checkerarray0X = np.zeros(self.tile_size)
        checkerarray1X = np.ones(self.tile_size)
        checkerarrayX = np.concatenate((checkerarray0X, checkerarray1X))
        checkerarrayX = np.tile(checkerarrayX, (self.tile_size, 1))
        checkerarrayY = np.concatenate((checkerarray1X, checkerarray0X))
        checkerarrayY = np.tile(checkerarrayY, (self.tile_size, 1))
        checkerboard = np.zeros((self.tile_size * 2, self.tile_size * 2))
        checkerboard[0:self.tile_size, :] = checkerarrayX
        checkerboard[self.tile_size:, :] = checkerarrayY
        self.output = np.tile(checkerboard, (self.tile_number, self.tile_number))
        outputcopy = copy.deepcopy(self.output)
        return outputcopy

    def show(self):
        plt.imshow(self.output, cmap='gray')
        plt.show()


class Circle:
    output = np.zeros(0)

    def __init__(self, resolution: int, radius: int, position: tuple):
        if not isinstance(resolution, int):
            raise TypeError("resolution must be set to an int")
        self.resolution = resolution
        if not isinstance(radius, int):
            raise TypeError("radius must be set to an int")
        self.radius = radius
        if not isinstance(position, tuple):
            raise TypeError("position must be set to an Tuple")
        self.position = position

    def draw(self):
        nx = self.resolution
        x = np.arange(nx)
        y = np.arange(nx)
        A = np.meshgrid(x, y)
        A[0] = A[0] - self.position[0]
        A[1] = A[1] - self.position[1]
        B = A[1] * A[1] + A[0] * A[0]
        B = np.less_equal(B, self.radius * self.radius)
        self.output = B
        outputcopy = copy.deepcopy(self.output)
        return outputcopy

    def show(self):
        plt.imshow(self.output, cmap='gray')
        plt.show()


class Spectrum:
    output = np.zeros(0)

    def __init__(self, resolution: int):
        if not isinstance(resolution, int):
            raise TypeError("resolution must be set to an int")
        self.resolution = resolution

    def draw(self):
        red = np.linspace(0, 1, self.resolution)
        green = np.linspace(0, 1, self.resolution)
        blue = np.linspace(1, 0, self.resolution)
        r = np.tile(red, (self.resolution, 1))
        g = np.tile(green, (self.resolution, 1))
        g = np.transpose(g)
        b = np.tile(blue, (self.resolution, 1))
        rgb_image = np.zeros([self.resolution, self.resolution, 3])
        rgb_image[:, :, 0] = r
        rgb_image[:, :, 1] = g
        rgb_image[:, :, 2] = b
        self.output = rgb_image
        outputcopy = copy.deepcopy(self.output)
        return outputcopy

    def show(self):
        plt.imshow(self.output)
        plt.show()
