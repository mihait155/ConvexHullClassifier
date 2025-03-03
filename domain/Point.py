import copy
from copy import deepcopy

class Point:
    def __init__(self, coordonates):
        self.coordonates = copy.deepcopy(coordonates)

    def get_coords(self):
        return copy.deepcopy(self.coordonates)

    def __str__(self):
        return f'{self.coordonates}'