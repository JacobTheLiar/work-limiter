from tkinter import messagebox

from configuration.configuration import Configuration
from configuration.state_reader import StateReader
from configuration.state_writer import StateWriter
from view.main_view import MainView


class WorkLimiterApplication:
    def __init__(self):
        self.__configuration = Configuration()
        self.__remaining_time = self.__configuration.WAITING_TIME
        self.__main_view = MainView(self.__configuration)
        self.__state = StateWriter(self.__configuration, self.__main_view)

    def main(self):
        self.__remaining_time = int(StateReader(self.__configuration, self.__main_view).get_remaining_time())
        self.update_time()
        self.__main_view.mainloop()

    def update_time(self):
        self.__remaining_time -= 1
        self.__state.save(self.__remaining_time)
        if self.__remaining_time > 0:
            self.__main_view.update_time(self.__remaining_time)
            self.__main_view.after(1000, self.update_time)
        else:
            messagebox.showinfo(self.__configuration.POPUP_TITLE, self.__configuration.POPUP_MESSAGE)


if __name__ == "__main__":
    limiter_app = WorkLimiterApplication()
    limiter_app.main()
