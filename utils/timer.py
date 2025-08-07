# utils/timer.py

import time

class Timer:
    def __init__(self):
        self.start_time = None
        self.end_time = None

    def start(self):
        self.start_time = time.time()

    def stop(self):
        self.end_time = time.time()

    def elapsed_time(self):
        if self.start_time is None or self.end_time is None:
            return 0
        return self.end_time - self.start_time

def format_time(seconds):
    minutes = seconds // 60
    remaining_seconds = seconds % 60
    return f"{int(minutes):02}:{int(remaining_seconds):02}"
