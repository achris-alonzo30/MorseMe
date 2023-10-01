import json


class MorseCoder:
    def __init__(self):
        with open('morse_code.json', 'r') as file:
            self.data = json.load(file)
        self.encoder = ''
        self.decoder = ''

    def encode(self, text):
        for char in text:
            # This check if the text contains space init.
            if char == ' ':
                # Add a space directly if the character is a space
                self.encoder += ' '
            else:
                # [ + ' ' ] will add a space after each Morse Code character
                self.encoder += self.data[char] + ' '

    def decode(self, morse_code):
        words = morse_code.split('/')  # Split the Morse code by '/'
        for word in words:
            letters = word.split()  # Split each word into individual Morse code letters
            for letter in letters:
                if letter == '':
                    self.decoder += ' '  # Add an empty space
                elif letter in self.data.values():  # Checks if letter in the data values
                    # Retrieve the letters using the index.
                    self.decoder += list(self.data.keys())[list(self.data.values()).index(letter)]
                else:
                    self.decoder += '?'  # Use '?' for unrecognized Morse code characters
            if len(word) > 0:  # Check if the word is not empty
                self.decoder += ' '  # Add a space between words

    def reset(self):
        # Reset the MorseCoder instance
        self.encoder = ""
        self.decoder = ""
