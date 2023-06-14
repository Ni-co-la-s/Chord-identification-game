from piano_classes import PianoNote, PianoChord
import random

# Major chords
major_chord_intervals = [
    [0, 4, 7],
    [4, 7, 12],
    [7, 12, 16]
]

# Minor chords
minor_chord_intervals = [
    [0, 3, 7],
    [3, 7, 12],
    [7, 12, 15]
]

# Sus2 chords
sus2_chord_intervals = [
    [0, 2, 7],
    [2, 7, 12],
    [7, 12, 14]
]

# Sus4 chords
sus4_chord_intervals = [
    [0, 5, 7],
    [5, 7, 12],
    [7, 12, 17]
]

# Diminished chords
dim_chord_intervals = [
    [0, 3, 6],
    [3, 6, 12],
    [6, 12, 15]
]

# Augmented chords
aug_chord_intervals = [
    [0, 4, 8],
    [4, 8, 12],
    [8, 12, 16]
]


# Major 7th chords (MM7)
major_7th_chord_intervals = [
    [0, 4, 7, 11],
    [4, 7, 11, 14],
    [7, 11, 14, 17],
    [11, 14, 17, 21]
]

# Minor 7th chords (mm7)
minor_7th_chord_intervals = [
    [0, 3, 7, 10],
    [3, 7, 10, 14],
    [7, 10, 14, 17],
    [10, 14, 17, 21]
]

# Dominant 7th chords (Mm7)
dominant_7th_chord_intervals = [
    [0, 4, 7, 10],
    [4, 7, 10, 14],
    [7, 10, 14, 17],
    [10, 14, 17, 20]
]


# Dictionary of chord types and their intervals
chord_lists = {
    "Major": major_chord_intervals,
    "Minor": minor_chord_intervals,
    "Sus2": sus2_chord_intervals,
    "Sus4": sus4_chord_intervals,
    "Diminished": dim_chord_intervals,
    "Augmented": aug_chord_intervals,
    "Major 7th": major_7th_chord_intervals,
    "Minor 7th": minor_7th_chord_intervals,
    "Dominant 7th": dominant_7th_chord_intervals
}

def select_random_note(start_note="c3",end_note="c6"):
    start_index = PianoNote.NOTE_NAMES.index(start_note)
    end_index = PianoNote.NOTE_NAMES.index(end_note)
    random_index = random.randint(start_index, end_index)
    random_note = PianoNote.NOTE_NAMES[random_index]
    return random_note

