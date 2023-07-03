class Rectangle:
    def __init__(self, width: int, height: int):
        self._width = width
        self._height = height

    def set_width(self, width: int):
        self._width = width

    def set_height(self, height: int):
        self._height = height

    def get_area(self) -> int:
        return self._width * self._height

    def get_perimeter(self) -> int:
        return self._width * 2 + self._height * 2

    def get_diagonal(self) -> float:
        return (self._width ** 2 + self._height ** 2) ** .5

    def get_picture(self) -> str:
        if self._width > 50 or self._height > 50:
            return 'Too big for picture.'

        return '\n'.join(['*' * self._width] * self._height) + '\n'

    def get_amount_inside(self, rect) -> int:
        return int(self._width / rect._width) * int(self._height / rect._height)

    def __str__(self):
        return f'Rectangle(width={self._width}, height={self._height})'


class Square(Rectangle):
    def __init__(self, side: int):
        super().__init__(side, side)

    def set_side(self, side):
        super().set_width(side)
        super().set_height(side)

    def set_width(self, side: int):
        self.set_side(side)

    def set_height(self, side: int):
        self.set_side(side)

    def __str__(self):
        return f'Square(side={self._width})'
