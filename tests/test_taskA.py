import pytest

from modules.taskA import ERROR_MESSAGE, get_github_projects_names, check_url, check_name, get_project_name_from_url, \
    convert_url_list

good_urls_to_check = [
    'https://github.com/miguelgrinberg/Flask-SocketIO',
    'https://github.com/miguelgrinberg/Flask-SocketIO.git'
]


@pytest.mark.parametrize('url', good_urls_to_check)
def test_check_url_good(url):
    assert check_url(url) is None


bad_urls_to_check = [None, '', 'asd', 'https://gitlab.com/miguelgrinberg/asd',
                     'https://github.com/miguelgrinberg/Flask SocketIO']


@pytest.mark.parametrize('url', bad_urls_to_check)
def test_check_url_bad(url):
    with pytest.raises(ValueError):
        check_url(url)


good_names = ['asd', 'asd1', 'asd-asd', 'asd.asd', 'asd_asd']


@pytest.mark.parametrize('name', good_names)
def test_check_name_good(name):
    assert check_name(name) is None


bad_names = ['', 'ads#', 'asd asd', 'asd!', 'asd?']


@pytest.mark.parametrize('name', bad_names)
def test_check_name_bad(name):
    with pytest.raises(ValueError):
        check_name(name)


urls_for_get_project_name_from_url = [
    ('https://github.com/miguelgrinberg/Flask-SocketIO', 'Flask-SocketIO'),
    ('https://github.com/miguelgrinberg/Flask-SocketIO.git', 'Flask-SocketIO'),
    ('https://github.com/miguelgrinberg/', None),
    ('https://github.com/', None),
]


@pytest.mark.parametrize('url, name', urls_for_get_project_name_from_url)
def test_get_project_name_from_url(url, name):
    assert get_project_name_from_url(url) == name


url_list_to_convert = [
    ([], [ERROR_MESSAGE]),
    ('', ['']),
    (None, [ERROR_MESSAGE]),
    ([''], ['']),
    (['asd'], ['asd']),
    ("https://gitlab.com/miguelgrinberg/asd", ["https://gitlab.com/miguelgrinberg/asd"]),
    ("https://github.com/miguelgrinberg/Flask-SocketIO, https://github.com/miguelgrinberg/Flask-SocketIO.git",
     ["https://github.com/miguelgrinberg/Flask-SocketIO", "https://github.com/miguelgrinberg/Flask-SocketIO.git"]),
    (["https://github.com/miguelgrinberg/Flask-SocketIO", "https://github.com/miguelgrinberg/Flask-SocketIO.git"],
     ["https://github.com/miguelgrinberg/Flask-SocketIO", "https://github.com/miguelgrinberg/Flask-SocketIO.git"]),
]


@pytest.mark.parametrize('url_list, result_list', url_list_to_convert)
def test_convert_url_list(url_list, result_list):
    assert convert_url_list(url_list) == result_list


urls = [
    ([], [ERROR_MESSAGE]),
    ('', [ERROR_MESSAGE]),
    ([''], [ERROR_MESSAGE]),
    (None, [ERROR_MESSAGE]),
    (['asd'], [ERROR_MESSAGE]),
    ("https://gitlab.com/miguelgrinberg/asd", [ERROR_MESSAGE]),
    ("https://github.com/miguelgrinberg/", [ERROR_MESSAGE]),
    (['asd', "https://github.com/miguelgrinberg/Flask-SocketIO"], [ERROR_MESSAGE, "Flask-SocketIO"]),
    ("https://github.com/miguelgrinberg/Flask SocketIO", [ERROR_MESSAGE]),
    ("https://github.com/miguelgrinberg/Flask-SocketIO&", [ERROR_MESSAGE]),
    ("https://github.com/miguelgrinberg/Flask-SocketIO", ["Flask-SocketIO"]),
    ("https://github.com/miguelgrinberg/Flask-SocketIO.git", ["Flask-SocketIO"]),
    ("https://github.com/miguelgrinberg/Flask-SocketIO, https://github.com/miguelgrinberg/Flask-SocketIO.git",
     ["Flask-SocketIO", "Flask-SocketIO"]),
]


@pytest.mark.parametrize('url_list, names_list', urls)
def test_get_github_projects_names(url_list, names_list):
    assert get_github_projects_names(url_list) == names_list
