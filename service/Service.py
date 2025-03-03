import numpy as np
from scipy.spatial import ConvexHull


def in_hull(p, hull):
    return np.all(np.dot(hull.equations[:, :-1], p) + hull.equations[:, -1] <= 1e-10)


class Service:
    def __init__(self, repo):
        self.repo = repo
        self.hull = None
        self.calculated_hull = False

    def calculate_hull(self):
        # Get the sample data from repo
        data = self.repo.get_data()

        # Get the points matrix as list of list. Then convert to numpy matrix
        points_matrix = []
        for point in data:
            coords_line = []
            coords_point = point.get_coords()
            for c in coords_point:
                coords_line.append(c)
            points_matrix.append(coords_line)

        # Convert to numpy matrix
        points = np.array(points_matrix)

        self.hull = ConvexHull(points)

    def run_query(self, query):
        # Split query string and construct query point y
        query_data = query.split(" ")
        y = []
        for elem in query_data:
            y.append(int(elem))

        if not self.calculated_hull:
            self.calculate_hull()
            self.calculated_hull = True

        query_point = np.array(y)
        if in_hull(query_point, self.hull):
            return True
        return False
