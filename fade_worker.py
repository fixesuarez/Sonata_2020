import time
from threading import Thread

class FadeWorker(Thread):
    def __init__(self, note_listener, delay):
        Thread.__init__(self)
        self.note_listener = note_listener
        self.delay = delay
        self.go = False

    def run(self):
        print("Fade worker Started")
        self.go = True
        while self.go:
            self.note_listener.fade()
            time.sleep(self.delay / 1000.)

    def stop(self):
        self.go = False
