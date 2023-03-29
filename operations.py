import datetime

class Operations:
    def __init__(self, id, condition, date_, sum_operation, description, to_whom, from_whom=None):
        self.id = id
        self.sum_operation = sum_operation
        self.date = self._date_output(date_)
        self.to_whom = to_whom
        self.from_whom = from_whom
        self.state = condition
        self.description = description

    def get_execution_check(self) -> bool:
        """
        про
        :return: Bool
        """
        if self.state == 'ВЫПОЛНЕНО':
            return True
        else:
            return False



    def _date_output(self, date: str) -> datetime:
        date_list = date.split('T')
        date_time_obj = ' '.join(date_list)
        return datetime.datetime.strptime(date_time_obj,  '%Y-%m-%d %H:%M:%S.%f')


    def get_translation_description(self) -> str:
        """
        описание перевода
        :return: str
        """
        return self.description

    def format_where(self) -> str:
        """
        откуда
        :return: srt
        """
        if self.from_whom:
            from_list = self.from_whom.split(' ')
            num_str = from_list[1]
            formatted_num = num_str[:2] + "*" * 10 + num_str[-4:]

            return f'{from_list[0]}: {" ".join(formatted_num[i:i + 4] for i in range(0, 16, 4))}'

        else:
            return "от кого не указано"

    def form_recipient(self):
        """
        куда
        :return:str
        """
        from_list = self.to_whom.split(' ')
        return f"{from_list[0]}: **{self.to_whom[-4:]}"

    def get_transfer_amount(self):
        """
        сумма перевода
        :return: str
        """

        return self.sum_operation["сумма"]

    def get_currency(self):
        """
        валюта
        :return:
        """
        return self.sum_operation["валюта"]["имя"]

    def get_date(self)-> datetime:
        """
        формат даты
        :return: data
        """
        return self.date.date()