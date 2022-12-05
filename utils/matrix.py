from typing import List

from utils.exceptions import MultiplyException


class Array:
    """Массив"""

    def __init__(self, array: List) -> None:
        self.size = len(array)
        self._array = {}

        for index, item in enumerate(array):
            self._array[index] = item

    def __call__(self, *args, **kwargs):
        return self._array.values()

    def __str__(self) -> str:
        return '[{}]'.format(', '.join([str(i) for i in self._array.values()]))

    def get_item(self, index: int) -> int:
        """Получение элемента по индексу"""
        return self._array.get(index)

    def to_list(self) -> List:
        """Преобразование в список"""
        return list(self._array.values())

    def multiplication(self, array: 'Array') -> 'Array':
        """Перемножение массивов"""
        return Array(
            [
                self.get_item(i) * array.get_item(i) or 0
                for i in range(self.size)
                if self.get_item(i)
            ]
        )


class Matrix:
    """Матрица"""

    def __init__(self, matrix: List[list | Array]) -> None:
        self.size = len(matrix)
        self._matrix = {}
        self._elem = 0

        for index, array in enumerate(matrix):
            if isinstance(array, Array):
                self._matrix[index] = array
                self._elem += array.size
            else:
                self._matrix[index] = Array(array)
                self._elem += len(array)

        if self._elem % self.size == 0:
            # Одинаковое кол-во элементов shape = (строк, столбцов)
            self.shape = (self.size, int(self._elem / self.size))
        else:
            # Разное кол-во элементов shape = (строк, )
            self.shape = (self.size,)

    def multiplication(self, matrix: 'Matrix') -> 'Matrix':
        """Перемножение матриц"""
        if self.shape[1] != matrix.shape[0]:
            raise MultiplyException(
                'Матрицы не могут быть перемножены, проверьте размерность'
            )
        new_matrix = []
        for x in range(self.shape[0]):
            new_line = []
            for y in range(matrix.shape[1]):

                line = self.get_line(x)
                column = matrix.get_column(y)

                new_line.append(sum(line.multiplication(column).to_list()))
            new_matrix.append(new_line)

        return Matrix(new_matrix)

    def to_list(self) -> List[list]:
        """Преобразовываем в список"""
        return list([array.to_list() for array in self._matrix.values()])

    def get_column(self, index: int) -> Array:
        """Получение колонки по индексу"""
        return Array(
            [array.get_item(index) for array in self._matrix.values()]
        )

    def get_line(self, index: int) -> Array:
        """Получение строки"""
        return self._matrix.get(index)

    def get_item(self, line: int, index: int) -> int:
        """Получение элемента по индексу"""
        return self._matrix.get(line, {}).get_item(index)
