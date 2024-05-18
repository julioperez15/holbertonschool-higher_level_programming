#!/usr/bin/python3
class Square:
    """Represents a square."""
    def __init__(self, size=0, position=(0, 0)):
        """Initializes the square with a size and position."""
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """Gets the size of the square."""
        return self.__size

        @size.setter
        def size(self, value):
            """Sets the size of the square."""
            if not isinstance(value, int):
                raise TypeError("size must be an integer")
            if value < 0:
                raise ValueError("size must be >= 0")
            self.__size = value

    @property
    def position(self):
        """Gets the position of the square."""
        return self.__position

    @position.setter
    def position(self, value):
        """Sets the position of the square."""
        if not (isinstance(value, tuple) and len(value) == 2
                and all(isinstance(i, int) and i >= 0 for i in value)):
            self.__position = value
        else:
            raise TypeError(
                "position must be a tuple of 2 non-negative integers"
                )

    def area(self):
        """Returns the area of the square."""
        return self.__size ** 2

    def my_print(self):
        """Prints the square with the character #
        at the position specified by the position attribute."""
        if self.__size == 0:
            print()
        else:
            print("\n" * self.position[1], end="")
            for _ in range(self.__size):
                print("_" * self.position[0] + "#" * self.__size)
my_square_1 = Square(3)
my_square_1.my_print()

print("--")

my_square_2 = Square(3, (1, 1))
my_square_2.my_print()

print("--")

my_square_3 = Square(3, (3, 0))
my_square_3.my_print()

print("--")
