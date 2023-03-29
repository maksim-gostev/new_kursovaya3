from constant import FILE_JSON
from utils import creating_classes_and_sorting


def withdrawal_operations(file: str):
    """
    выводит отфильтрованные данные в нужном формате
    :param file: название ваила
    :return: данные или сведения об ошибке
    """
    class_list = creating_classes_and_sorting(file)
    if class_list:
        count = 0
        while count < 5:
            operations_object = class_list[count]
            print(operations_object.get_date(), operations_object.get_translation_description())
            print(f'{operations_object.format_where()} -> {operations_object.form_recipient()}')
            print(f'{operations_object.get_transfer_amount()} {operations_object.get_currency()}')
            print()

            count += 1
    else:
        print('Ошибка на сервере')


if __name__ == '__main__':
    withdrawal_operations(FILE_JSON)
