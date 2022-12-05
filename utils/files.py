import os
from pathlib import Path
from typing import List

import xlsxwriter


class FilesReader:
    """Для чтения тестовых данных из файлов"""

    _file_in = 'test.{}.in'
    _file_out = 'test.{}.out'

    def __init__(
        self,
        path: Path,
        lines: dict | None = None,
        count_files: int = 1
    ) -> None:
        """Инициализируем считыватель.

        :param path: путь к папке с файлами.
        :param count_files: Сколько файлов обработать.
        :param lines: Сколько строк считать и под какими именами вернуть.
        """
        self._path = path
        self._count_files = count_files
        if lines is None:
            self._lines = {1: 'N'}
        else:
            self._lines = lines

    def get_test_data(self) -> List[dict[str, str | dict[str, str]]]:
        """Читаем данные с файлов."""

        data = []

        for i in range(self._count_files):
            path_file_in = self._path / self._file_in.format(i)
            path_file_out = self._path / self._file_out.format(i)
            if (
                os.path.isfile(path_file_in) and
                os.path.isfile(path_file_out)
            ):
                test_data: dict = {
                    'in': {}, 'out': None
                }
                with open(path_file_in) as file:
                    for line in self._lines.keys():
                        test_data['in'].update(
                            {
                                self._lines[line]: file.readline().strip()
                            }
                        )

                with open(path_file_out) as file:
                    test_data['out'] = file.readline().strip()

                data.append(test_data)
        return data
