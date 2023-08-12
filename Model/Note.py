from datetime import datetime
import Presenter.counter as counter


class Note:
    def __init__(self, id=str(counter.counter()), title="текст", body="текст",
                 date=str(datetime.now().strftime("%d.%m.%Y %H:%M:%S"))):
        self.id = id
        self.title = title
        self.body = body
        self.date = date

    def get_id(self):
        return self.id

    def get_title(self):
        return self.title

    def get_body(self):
        return self.body

    def get_date(self):
        return self.date

    def set_id(self):
        self.id = str(counter.counter())

    def set_title(self):
        self.title = self

    def set_body(self):
        self.body = self

    def set_date(self):
        self.date = str(datetime.now().strftime("%d.%m.%Y %H:%M:%S"))

    def to_string(self):
        return self.id + ';' + self.title + ';' + self.body + ';' + self.date

    def map_note(self):
        return '\nID: ' + self.id + '\n' + 'Название: ' + self.title + '\n' + 'Описание: ' + self.body + '\n' + 'Дата публикации: ' + self.date
