from modules.taskF import TextF

text = TextF('aa aa, aa b 123? #Дрова! тот;')


def test_get_word_list():
    assert text._get_word_list() == ['aa', 'aa', 'aa', 'b', '123', 'Дрова', 'тот']


def test_longest_word(capsys):
    assert text.longest_word == 'Дрова'
    assert "Время выполнения longest_word" in capsys.readouterr().out


def test_most_common_word(capsys):
    assert text.most_common_word == 'aa'
    assert f"Время выполнения most_common_word" in capsys.readouterr().out


def test_amount_of_special_symbols(capsys):
    assert text.amount_of_special_symbols == 5
    assert "Время выполнения amount_of_special_symbols" in capsys.readouterr().out


def test_get_polindroms(capsys):
    assert text.get_polindroms() == 'aa,aa,aa,b,тот'
    assert "Время выполнения get_polindroms" in capsys.readouterr().out
