import time
import datetime
import tkinter as tk
import platform
from tkinter import messagebox


class WorkLimiterApplication:
    def __init__(self):
        self.WAITING_TIME = 3600
        self.FILE_NAME = "state.txt"
        self.CURRENT_DATE_PARAM = "current_date"
        self.REMAINING_TIME_PARAM = "remaining_time"
        self.WINDOW_POS_X = "window_position_x"
        self.WINDOW_POS_Y = "window_position_x"
        self.TIME_LEFT_PATTERN = "Time left\n{0}:{1:02d}"
        self.WINDOW_TITLE = "Countdown Timer"
        self.POPUP_TITLE = "Sorry!"
        self.POPUP_MESSAGE = "Today's time's up!"

        self.remaining_time = self.WAITING_TIME
        self.root = tk.Tk()
        self.time_label = None

    def configure_window(self):
        self.time_label = tk.Label(self.root, font=("Arial", 24), fg="#ECECEC", bg="#333333")
        self.time_label.pack(padx=50, pady=50)

        self.root.title(self.WINDOW_TITLE)
        self.root.resizable(False, False)
        self.root.config(bg="#333333")
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        system = platform.system()
        if system == "Windows":
            self.root.attributes("-toolwindow", "1")
        elif system == "Linux":
            self.root.attributes("-type", "dock")

    def on_closing(self):
        pass

    def main(self):
        self.configure_window()
        self.load_state()
        self.update_time()
        self.root.mainloop()

    def load_state(self):
        try:
            with open(self.FILE_NAME, "r") as file:
                state = eval(file.read())
            saved_date = state.get(self.CURRENT_DATE_PARAM)
            if saved_date == datetime.date.today():
                self.remaining_time = state.get(self.REMAINING_TIME_PARAM)
            window_x = int(state.get(self.WINDOW_POS_X))
            window_y = int(state.get(self.WINDOW_POS_Y))
            self.root.geometry(f"+{window_x}+{window_y}")
        except(FileNotFoundError, SyntaxError):
            pass

    def save_state(self):
        state = {
            self.CURRENT_DATE_PARAM: datetime.date.today(),
            self.REMAINING_TIME_PARAM: self.remaining_time,
            self.WINDOW_POS_X: self.root.winfo_x(),
            self.WINDOW_POS_Y: self.root.winfo_y()
        }

        with open(self.FILE_NAME, "w") as file:
            file.write(str(state))

    def update_time(self):
        self.remaining_time -= 1
        if self.remaining_time > 0:
            minutes = self.remaining_time // 60
            seconds = self.remaining_time % 60
            self.time_label.config(text=self.TIME_LEFT_PATTERN.format(minutes, seconds))
        else:
            messagebox.showinfo(self.POPUP_TITLE, self.POPUP_MESSAGE)
            self.root.destroy()

        self.save_state()
        self.root.after(1000, self.update_time)


if __name__ == "__main__":
    limiter_app = WorkLimiterApplication()
    limiter_app.main()
