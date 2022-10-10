import sys

import numpy as np
import pygame

from Points import Point

width = 1200
height = 800


def start_screen(pygame, screen):
    screen.fill((255, 255, 255))
    pygame.draw.line(screen, color=(0, 0, 0), start_pos=(width / 2, 0), end_pos=(width / 2, height))
    pygame.draw.line(screen, color=(0, 0, 0), start_pos=(0, height / 2), end_pos=(width, height / 2))


class Line(pygame.sprite.Sprite):
    def __init__(self, pos, x, y):
        pygame.sprite.Sprite.__init__(self)
        if pos == "y":
            self.image = pygame.Surface((3, height))
            self.image.fill((0, 0, 0))
            self.rect = self.image.get_rect()
            self.rect.centerx = x
            self.rect.centery = y
        elif pos == "x":
            self.image = pygame.Surface((width, 3))
            self.image.fill((0, 0, 0))
            self.rect = self.image.get_rect()
            self.rect.centerx = x
            self.rect.centery = y


class Dot(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.surface.Surface((5, 5))
        self.image.fill((0, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y


class Lagrange:
    def __init__(self):
        pass

    def l(self, points, i):
        coeff = np.ones(1)
        for j in range(len(points)):
            if j != i:
                c = [-points[j][0] / (points[i][0] - points[j][0]), 1 / (points[i][0] - points[j][0])]
                coeff = self.multiply(coeff, c)
        # print(coeff)
        return coeff

    def multiply(self, c1, c2):
        coeff = np.zeros(len(c1) + len(c2) - 1)
        for count_i, value_i in enumerate(c1):
            for count_j, value_j in enumerate(c2):
                coeff[count_i + count_j] += value_j * value_i
        return coeff

    def L(self, points):
        Sum = []
        for i in range(len(points)):
            Sum.append(self.l(points, i) * points[i][1])
        res = np.zeros(len((points)))
        for i in range(len(res)):
            for j in range(len(Sum)):
                res[i] += Sum[j][i]
        # print(1)
        return res


def main():
    pygame.init()
    screen = pygame.display.set_mode((width, height))
    # screen.fill((255, 255, 255))
    # pygame.draw.line(screen, color=(0, 0, 0), start_pos=(width / 2, 0), end_pos=(width / 2, height))
    # pygame.draw.line(screen, color=(0, 0, 0), start_pos=(0, height / 2), end_pos=(width, height / 2))
    # start_screen(pygame=pygame, screen=screen)
    pygame.display.flip()
    points = Point(width=width, height=height)
    all_sprites = pygame.sprite.Group()
    line = Line("y", width / 2, height / 2)
    all_sprites.add(line)
    line1 = Line("x", width / 2, height / 2)
    all_sprites.add(line1)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                # pygame.

                all_sprites = pygame.sprite.Group()
                line = Line("y", width / 2, height / 2)
                all_sprites.add(line)
                line1 = Line("x", width / 2, height / 2)
                all_sprites.add(line1)
                points.add_coordinate(event.pos[0], event.pos[1])
                points.to_normal_coordinate()
                lagrange = Lagrange().L(points=points.normal_coordinates)
                # print(lagrange)
                start = int(-width / 2)
                while start < int(width / 2):

                    y = points.calc(start, lagrange)
                    x_, y_ = points.to_screen_coordinate((start, y))
                    # print(x, y)
                    all_sprites.add(Dot(x=x_, y=y_))
                    start += 0.05

        screen.fill((255, 255, 255))
        all_sprites.draw(screen)
        pygame.display.flip()


if __name__ == '__main__':
    main()
