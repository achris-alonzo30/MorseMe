from tkinter import *
from morse_coder import MorseCoder

# Import Classes
morse_coder = MorseCoder()

# Static
FONT_NAME = "Courier"
FONT_COLOR = "#2D4356"
BG_COLOR = "#F7FBFC"
LIGHT_BLUE = "#769FCD"
LIGHTER_BLUE = "#B9D7EA"
LIGHTEST_BLUE = "#D6E6F2"


# Change the selected option (Encode or Decode) when the user selects an option in the OptionMenu widget.
def handle_selection(selection):
    if selection == "Encode":
        label_option.config(text="Decode")

    elif selection == "Decode":
        label_option.config(text="Encode")


# Convert the text from the input Text widget to the output Text widget.
def convert_text():
    selection = selected_option.get()  # Get the selected option (Encode or Decode)
    input_text = text_input.get("1.0", "end-1c").lower()  # Get the all text from the input Text widget

    if selection == "Encode":
        morse_coder.encode(input_text)  # Encode the input text
        text_output.delete("1.0", "end")  # Clear the output Text widget
        text_output.insert(END, morse_coder.encoder)  # Insert the encoded text in the output Text widget
    elif selection == "Decode":
        morse_coder.decode(input_text)  # Decode the input text
        text_output.delete("1.0", "end")  # Clear the output Text widget
        text_output.insert(END, morse_coder.decoder)  # Insert the decoded text in the output Text widget


# Clears the text from the input Text widget and the output Text widget.
def clear():
    text_output.delete("1.0", "end")
    text_input.delete("1.0", "end")
    morse_coder.reset()


# Create a window
root = Tk()
root.title("Morse Code Converter")
root.config(padx = 50, pady = 50, bg = BG_COLOR)

# Create a frame for Input
canvas_input = Canvas(root, width = 300, height = 300, bg = LIGHTEST_BLUE, highlightthickness = 1)

selected_option = StringVar()
selected_option.set("Encode")
option_menu = OptionMenu(root, selected_option, "Encode", "Decode", command = handle_selection)
option_menu.config(width = 6, font = (FONT_NAME, 20), bg = BG_COLOR, fg = LIGHT_BLUE, highlightthickness = 1)
canvas_input.create_window(150, 45, window = option_menu)

text_input = Text(root, width = 25, height = 10, fg = FONT_COLOR, bg = LIGHTER_BLUE, highlightthickness = 1)
text_input.config(font = (FONT_NAME, 15), padx = 20, pady = 20)
text_input.insert("1.0", "Ex. Hello World")  # Insert "Example Text" at the beginning (line 1, column 0)
text_input.bind("<FocusIn>", lambda event: text_input.delete("1.0", "end") if text_input.get("1.0", "end-1c") == "Ex. Hello World" else None)
text_input.bind("<FocusOut>", lambda event: text_input.insert("1.0", "Ex. Hello World") if not text_input.get("1.0", "end-1c") else None)

canvas_input.create_window(150, 180, window = text_input)

canvas_input.grid(column = 0, row = 0, padx = 10)

# -------------------------------------------------------------------------------------------------------------------- #

# Create a frame for Output
canvas_output = Canvas(root, width = 300, height = 300, bg = LIGHTEST_BLUE, highlightthickness = 1)

label_option = Label(canvas_output, text = "")
label_option.config(width = 10, font = (FONT_NAME, 20), bg = BG_COLOR, fg = LIGHT_BLUE, highlightthickness = 0)
canvas_output.create_window(150, 45, window = label_option)

text_output = Text(root, width = 25, height = 10, fg = FONT_COLOR, bg = LIGHTER_BLUE, highlightthickness = 1)
text_output.config(font = (FONT_NAME, 15), padx = 20, pady = 20)
text_output.insert("1.0", "Ex. .... . .-.. .-.. --- / .-- --- .-. .-.. -..")
canvas_output.create_window(150, 180, window = text_output)
canvas_output.grid(column = 1, row = 0, padx = 10)

# -------------------------------------------------------------------------------------------------------------------- #
convert = Button(root, text = "Convert", command = convert_text)
convert.config(width = 10, font = (FONT_NAME, 20), fg="#321E1E", highlightthickness = 0)
convert.grid(column = 0, row = 1, columnspan = 2, pady=20)

clear = Button(root, text = "Restart", command = clear)
clear.config(width = 10, font = (FONT_NAME, 20), fg="#5C8984", highlightthickness = 0)
clear.grid(column = 0, row = 2)

exit_window = Button(root, text = "Exit", command = root.quit)
exit_window.config(width = 10, font = (FONT_NAME, 20), fg="#CD1818", highlightthickness = 0)
exit_window.grid(column = 1, row = 2)

root.mainloop()
