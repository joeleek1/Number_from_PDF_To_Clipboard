import re
import tkinter as tk
from tkinter import ttk

import pyperclip
import time
import keyboard
from threading import Thread

def extract_inv_numbers(text):
    pattern = r'\bINV-(\d{5})\b'
    inv_numbers = re.findall(pattern, text)
    return inv_numbers

def submit_text():
    text = text_entry.get("1.0", "end-1c")
    global inv_numbers
    inv_numbers = extract_inv_numbers(text)
    inv_numbers.append("Finished")
    print(inv_numbers)
    copy_next_item()

def copy_next_item():
    global current_index
    if current_index < len(inv_numbers):
        next_item = inv_numbers[current_index]
        pyperclip.copy(next_item)
        print(f'Copied to clipboard: {next_item}')
        current_index += 1
    else:
        print('No more items in the list.')

def check_paste_key():
    global current_index
    while True:
        if current_index < len(inv_numbers):
            if keyboard.is_pressed('ctrl') and keyboard.is_pressed('v'):
                while keyboard.is_pressed('ctrl') or keyboard.is_pressed('v'):
                    time.sleep(0.1)

                time.sleep(0.1)
                copy_next_item()

def main():
    global text_entry
    global current_index
    global inv_numbers
    current_index = 0
    inv_numbers = []

    root = tk.Tk()
    root.title("Invoice Number Extractor")

    main_frame = ttk.Frame(root, padding="10")
    main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

    text_entry = tk.Text(main_frame, wrap=tk.WORD, width=40, height=10)
    text_entry.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

    submit_button = ttk.Button(main_frame, text="Submit", command=submit_text)
    submit_button.grid(row=1, column=0, pady=10)

    paste_key_thread = Thread(target=check_paste_key)
    paste_key_thread.daemon = True
    paste_key_thread.start()

    root.mainloop()

if __name__ == "__main__":
    main()
