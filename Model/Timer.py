import threading
import time



class Timer:

    def __init__(self):
        self.seconds = 0
        self.minutes = 0

    def time(self):
        string = "00:00"
        if self.seconds > 59:
            seconds = 0
            self.minutes += 1
            if self.minutes < 10:
                string = str(self.minutes) + ":0" + str(self.seconds)
            else:
                string = "0" + str(self.minutes) + ":0" + str(self.seconds)
        else:
            if self.seconds < 10:
                if self.minutes < 10:
                    string = "0" + str(self.minutes) + ":0" + str(self.seconds)
                else:
                    string = str(self.minutes) + ":0" + str(self.seconds)
            else:
                if self.minutes < 10:
                    string = "0" + str(self.minutes) + ":" + str(self.seconds)
                else:
                    string = str(self.minutes) + ":0" + str(self.seconds)
        return string



    def start(self):
        while True:
            self.seconds += 1
            time.sleep(1)

