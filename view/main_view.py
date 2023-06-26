import platform
import tkinter

from configuration.configuration import Configuration


class MainView(tkinter.Tk):

    def __init__(self, configuration: Configuration) -> None:
        super().__init__()
        self.__time_label = None
        self.__configuration = configuration
        self.configure_window()

    def configure_window(self):
        self.__time_label = tkinter.Label(self, font=("Arial", 24), fg="#ECECEC", bg="#333333")
        self.__time_label.pack(padx=50, pady=50)

        self.title(self.__configuration.WINDOW_TITLE)
        self.resizable(False, False)
        self.config(bg="#333333")
        self.protocol("WM_DELETE_WINDOW", self.on_closing)
        system = platform.system()
        if system == "Windows":
            self.attributes("-toolwindow", "1")
        elif system == "Linux":
            self.attributes("-type", "dialog")

    def on_closing(self):
        pass

    def update_time(self, remaining_time: int):
        print(f"remaining_time: {remaining_time}")
        if remaining_time > 0:
            minutes = remaining_time // 60
            seconds = remaining_time % 60
            self.__time_label.config(text=self.__configuration.TIME_LEFT_PATTERN.format(minutes, seconds))
