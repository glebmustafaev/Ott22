class Figure:
    sides_count = 0

    def __init__(self, __sides: list,__color: list,filled: bool):
        self.__sides = __sides
        self.__color = __color
        self.filled = filled
        __sides = []
        __color = []
        filled = False
    def get_color(self):

        return self.__color
    def __is_valid_color(self):
        for i in self.__color:
            if i in range(0,225):
                return True
            else: return False
    def set_color(self,r,g,b):
        self.r = r
        self.g = g
        self.b = b
        self.__color = [self.r,self.g,self.b]
    def  __is_valid_sides(self):
        for j in self.__sides:
            if j > 0 and len(self.__sides) == self.sides_count:
                return True
            else: return False
    def get_sides(self):
        return self.__sides
    def __len__(self):
        return sum(self.__sides)
    def set_sides(self, *new_sides):
        if self.__sides != self.sides_count:
