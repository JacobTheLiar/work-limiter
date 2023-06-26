class Configuration:
    def __init__(self):
        self.WAITING_TIME = 3600
        self.FILE_NAME = "state.txt"
        self.CURRENT_DATE_PARAM = "current_date"
        self.REMAINING_TIME_PARAM = "remaining_time"
        self.WINDOW_POS_X = "window_position_x"
        self.WINDOW_POS_Y = "window_position_y"
        self.TIME_LEFT_PATTERN = "Time left\n{0}:{1:02d}"
        self.WINDOW_TITLE = "Countdown Timer"
        self.POPUP_TITLE = "Sorry!"
        self.POPUP_MESSAGE = "Today's time's up!"
