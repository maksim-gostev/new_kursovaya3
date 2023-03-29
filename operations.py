import datetime




class Operations:
    def __init__(self, pk, condition, date_, sum_operation, description, to_whom, from_whom=None):
        self._id = pk
        self._sum_operation = sum_operation
        self.date = self._date_output(date_)
        self._to_whom = to_whom
        self._from_whom = from_whom
        self._state = condition
        self._description = description

    def _date_output(self, date: str) -> datetime:
        """
        форматирование даты
        :param date: страка
        :return: дата
        """
        date_list = date.split('T')
        date_time_obj = ' '.join(date_list)
        return datetime.datetime.strptime(date_time_obj, '%Y-%m-%d %H:%M:%S.%f')



    def get_execution_check(self) -> bool:
        """
        Проверка статуса выполнения операции
        :return: Bool
        """
        if self._state == 'ВЫПОЛНЕНО':
            return True
        else:
            return False

    def get_translation_description(self) -> str:
        """
        описание перевода
        :return: str
        """
        return self._description

    def format_where(self) -> str:
        """
        форматирование от куда перевод
        :return: srt
        """
        if self._from_whom:
            from_list = self._from_whom.split(' ')
            num_str = from_list[1]
            formatted_num = num_str[:2] + "*" * 10 + num_str[-4:]

            return f'{from_list[0]}: {" ".join(formatted_num[i:i + 4] for i in range(0, 16, 4))}'

        else:
            return "от кого не указано"

    def form_recipient(self) -> str:
        """
        форматирования куда перевод
        :return:str
        """
        from_list = self._to_whom.split(' ')
        return f"{from_list[0]}: **{self._to_whom[-4:]}"

    def get_transfer_amount(self) -> str:
        """
        сумма перевода
        :return: str
        """

        return self._sum_operation["сумма"]

    def get_currency(self) -> str:
        """
        валюта
        :return:
        """
        return self._sum_operation["валюта"]["имя"]

    def get_date(self) -> datetime:
        """
        формат даты
        :return: data
        """
        return self.date.date()
