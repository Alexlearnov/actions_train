
1 = self.horizontal + 1, self.vertical + 2
2 = self.horizontal + 1, self.vertical - 2

3 = self.horizontal - 1, self.vertical + 2
4 = self.horizontal - 1, self.vertical - 2

5 = self.horizontal + 2, self.vertical + 1
6 = self.horizontal + 2, self.vertical - 1

7 = self.horizontal - 2, self.vertical + 1
8 = self.horizontal - 2, self.vertical - 1


class Knight:
    def __init__(self, horizontal: str, vertical: int, color: str):
        """
        horizontal — координата коня по горизонтальной оси, представленная латинской буквой от a до h
        vertical — координата коня по вертикальной оси, представленная целым числом от 1 до 8 включительно
        color — цвет коня (black или white)
        """

        self.horizontal = horizontal
        self.vertical = vertical
        self.color = color
        self._possible_moves = [
            (hor_ord, vert_int)
            for _ in range(8)
        ]

    @staticmethod
    def get_char():
        """
        метод, возвращающий символ N
        """

        return "N"

    def can_move(self, horizontal: str, vertical: int):
        if ord("a") <= ord(horizontal) <= ord("h") and 1 <= vertical <= 8:
            if (vertical - 2 == self.vertical or vertical + 2 == self.vertical) and (
                ord(horizontal) - 1 == self.horizontal
                or ord(horizontal) + 1 == self.horizontal
            ):
                return True
            elif (vertical - 1 == self.vertical or vertical + 1 == self.vertical) and (
                ord(horizontal) - 2 == self.horizontal
                or ord(horizontal) + 2 == self.horizontal
            ):
                return True

        return False

    def move_to(self, horizontal: str, vertical: int):
        """
        метод, принимающий в качестве аргументов координаты клетки по горизонтальной и по вертикальной осям
        и заменяющий текущие координаты коня на переданные. Если конь из текущей клетки не может переместиться на клетку
        с указанными координатами, его координаты должны остаться неизменными
        """
        if self.can_move(horizontal, vertical):
            self.horizontal = horizontal
            self.vertical = vertical

    def draw_board(self):
        """
        метод, печатающий шахматное поле, отмечающий на этом поле коня и клетки, на которые может переместиться конь.
        Пустые клетки должны быть отображены символом ., конь — символом N, клетки, на которые может переместиться конь,
        — символом *
        """

        # for i in range(8):
        #     for j in range(8):
        #


print(ord("a") , ord("h"))

knight = Knight("c", 3, "white")

print(knight._possible_moves)
# print(knight.horizontal, knight.vertical)
# print(knight.can_move('e', 5))
# print(knight.can_move('e', 4))
#
# knight.move_to('e', 4)
# print(knight.horizontal, knight.vertical)

# c 3
# False
# True
# e 4
