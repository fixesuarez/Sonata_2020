from threading import Thread

class FadeWorker(Thread):
    def __init__(self, note_listener, delay):
        Thread.__init__(self)
        self.note_listener = note_listener
        self.go = False

    def start(self):
        print("Fade worker Started")
        self.go = True
        while self.go:
            self.note_listener.fade()

    def stop(self):
        self.go = False
