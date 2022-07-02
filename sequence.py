from dataclasses import dataclass


@dataclass
class Sequence:
    chord: str
    octave: int
    barre: bool
    signature: tuple
    tempo: int
    strum: dict
