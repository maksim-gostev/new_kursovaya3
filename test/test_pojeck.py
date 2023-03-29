import pytest
import datetime

from operations import Operations
from utils import get_data_operation

from constant import FILE_JSON

valid_keys1 = {'description',
               'id',
               'ОперацияСумма',
               'дата',
               'кому',
               'от',
               'состояние',
               }

valid_keys2 = {'description',
               'id',
               'ОперацияСумма',
               'дата',
               'кому',
               'состояние',
               }


def test_get_data_operation():
    res = get_data_operation(FILE_JSON)
    assert type(res) == list, 'возвращает не список'
    assert type(res[1]) == dict, 'возвращает не словарь'
    for i in range(len(res)):
        assert set(res[i].keys()) == set(valid_keys1) or set(res[i].keys()) == set(
            valid_keys2), 'неверный список ключей'


def get_obj_operation(file: str) -> Operations:
    data = get_data_operation(file=file)[1]
    operations = Operations(**data)
    return operations


class Test_Operations:

    def test_execution_check(self):
        assert get_obj_operation(FILE_JSON).get_execution_check() == True, 'Возвратиллось не True'

    def test_translation_description(self):
        assert get_obj_operation(
            FILE_JSON).get_translation_description() == 'Перевод организации', 'Не совпало описание перевода'

    def test_format_where(self):
        assert get_obj_operation(
            FILE_JSON).format_where() == 'MasterCard 7158 3*** ***6 758', 'Не совпало откуда перевод'

    def test_form_recipient(self):
        assert get_obj_operation(FILE_JSON).form_recipient() == 'Счет **5560', 'Не совпало куда перевод'

    def test_transfer_amount(self):
        assert get_obj_operation(FILE_JSON).get_transfer_amount() == '8221,37', 'Не совпала сумма перевода'

    def test_currency(self):
        assert get_obj_operation(FILE_JSON).get_currency() == 'доллары США', 'Не совпала валюта перевода'

    def test_format_date(self):
        assert get_obj_operation(FILE_JSON).get_date() == datetime.date(2019, 7, 3), 'Не совпала дата'
