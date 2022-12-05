from dz4_arrays.common import ABCArray
from dz4_arrays.factor_array import FactorArray
from dz4_arrays.matrix_array import MatrixArray
from dz4_arrays.single_array import SingleArray
from dz4_arrays.vector_array import VectorArray


class TestArrays:
    """Тестируем созданные массивы"""

    @staticmethod
    def run_test_array(array: ABCArray):
        """Тестируем методы массива"""
        assert array.size() == 0

        array.add(1)
        array.add(2)
        array.add(3)
        array.add(4)
        array.add(5)
        array.add(6)
        array.add(7)
        array.add(8)
        array.add(9)
        array.add(10)
        array.add(11)
        array.add(12)
        array.add(13)
        array.add(14)
        array.add(15)
        array.add(16)
        array.add(17)

        assert 5 in array
        assert array.size() == 17

        item = array.remove(0)

        assert item == 1
        assert array.size() == 16

        item = array.remove(7)

        assert item == 9
        assert array.size() == 15

        array.insert(99, 2)

        assert 99 in array
        assert array.size() == 16
        assert 99 == array[2]

        array.insert(66, 0)

        assert 66 in array
        assert array.size() == 17
        assert 66 == array[0]

    @staticmethod
    def matrix_insert(array: ABCArray):
        """Тестируем вставку в конец у матричного массива"""
        array.add(17)
        array.insert(654, array.size() - 1)
        array.insert(655, array.size() - 1)
        array.insert(656, array.size() - 1)
        array.insert(657, array.size() - 1)
        array.insert(658, array.size() - 1)
        array.insert(659, array.size() - 1)
        array.insert(659, array.size() - 1)
        array.insert(659, array.size() - 1)
        array.insert(659, array.size() - 1)
        array.insert(659, array.size() - 1)
        array.insert(659, array.size() - 1)

        assert array.size() == 29

    def test_matrix_array(self):
        """Тестируем матрицу массив"""
        array = MatrixArray()
        self.run_test_array(array=array)
        self.matrix_insert(array=array)

    def test_factor_array(self):
        """Тестируем фактор массив"""
        self.run_test_array(array=FactorArray())

    def test_vector_array(self):
        """Тестируем векторный массив"""
        self.run_test_array(array=VectorArray())

    def test_simple_array(self):
        """Тестируем простой массив"""
        self.run_test_array(array=SingleArray())
