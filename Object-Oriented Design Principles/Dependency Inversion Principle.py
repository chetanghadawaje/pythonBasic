"""
Abstractions should not depend upon details. Details should depend upon abstractions.
"""
from abc import ABC, abstractmethod


class FrontEnd:
    def __init__(self, data_source):
        self.data_source = data_source

    def display_data(self):
        data = self.data_source.get_data()
        print("Display data:", data)


class DataSource(ABC):
    @abstractmethod
    def get_data(self):
        pass


class Database(DataSource):
    def get_data(self):
        return "Data from the database"


class API(DataSource):
    def get_data(self):
        return "Data from the API"


db_front_end = FrontEnd(Database())
db_front_end.display_data()


api_front_end = FrontEnd(API())
api_front_end.display_data()

# O/P: Display data: Data from the database
# Display data: Data from the API
