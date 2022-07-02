from sequence import Sequence


class ChordTrainerGenerator:
    def __init__(self):
        pass

    def get_starting_sequence(self):
        strum = {"1": False}
        return Sequence(chord="A", octave=4, barre=False, signature=(4, 4), tempo=100, strum=strum)

    def generate_structure(self):
        # todo
        return (4, 4, 2, 4)

    def select_chord(self, seq: Sequence):
        seq.chord = "Am"
        return seq

    def select_tempo(self, seq: Sequence):
        # todo
        seq.tempo = 120
        return seq

    def select_pattern(self, seq: Sequence):
        # todo
        return seq

