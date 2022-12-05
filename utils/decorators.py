import abc
import time
from functools import wraps
from pathlib import Path

import pandas as pd
from pandas.errors import EmptyDataError


class AbcDecorator(abc.ABC):
    """Замеряем выполнение функции и пишем в файл"""

    def __init__(
        self,
        folder: str = '',
        line_excel: int = 0
    ) -> None:
        """

        :param folder: Имя папки куда загрузить файл с данными
        :param line_excel: Линия записи в файл excel
        """
        self.folder = folder
        self.line_excel = line_excel

    def __call__(self, func, *args, **kwargs):
        @wraps(func)
        def inner_func(*args, **kwargs):
            start_time = time.perf_counter()
            result = func(*args, **kwargs)
            end_time = time.perf_counter()
            total_time = end_time - start_time
            if 'n' in kwargs:
                print(
                    f'Func {func.__name__} | time - {total_time:.10f} sec'
                )
                self.writer(
                    func_name=func.__name__,
                    total_time=f'{total_time:.10f} sec',
                    doc=func.__doc__.replace('\n', '').strip(),
                    n=kwargs.get('n'),
                    a=kwargs.get('a'),
                )
            return result

        return inner_func

    def writer(self, func_name, total_time, doc, n, a):
        """Метод для записи данных

        :param func_name: Название функции
        :param total_time: Время выполнения
        :param doc: Описание функции
        :param n: N
        :return:
        """
        raise NotImplemented


class CSVOutput(AbcDecorator):

    name = 'tests/result_table.csv'
    sep = '|'

    def writer(self, func_name, total_time, doc, n, a):
        path = Path(__file__).resolve().parent.parent / self.folder / self.name

        if not path.exists():
            open(path, 'a').close()

        df = pd.DataFrame(
            {
                'func_name': [func_name],
                'N': n,
                'A': a,
                'time': [total_time]
            },
        )
        df = df.set_index('func_name')

        try:
            df_file = pd.read_csv(path, sep=self.sep)
            df_file = df_file.set_index('func_name')
            df = df_file.append(df)
        except EmptyDataError:
            pass

        df.to_csv(path, sep=self.sep)
