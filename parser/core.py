from prompt_toolkit import prompt
from prompt_toolkit.validation import Validator

from parser.parser import get_links
from parser.utils import write_to_file, validate_url


def start():
    print("Поиск ссылок ведущих на другие веб-сайты с глубиной до пяти уровней")
    url = prompt("Введите url-адрес: ", validator=Validator.from_callable(validate_url, error_message="Невалидный url"))
    links_list = get_links(url)

    for _ in range(4):
        repeat_procedure = prompt("Повторить процедуру для полученных ссылок? y/n: ", validator=Validator.from_callable(lambda x: x.lower() in ['y', 'n']))
        match repeat_procedure:
            case "y":
                print("OK")  # дописать 
            case "n":
                break

    information_output = prompt("Ссылки вывести в файл или в терминал? f/t: ", validator=Validator.from_callable(lambda x: x.lower() in ['f', 't']))
    match information_output:
        case "f":
            write_to_file(links_list)
            print("Ссылки записаны в файл links.txt в корне проекта.")
        case "t":
            for link in links_list:
                print(link)
