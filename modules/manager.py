from PySide6.QtWidgets import QMainWindow


class WindowManager:
    def __init__(self):
        self.windows = []

    def open_window(self, window):
        self.windows.append(window)
        if len(self.windows) > 1:
            self.windows[-2].hide()
        self.windows[-1].show()

    def close_window(self):
        if len(self.windows) > 1:
            self.windows[-2].show()
        self.windows[-1].close()
        self.windows.pop()