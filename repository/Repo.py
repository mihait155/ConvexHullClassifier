import copy

from domain.Point import Point


class Repo:
    def __init__(self):
        self.sample_data = []
        self.load_sample_data()

    def load_sample_data(self):
        # file = open("data/test_data_rectangle.txt", "r")
        file = open("data/sample_data.txt", "r")
        for line in file:
            if line[0] == '#':
                continue
            line = line.split(" ")
            line[len(line) - 1] = line[len(line) - 1].replace("\n", "")
            coords = []
            for elem in line:
                coords.append(int(elem))
            point = Point(coords)
            self.sample_data.append(point)

    def print_points(self):
        for point in self.sample_data:
            print(point)
        return len(self.sample_data)

    def get_data(self):
        return self.sample_data
