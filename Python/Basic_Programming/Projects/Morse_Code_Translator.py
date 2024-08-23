import winsound
import time

morse_code_dict = {
    'A': '.-',    'B': '-...',  'C': '-.-.',
    'D': '-..',   'E': '.',     'F': '..-.',
    'G': '--.',   'H': '....',  'I': '..',
    'J': '.---',  'K': '-.-',   'L': '.-..',
    'M': '--',    'N': '-.',    'O': '---',
    'P': '.--.',  'Q': '--.-',  'R': '.-.',
    'S': '...',   'T': '-',     'U': '..-',
    'V': '...-',  'W': '.--',   'X': '-..-',
    'Y': '-.--',  'Z': '--..',

    '0': '-----', '1': '.----', '2': '..---',
    '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..',
    '9': '----.'
}

# Take input from user
def take_input():
    print('''
          1. Click one for Text --> Morse code 
          2. Click two for Morse Code --> Text  
          ''')
    choice = input("Enter your choice: ")
    
    if choice == '1':
        text = input("\nEnter your text: ")
    elif choice == '2':
        text = input("\nEnter the Morse Code: ")
    else:
        print("Invalid choice")
        return None, None
    return choice, text

# Generate Morse code
def generate_morse_code(text):
    morse_code_text = ''
    for char in text.upper():
        if char in morse_code_dict:
            morse_code_text += morse_code_dict[char] + ' '
        elif char == ' ':
            morse_code_text += '/ '  # Separator for words
        else:
            morse_code_text += char + ' '
    print('\nYour Morse Code is:', morse_code_text)
    return morse_code_text

# Generate text from Morse code
def generate_text(morse_code_text):
    morse_code_text = morse_code_text.split(' ')
    plain_text = ''
    for char in morse_code_text:
        if char == '/':  # Handle word separation
            plain_text += ' '
        for key, value in morse_code_dict.items():
            if char == value:
                plain_text += key
                break
    print('\nYour Plain text is:', plain_text)
    return plain_text

# Play sound for Morse code
def set_sound(morse_code_text):
    for char in morse_code_text:
        if char == '.':
            winsound.Beep(1000, 200)  # Dot sound
        elif char == '-':
            winsound.Beep(1000, 600)  # Dash sound
        elif char == '/':
            time.sleep(0.7)  # Word separator pause
        time.sleep(0.2)  # Pause between signals

# Main loop
while True:
    if input('\nDo you want to play? (Y/N): ').lower() == 'y':
        choice, text = take_input()
        if choice == '1':
            morse_code_text = generate_morse_code(text)
            play_sound = input("\nDo you want to play the Morse code sound? (Y/N): ").lower()
            if play_sound == 'y':
                set_sound(morse_code_text)
        elif choice == '2':
            generate_text(text)
    else:
        print('\nThank you for using the Morse code converter!')
        break

# TIME -> 7:30AM, Friday, 23 August 2024 (IST)