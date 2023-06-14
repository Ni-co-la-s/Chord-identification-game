# Chord-identification-game
Small game to practice recognizing either quality of chords with relative pitch or exact chords with perfect pitch. The program plays a random chord and you need to guess the correct chord type and optionally the root note.

## Features

- Play a random chord for identification.
- Guess the chord type and root note.
- Score tracking to keep track of your progress.
- Option to guess the chord type only or both type and root note.
- Highlighting of correct notes and chords for feedback.

## Requirements

- Python 3.x
- Tkinter library (included in the standard Python distribution)
- pydub library (to play audio files)

## Installation

1. Clone the repository or download the source code files.
2. Install the required libraries:
    ```shell
    pip install pydub
    ```
3. Run the program:
    ```shell
    python chord_identification.py
    ```

## Usage

1. Launch the program.
2. Click the "Play Random Chord" button to hear a randomly generated chord.
3. Guess the chord type and optionally the root note.
4. Click the corresponding chord buttons to make your selection.
5. The program will display whether your guess is correct or incorrect.
6. The score label will keep track of your correct guesses out of the total chords played.
7. You can choose to guess the chord type only by checking the "Guess Type Only" checkbox.
8. To start a new game, click the "Play Random Chord" button again.
