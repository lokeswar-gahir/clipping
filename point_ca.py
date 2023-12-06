class Point_clipping:
    def __init__(self,min:tuple,max:tuple):
        self.x_min = min[0]
        self.x_max=max[0]
        self.y_min=min[1]
        self.y_max=max[1]
    def window_coordinates(self):
        return f"""
x_min : {self.x_min}
x_max : {self.x_max}
y_max : {self.y_max}
y_min : {self.y_min}
"""
    def check(self, coord):
        if coord is not None:
            if (self.x_min<= coord[0] <= self.x_max) and (self.y_min<= coord[1] <= self.y_max):
                return 1
        return 0
if __name__ == "__main__":
    x,y=tuple(map(int,input("Enter the coordinates: ").split(",")))
    p = Point_clipping(0,0,53,23)
    print(p.window_coordinates())