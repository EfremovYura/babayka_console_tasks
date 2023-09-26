import pytest
from modules.taskC import change_list

lists = [
    ([1, 3, 'a', '1'], [1, 9, 'abc_a_cba', 'abc_1_cba']),
    ([2, 3], [4, 9]),
    (['a', '1'], ['abc_a_cba', 'abc_1_cba']),
    ([], []),
]


@pytest.mark.parametrize('src_list, result_list', lists)
def test_change_list(src_list, result_list):
    assert change_list(src_list) == result_list
