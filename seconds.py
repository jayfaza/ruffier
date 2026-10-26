from kivy.clock import Clock
from kivy.uix.label import Label

class Timer(Label):
    def __init__(self, max, on_finish=None, **kwargs):
        super().__init__(**kwargs)
        self.current = max
        self._event = None
        self.text = f"{self.current}"
        self.on_finish = on_finish

    def restart(self, total, **kwargs):
        pass

    def start(self):

        self._event = Clock.schedule_interval(self.change, 1)
        pass

    def stop(self):
        if self._event is not None:
            self._event.cancel()
            self._event = None

    def change(self, dt):
        self.current -= 1
        self.text = f"{self.current}"
        if self.current == 0:
            self.stop()
            if self.on_finish:
                self.on_finish()
        pass
