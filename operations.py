import datetime

class Operations:
    def __init__(self, id, состояние, дата, ОперацияСумма, description, кому, от=None):
        self.id = id
        self.operation_amount = ОперацияСумма
        self.date = self._date_output(дата)
        self.to_whom = кому
        self.from_ = от
        self.state = состояние
        self.description = description

    def execution_check(self):
        """
        проверка выполнения
        :return: Bool
        """
        if self.state == 'ВЫПОЛНЕНО':
            return True
        else:
            return False



    def _date_output(self, date):
        date_list = date.split('T')
        date_time_obj = ' '.join(date_list)
        return datetime.datetime.strptime(date_time_obj,  '%Y-%m-%d %H:%M:%S.%f')


    def translation_description(self):
        """
        описание перевода
        :return: str
        """
        return self.description

    def format_where(self):
        """
        откуда
        :return: srt
        """
        if self.from_:
            from_list = self.from_.split(' ')
            star = '*'
            if len(from_list) > 2:
                check = f'{from_list[0]} {from_list[1]}'
                form_number =  f'{from_list[2][:5]}{star * (len(from_list[2]) - 10)}{from_list[2][-4:]}'

            else:
                check = f'{from_list[0]}'
                form_number = f'{from_list[1][:5]}{star * (len(from_list[1]) - 10)}{from_list[1][-4:]}'

            form_list = [form_number[i:i + 4] for i in range(0, len(form_number), 4)]

            result = f'{check} {" ".join(form_list)}'

            return result

        else:
            return "от кого не указано"

    def form_recipient(self):
        """
        куда
        :return:str
        """
        from_list = self.to_whom.split(' ')
        form_recipient = f'**{from_list[1][-4:]}'
        return f'{from_list[0]} {form_recipient}'

    def transfer_amount(self):
        """
        сумма перевода
        :return: str
        """

        return self.operation_amount["сумма"]

    def currency(self):
        """
        валюта
        :return:
        """
        return self.operation_amount["валюта"]["имя"]

    def format_date(self):
        """
        формат даты
        :return: data
        """
        return self.date.date()