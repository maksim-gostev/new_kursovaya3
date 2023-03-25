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


class Test_Operations:

    def test_execution_check(self):
        data = get_data_operation(FILE_JSON)[1]
        operations = Operations(**data)
        assert operations.execution_check() == True

    def test_translation_description(self):
        data = get_data_operation(FILE_JSON)[1]
        operations = Operations(**data)
        assert operations.translation_description() == 'Перевод организации'

    def test_format_where(self):
        data = get_data_operation(FILE_JSON)[1]
        operations = Operations(**data)
        assert operations.format_where() == 'MasterCard 7158 3*** ***6 758'

    def test_form_recipient(self):
        data = get_data_operation(FILE_JSON)[1]
        operations = Operations(**data)
        assert operations.form_recipient() == 'Счет **5560'

    def test_transfer_amount(self):
        data = get_data_operation(FILE_JSON)[1]
        operations = Operations(**data)
        assert operations.transfer_amount() == '8221,37'

    def test_currency(self):
        data = get_data_operation(FILE_JSON)[1]
        operations = Operations(**data)
        assert operations.currency() == 'доллары США'

    def test_format_date(self):
        data = get_data_operation(FILE_JSON)[1]
        operations = Operations(**data)
        assert operations.format_date() == datetime.date(2019, 7, 3)
