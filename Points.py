class Point:
    def __init__(self, width, height):
        self.coordinates = dict()
        self.width = width
        self.height = height
        self.center_X = self.width / 2
        self.center_Y = self.height / 2
        self.normal_coordinates = None

    def add_coordinate(self, X: int, Y: int):
        if self.check_need_to_add(X=X):
            self.coordinates.update({X: Y})
            self.to_normal_coordinate()
        else:
            pass

    def check_need_to_add(self, X: int) -> bool:
        if X in self.coordinates.keys():
            return False
        else:
            return True

    def get_coordinates(self):
        # return self.coordinates.
        for i in self.coordinates:
            print(i)
        pass

    def to_normal_coordinate(self):
        self.normal_coordinates = list()
        for x, y in self.coordinates.items():
            _x = x - self.center_X
            _y = self.center_Y - y
            self.normal_coordinates.append((_x, _y))

    def to_screen_coordinate(self, points):
        return points[0] + self.center_X, self.center_Y - points[1]

    def calc(self, x, points):
        sum = 0
        for power, value in enumerate(points):
            sum += pow(x, power) * value
        return sum
