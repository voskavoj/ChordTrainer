from sequence import Sequence
import time


class Metronome:
    def __init__(self, ui):
        self.ui = ui
        pass

    def show_sequence(self, current_seq: Sequence, next_seq: Sequence):
        print(current_seq)
        time.sleep(0.25)

