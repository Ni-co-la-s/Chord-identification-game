import random
import tkinter as tk
from tkinter import ttk
from pydub import AudioSegment
from pydub.playback import play
from piano_classes import PianoNote, PianoChord
from utils import chord_lists,select_random_note


# Global variables
selected_note = None
current_chord = None
current_chord_root = None
current_chord_type = None
total_chords = 0
correct_chords = 0

def select_random_chord(chord_lists):
    """
    Selects a random chord from the available chord types in the listbox.
    
    Args:
        chord_lists (dict): A dictionary containing chord types and corresponding intervals.
    
    Returns:
        tuple: The type and intervals of the randomly selected chord.
    """
    selected_chord_types = [chord_listbox.get(i) for i in chord_listbox.curselection()]
    random_chord_type = random.choice(selected_chord_types)
    random_chord_list = chord_lists[random_chord_type]
    random_chord = random_chord_list[0]
    return random_chord_type, random_chord

def play_random_chord():
    """
    Plays a random chord from the selected chord types in the listbox.
    Updates the global variables for current chord, its root, type and total chords.
    Updates the score label with the current score.
    """
    global current_chord, current_chord_root, current_chord_type, total_chords
    current_chord_type, current_chord_intervals = select_random_chord(chord_lists)
    current_chord_root = select_random_note()
    current_chord = PianoChord(current_chord_root, current_chord_intervals)
    print("Random Chord Type:", current_chord_type)
    print("Random Chord Root:", current_chord_root)
    current_chord.play()
    total_chords += 1
    score_label.config(text=f"Score: {correct_chords}/{total_chords}")

def play_chord():
    """
    Plays the current chord if it exists.
    """
    global current_chord
    if current_chord is not None:
        current_chord.play()

def reset_interface():
    """
    Resets the interface
    """
    result_label.config(text="")
    play_button.config(bg="SystemButtonFace")
    for button in note_buttons.values():
        button.config(state=tk.NORMAL)
        button.config(bg="SystemButtonFace")
    for button in chord_buttons.values():
        button.config(state=tk.NORMAL)
        button.config(bg="SystemButtonFace")  # Set chord buttons back to normal appearance
    play_random_chord()

    
def note_button_click(note):
    """
    Handles the event of clicking a note button.
    Args:
        note (str): The note that was clicked.
    """
    global selected_note
    if not guess_type_only_var.get():  # If Guess Type Only checkbox is not checked
        selected_note = note
        for button in note_buttons.values():
            button.config(bg="SystemButtonFace")
        note_buttons[note].config(bg="orange")

def chord_button_click(chord_type):
    """
    Handles the event of clicking a chord button. Checks if the selected note and chord type matches the actual chord. 
    Updates the result label, button colors, score label and disables note and chord buttons.

    Args:
        chord_type (str): The chord type that was clicked.
    """
    global selected_note, current_chord, current_chord_root, current_chord_type, correct_chords
    if guess_type_only_var.get() == 1:
        if chord_type == current_chord_type:
            result_label.config(text="Correct!", fg="green")
            play_button.config(bg="green")
            correct_chords += 1
        else:
            result_label.config(text="Incorrect!", fg="red")
            play_button.config(bg="red")
            chord_buttons[current_chord_type].config(bg="green")  # highlight correct chord
    else:
        if selected_note and current_chord:
            selected_note = selected_note.lower().replace('#', 's')
            if selected_note == current_chord_root.lower().replace('#', 's')[:-1] and chord_type == current_chord_type:
                result_label.config(text="Correct!", fg="green")
                play_button.config(bg="green")
                correct_chords += 1
            else:
                result_label.config(text="Incorrect!", fg="red")
                play_button.config(bg="red")
                note_buttons[current_chord_root[:-1].replace('s', '#').upper()].config(bg="green")  # highlight correct note
                chord_buttons[current_chord_type].config(bg="green")  # highlight correct chord
        else:
            result_label.config(text="Please select a note first", fg="red")
            return
    for button in note_buttons.values():
        button.config(state=tk.DISABLED)
    for button in chord_buttons.values():
        button.config(state=tk.DISABLED)
    root.after(1000, reset_interface)
    score_label.config(text=f"Score: {correct_chords}/{total_chords}")
    selected_note = ""
    

def update_note_buttons():
    """
    Updates the state and color of note buttons based on the state of the checkbox.
    """
    if guess_type_only_var.get():  # If Guess Type Only checkbox is checked
        for button in note_buttons.values():  # Disable all note buttons
            button.config(state=tk.DISABLED) 
    else:
        for button in note_buttons.values():  # Enable all notee buttons
            button.config(state=tk.NORMAL) 
            button.config(bg="SystemButtonFace")


def select_chord_listbox(event):
    """
    Handles the event of selecting chords in the listbox. 
    Args:
        event (Event): The event object passed by the Tkinter event system.
    """
    global chord_buttons
    chord_buttons = {}  # Clear old buttons

    # Delete old buttons
    for widget in chord_frame.winfo_children():
        widget.destroy()

    # Create new buttons
    selected_chords = [chord_listbox.get(i) for i in chord_listbox.curselection()]
    for i, chord_type in enumerate(selected_chords):
        chord_button = tk.Button(chord_frame, text=chord_type, width=10, command=lambda chord=chord_type: chord_button_click(chord))
        chord_button.grid(row=i // 3, column=i % 3, padx=5, pady=5)
        chord_buttons[chord_type] = chord_button


# Create the GUI
root = tk.Tk()
root.title("Chord Identification")
root.geometry("800x600")

# Score label
score_label = tk.Label(root, text="Score: 0/0", anchor="w")
score_label.pack(fill="x", padx=10)

button_frame = tk.Frame(root)
button_frame.pack(pady=10)

# Button for playing random chord
play_button = tk.Button(button_frame, text="Play Random Chord", command=play_random_chord)
play_button.grid(row=0, column=1, padx=5, pady=5)

# Button for repeating chord
repeat_button = tk.Button(button_frame, text="Repeat Chord", command=play_chord)
repeat_button.grid(row=0, column=0, padx=5, pady=5)

# Buttons for notes
note_frame = tk.Frame(root)
note_frame.pack(pady=10)

note_buttons = {}

notes = ["A", "A#", "B", "C", "C#", "D", "D#", "E", "F", "F#", "G", "G#"]

for i, note_name in enumerate(notes):
    note_button = tk.Button(note_frame, text=note_name, width=5, command=lambda note=note_name: note_button_click(note))
    note_button.grid(row=0, column=i, padx=2, pady=2)
    note_buttons[note_name] = note_button

# Buttons for chord types
chord_frame = tk.Frame(root)
chord_frame.pack(pady=10)

chord_buttons = {}

chord_types = list(chord_lists.keys())

for i, chord_type in enumerate(chord_types):
    chord_button = tk.Button(chord_frame, text=chord_type, width=10, command=lambda chord=chord_type: chord_button_click(chord))
    chord_button.grid(row=i // 3, column=i % 3, padx=5, pady=5)
    chord_buttons[chord_type] = chord_button

result_label = tk.Label(root, text="")
result_label.pack(pady=10)

# Option check boxes
options_frame = tk.Frame(root)
options_frame.pack(pady=10)

guess_type_only_var = tk.IntVar()
guess_type_only_var.trace("w", lambda *args: update_note_buttons())
guess_type_only_check = tk.Checkbutton(options_frame, text="Guess Type Only", variable=guess_type_only_var)
guess_type_only_check.pack(side=tk.LEFT, padx=10)

# Listbox for chords
chord_listbox = tk.Listbox(root, selectmode=tk.MULTIPLE)
chord_listbox.bind("<<ListboxSelect>>", select_chord_listbox)

chord_types = list(chord_lists.keys())
for i, chord_type in enumerate(chord_types):
    chord_listbox.insert(tk.END, chord_type)
    if chord_type in [    "Major", "Minor", "Sus2", "Sus4", "Diminished",
                      "Augmented", "Major 7th", "Minor 7th","Dominant 7th"]:
        chord_listbox.selection_set(i)

chord_listbox.pack(pady=10)


root.mainloop()