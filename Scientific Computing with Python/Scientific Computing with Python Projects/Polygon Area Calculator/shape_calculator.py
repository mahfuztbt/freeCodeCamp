class Rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_area(self):
        area = self.width * self.height
        return area

    def get_perimeter(self):
        perimeter = 2 * self.width + 2 * self.height
        return perimeter

    def get_diagonal(self):
        diagonal = (self.width ** 2 + self.height ** 2) ** .5
        return diagonal

    def get_picture(self):
        if self.width > 50 or self.height > 50:
            row = "Too big for picture."
        else:
            line = self.width * "*"
            x = 0
            row = ""
            while x < self.height:
                row += line + "\n"
                x += 1
        return row

    def get_amount_inside(self, side):
        number_of_times = (self.width * self.height) // (side.width * side.height)
        return number_of_times

    def __str__(self):
        output = f"Rectangle(width={self.width}, height={self.height})"
        return output



class Square(Rectangle):

    def __init__(self, side):
        self.width = side
        self.height = side

    def set_side(self, side):
        self.width = side
        self.height = side

    def __str__(self):
        output = f"Square(side={self.width})"
        return output
