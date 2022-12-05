from pathlib import Path
from typing import List

import pytest

from utils.files import FilesReader


@pytest.fixture
def fibo_payload() -> List[dict[str, str | dict[str, str]]]:
    """Данные для тестирования чисел фибоначчи"""
    get_test_data = FilesReader(
        path=Path(__file__).resolve().parent.joinpath('fibo'),
        count_files=14
    )
    return get_test_data.get_test_data()


@pytest.fixture
def power_payload() -> List[dict[str, str | dict[str, str]]]:
    """Данные для тестирования возведения в степень"""
    get_test_data = FilesReader(
        path=Path(__file__).resolve().parent.joinpath('power'),
        lines={
            1: 'A', 2: 'N'
        },
        count_files=14
    )
    return get_test_data.get_test_data()


@pytest.fixture
def primes_payload() -> List[dict[str, str | dict[str, str]]]:
    """Данные для тестирования поиска простых чисел"""
    get_test_data = FilesReader(
        path=Path(__file__).resolve().parent.joinpath('primes'),
        count_files=15
    )
    return get_test_data.get_test_data()
