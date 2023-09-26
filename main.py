from modules.taskA import get_github_projects_names
from modules.taskB import lists_to_dict
from modules.taskC import change_list
from modules.taskD import run_async_http_get
from modules.taskE import TextE

from data.dataA import GOOD_URL1, GOOD_URL2
from data.dataB import LIST1, LIST2
from data.dataC import LIST_C
from data.dataE import STRING_E
from modules.taskF import TextF

if __name__ == '__main__':
    print('\ntask A')
    print(GOOD_URL1, GOOD_URL2)
    print(get_github_projects_names([GOOD_URL1, GOOD_URL2]))

    print('\ntask B')
    print(LIST1, LIST2)
    print(lists_to_dict(LIST1, LIST2))

    print('\ntask C')
    print(LIST_C)
    print(change_list(LIST_C))

    print('\ntask D')
    run_async_http_get()

    print('\ntask E')
    print(STRING_E[:50], '...', '\n')
    text = TextE(STRING_E)
    print("longest_word:", text.longest_word)
    print("most_common_word:", text.most_common_word)
    print("amount_of_special_symbols:", text.amount_of_special_symbols)
    print("polindroms:", text.get_polindroms())

    print('\ntask F')
    print(STRING_E[:50], '...', '\n')
    text_f = TextF(STRING_E)
    print("longest_word:", text_f.longest_word)
    print("most_common_word:", text_f.most_common_word)
    print("amount_of_special_symbols:", text_f.amount_of_special_symbols)
    print("polindroms:", text_f.get_polindroms())

