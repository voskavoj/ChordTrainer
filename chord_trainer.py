from metronome import Metronome
from chord_trainer_gen import ChordTrainerGenerator


class ChordTrainer:
    def __init__(self, ui):
        self.gen = ChordTrainerGenerator()
        self.metronome = Metronome(ui=ui)

        self.structure = self.gen.generate_structure()
        self.current_seq = self.gen.get_starting_sequence()
        self.next_seq = self.current_seq

        self.loop()

    def loop(self):
        while True:
            for segment_len in self.structure:
                for chord in range(segment_len):
                    # move sequences
                    self.current_seq = self.next_seq
                    # generate new next sequence
                    self.next_seq = self.gen.select_chord(self.current_seq)
                    # view
                    self.send_to_metronome()

                # after segment, change tempo and pattern
                self.next_seq = self.gen.select_tempo(self.current_seq)
                self.next_seq = self.gen.select_pattern(self.current_seq)
            # after whole song, make one repetition and start over
            self.next_seq = self.gen.get_starting_sequence()
            self.send_to_metronome()
            self.structure = self.gen.generate_structure()

    def send_to_metronome(self):
        self.metronome.show_sequence(self.current_seq, self.next_seq)
