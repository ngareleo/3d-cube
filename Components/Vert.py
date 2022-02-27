class Vert:

    def __init__(self, x, y, z):
        self.original_x = x
        self.original_y = y
        self.original_z = z
        self.c_X = self.original_x
        self.c_Y = self.original_y
        self.c_Z = self.original_z

        assert (self.c_X == self.original_x)
        assert (self.c_Y == self.original_y)
        assert (self.c_Z == self.original_z)

    def __repr__(self):
        return f"{self.c_X}\t{self.c_Y}\t{self.c_Z}"

    def __str__(self):
        return f"{self.c_X}\t{self.c_Y}\t{self.c_Z}"
