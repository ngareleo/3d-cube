class Vertex:

    def __init__(self, x, y, z):
        self.original_x = x
        self.original_y = y
        self.original_z = z
        self.coordinate_x = self.original_x
        self.coordinate_y = self.original_y
        self.coordinate_z = self.original_z

        assert (self.coordinate_x == self.original_x)
        assert (self.coordinate_y == self.original_y)
        assert (self.coordinate_z == self.original_z)

    def __repr__(self):
        return f"{self.coordinate_x}\t{self.coordinate_y}\t{self.coordinate_z}"

    def __str__(self):
        return f"{self.coordinate_x}\t{self.coordinate_y}\t{self.coordinate_z}"
