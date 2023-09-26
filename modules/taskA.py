from copy import deepcopy
from typing import Any

import validators

ERROR_MESSAGE = 'url not correct'


def check_url(url: str) -> None | Exception:
    """ Проверка валидности url github.com."""
    if not validators.url(url):
        raise ValueError

    if not url.startswith('https://github.com/'):
        raise ValueError


def check_name(name: str) -> None | Exception:
    """ Имя репозитория может содержать ASCII буквы, цифры и символы ., -, и _."""
    if not name:
        raise ValueError

    if not all([(letter.isalnum() or letter in '.-_') for letter in name]):
        raise ValueError


def get_project_name_from_url(url: str) -> str | None:
    """ Получает имя проекта из url. """
    try:
        check_url(url)

        name = url.split('/')[4].rstrip('.git')

        check_name(name)
    except (IndexError, ValueError):
        name = None

    return name


def convert_url_list(url_list: list[str] | str | Any) -> list[str]:
    """Преобразует данные в список."""
    url_list = deepcopy(url_list)

    if isinstance(url_list, str):
        url_list = url_list.split(', ')

    if not isinstance(url_list, list):
        try:
            url_list = list(url_list)
        except TypeError:
            url_list = [ERROR_MESSAGE]

    if not url_list:
        url_list = [ERROR_MESSAGE]

    return url_list


def get_github_projects_names(url_list: list[str] | str) -> list[str]:
    """
    Функция принимает в качестве аргумента набор ссылок.
    Ссылки имеют формат ссылок на проекты на гитхабе
    (например: https://github.com/miguelgrinberg/Flask-SocketIO, https://github.com/miguelgrinberg/Flask-SocketIO.git).
    Функция должна обработать полученные ссылки и вывести в консоль названия самих гит-проектов.
    Стоит рассмотреть защиту от ссылок "вне формата".
    """

    url_list = convert_url_list(url_list)

    return [(get_project_name_from_url(url) or ERROR_MESSAGE) for url in url_list]
