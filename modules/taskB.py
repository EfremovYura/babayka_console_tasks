from itertools import zip_longest
from collections import OrderedDict


def lists_to_dict(list1: list, list2: list) -> OrderedDict:
    """
    Функция принимает два списка и возвращает словарь (ключ из первого списка, значение из второго),
    упорядоченный по ключам. Длина первого списка не должна быть равна длине второго.
    """
    zip_func = zip_longest if len(list1) > len(list2) else zip

    ordered_list = sorted([(key, value) for key, value in zip_func(list1, list2)], key=lambda x: x[0])

    return OrderedDict((key, value) for key, value in ordered_list)
