import datetime
from tkinter import Tk

from configuration.configuration import Configuration


class StateReader:

    def __init__(self, configuration: Configuration, main_view: Tk):
        self.__configuration = configuration
        self.__main_view = main_view

    def get_remaining_time(self) -> int:
        try:
            with open(self.__configuration.FILE_NAME, "r") as file:
                state = eval(file.read())

            saved_date = state.get(self.__configuration.CURRENT_DATE_PARAM)
            window_x = int(state.get(self.__configuration.WINDOW_POS_X))
            window_y = int(state.get(self.__configuration.WINDOW_POS_Y))
            remaining_time = int(state.get(self.__configuration.REMAINING_TIME_PARAM))

            self.__main_view.geometry(f"+{window_x}+{window_y}")
            return remaining_time if saved_date == datetime.date.today() else self.__configuration.WAITING_TIME

        except(FileNotFoundError, SyntaxError):
            return self.__configuration.WAITING_TIME
