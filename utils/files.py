import os
from pathlib import Path
from typing import List


def get_test_data_from_folder(
    path: Path, count_data: int
) -> List[dict[str, int]]:
    """Получаем данные для тестирования"""
    data = []

    for i in range(count_data):
        test_data = {}

        if os.path.isfile(path / f'test.{i}.in'):
            with open(path / f'test.{i}.in') as f:
                test_data.update({'in': int(f.readline().strip())})

        if os.path.isfile(path / f'test.{i}.out'):
            with open(path / f'test.{i}.out') as f:
                test_data.update({'out': int(f.readline().strip())})

        data.append(test_data)

    return data
