from modules.taskE import TextE

text = TextE('aa aa, aa b 123? #Дрова! тот;')


def test_get_word_list():
    assert text._get_word_list() == ['aa', 'aa', 'aa', 'b', '123', 'Дрова', 'тот']


def test_longest_word():
    assert text.longest_word == 'Дрова'


def test_most_common_word():
    assert text.most_common_word == 'aa'


def test_amount_of_special_symbols():
    assert text.amount_of_special_symbols == 5


def test_get_polindroms():
    assert text.get_polindroms() == 'aa,aa,aa,b,тот'
