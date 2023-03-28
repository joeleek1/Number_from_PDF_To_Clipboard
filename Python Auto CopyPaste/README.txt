Invoice Number Extractor
The Invoice Number Extractor is a Python script that utilizes tkinter for a simple GUI. It allows users to extract invoice numbers from a pasted text input based on a custom prefix and length. The extracted invoice numbers are then automatically copied to the clipboard one by one as the user presses Ctrl + V.

Features
Customizable prefix and length for invoice numbers
Automatic clipboard handling for easy pasting of extracted invoice numbers
Simple and easy-to-use GUI
Requirements
Python 3.6 or higher
tkinter (included in the standard library)
pyperclip
keyboard
Installation
Install the required packages:

Copy code
pip install pyperclip keyboard
Save the Invoice Number Extractor script as a .py file (e.g., invoice_number_extractor.py).

Usage
Run the script:

Copy code
python invoice_number_extractor.py
The Invoice Number Extractor GUI will open.

Enter the custom prefix and length for the invoice numbers in the provided input fields.

Paste the text containing the invoice numbers in the large text box.

Click the "Submit" button to extract the invoice numbers.

Press Ctrl + V to paste the extracted invoice numbers one by one. The application will automatically copy the next invoice number after each paste action. When all invoice numbers have been pasted, the word "Finished" will be copied to the clipboard.

There is also an executable version for windows that can be found in the dist folder.

License
This project is available under the MIT License. See the LICENSE file for more info.
