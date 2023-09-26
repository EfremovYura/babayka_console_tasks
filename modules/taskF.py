"""
Написать декоратор к предыдущему классу, который будет выводить в консоль время выполнения каждого метода.
Результат выполнения задания должен быть оформлен в виде файла с кодом.
"""
from time import time
import re
import string
from collections import Counter
from functools import wraps


def timeit(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time()
        result = func(*args, **kwargs)
        stop = time()
        print(f"Время выполнения {func.__name__}: {stop - start} сек.")
        return result

    return wrapper


class TextF:
    def __init__(self, text: str) -> None:
        self.text = text

    def _get_word_list(self) -> list[str]:
        """Возвращает список слов."""
        return re.sub(r'[^\w\s]', '', self.text).split()

    @property
    @timeit
    def longest_word(self) -> str:
        """Возвращает последнее самое длинное слово в тексте."""
        return sorted(self._get_word_list(), key=lambda x: len(x))[-1]

    @property
    @timeit
    def most_common_word(self) -> str:
        """Возвращает самое часто встречающееся слово."""
        return Counter(self._get_word_list()).most_common(1)[0][0]

    @property
    @timeit
    def amount_of_special_symbols(self) -> int:
        """Возвращает количество спецсимволов в тексте (точки, запятые и так далее)."""
        return len([symbol for symbol in self.text if symbol in string.punctuation])

    @timeit
    def get_polindroms(self) -> str:
        """Возвращает все слова палиндромы через запятую."""
        return ','.join([word for word in self._get_word_list() if word == word[::-1]])
