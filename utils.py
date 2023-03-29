import json
import operator

from operations import Operations



def get_data_operation(file: str) -> dict:
    with open(file, 'r', encoding='utf-8') as f:
        return json.load(f)


def creating_classes_and_sorting(file: str) -> list[Operations]:
    class_list = []
    for data in get_data_operation(file):
        operation = Operations(data["id"], data["состояние"], data["дата"],
                               data["ОперацияСумма"], data["description"],
                               data["кому"],  data.get("от"))
        if operation.get_execution_check():
            class_list.append(operation)
    sorted_class = sorted(class_list, key=operator.attrgetter('date'), reverse=True)
    return sorted_class

