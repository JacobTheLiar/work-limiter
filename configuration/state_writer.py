import datetime
from tkinter import Tk

from configuration.configuration import Configuration


class StateWriter:

    def __init__(self, configuration: Configuration, main_view: Tk):
        self.__configuration = configuration
        self.__main_view = main_view

    def save(self, remaining_time: int):
        state = {
            self.__configuration.CURRENT_DATE_PARAM: datetime.date.today(),
            self.__configuration.REMAINING_TIME_PARAM: remaining_time,
            self.__configuration.WINDOW_POS_X: self.__main_view.winfo_x(),
            self.__configuration.WINDOW_POS_Y: self.__main_view.winfo_y()
        }
        with open(self.__configuration.FILE_NAME, "w") as file:
            file.write(str(state))
