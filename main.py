import operator

from operations import Operations
from constant import FILE_JSON
from utils import get_data_operation


def creating_classes_and_sorting(file):
    class_list = []
    for data in get_data_operation(file):
        operation = Operations(**data)
        if operation.execution_check():
            class_list.append(operation)
    sorted_class = sorted(class_list, key=operator.attrgetter('date'), reverse=True)
    return sorted_class


def withdrawal_operations(file):
    class_list = creating_classes_and_sorting(file)
    count = 0
    while count < 5:
        operations_object = class_list[count]
        print(operations_object.format_date(), operations_object.translation_description())
        print(f'{operations_object.format_where()} -> {operations_object.form_recipient()}')
        print(f'{operations_object.transfer_amount()} {operations_object.currency()}')
        print()

        count += 1


if __name__ == '__main__':
    withdrawal_operations(FILE_JSON)
