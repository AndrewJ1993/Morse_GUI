import tkinter
import RPi.GPIO as GPIO
import time


GPIO.setmode(GPIO.BCM)
GPIO.setup(13, GPIO.OUT)
GPIO.setup(26, GPIO.OUT)
GPIO.setup(5, GPIO.OUT)


# Gui definitions
win = tkinter.Tk()
v = tkinter.StringVar()
win.title("Morse Code")

morse_alphabet = {"A": ".-",    "B": "-...",   "C": "-.-.", 
                 "D": "-..",    "E": ".",      "F": "..-.",
                 "G": "--.",    "H": "....",   "I": "..",
                 "J": ".---",   "K": "-.-",    "L": ".-..",
                 "M": "--",     "N": "-.",     "O": "---",
                 "P": ".--.",   "Q": "--.-",   "R": ".-.",
                 "S": "...",    "T": "-",      "U": "..-",
                 "V": "...-",   "W": ".--",    "X": "-..-",
                 "Y": "-.--",   "Z": "--..",
 
                 "0": "-----",  "1": ".----",  "2": "..---",
                 "3": "...--",  "4": "....-",  "5": ".....",
                 "6": "-....",  "7": "--...",  "8": "---..",
                 "9": "----." 
                 }

wait_length = .5
dash_length = .3
dot_length = .1

def dash():
    GPIO.output(5, GPIO.HIGH)
    time.sleep(dash_length)
    GPIO.output(5, GPIO.LOW)
    time.sleep(wait_length)


def dot():
    GPIO.output(5, GPIO.HIGH)
    time.sleep(dot_length)
    GPIO.output(5, GPIO.LOW)
    time.sleep(wait_length)


def morse_translator(word):
    word = word[:13].upper()
    for letter in word:
        print(letter)
        morse_representation = morse_alphabet[letter]
        morse_blinker(morse_representation)


def morse_blinker(word):
    for dot_dash in word:
        if dot_dash == ".":
            dot()
        else:
            dash()


# Widgets
entry = tkinter.Entry(win, textvariable=v).grid(row=1, column=1)
led_button = tkinter.Button(win, text = "Submit",  command = lambda: morse_translator(v.get()), height = 1, width = 24).grid(row=3, column=1)


win.mainloop()
