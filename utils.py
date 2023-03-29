import json
import operator
from json import JSONDecodeError
from typing import Union

from operations import Operations



def get_data_operation(file: str) -> Union[list, bool]:
    """
    получение данных из фаила
    :param file: название фаила
    :return: словарь или фолс
    """
    try:
        with open(file, 'r', encoding='utf-8') as f:
            return json.load(f)
    except (FileNotFoundError, JSONDecodeError):
        return False


def creating_classes_and_sorting(file: str ) -> Union[list[Operations], bool]:
    """
    фильтрация данных по статусу
    и сортировка по дату
    :param file: названия фаила
    :return: список или фолс
    """
    data_file = get_data_operation(file)
    if data_file:
        class_list = []
        for data in data_file:
            operation = Operations(data["id"], data["состояние"], data["дата"], data["ОперацияСумма"], data["description"],
                               data["кому"], data.get("от"))
            if operation.get_execution_check():
                class_list.append(operation)
        sorted_class = sorted(class_list, key=operator.attrgetter('date'), reverse=True)
        return sorted_class
    else:
        return False
