import pytest
from collections import OrderedDict

from modules.taskB import lists_to_dict

check_lists = [
    ([], [1], OrderedDict([])),
    ([1], [], OrderedDict([(1, None)])),
    ([2, 1], [2], OrderedDict([(1, None), (2, 2)])),
    ([1, 2], ["1", "2"], OrderedDict([(1, "1"), (2, "2")])),
    ([2, 1], [2, 1, 3], OrderedDict([(1, 1), (2, 2)])),
]


@pytest.mark.parametrize('list1, list2, result_dict', check_lists)
def test_lists_to_dict(list1, list2, result_dict):
    assert lists_to_dict(list1, list2) == result_dict
