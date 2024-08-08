# Email Simulator

This project is a simple email simulator implemented in Python. It allows users to simulate receiving, reading, marking as spam, and deleting emails from an inbox.

## Features

- **Email Class**: 
  - Represents an individual email with attributes for the email address, subject line, and email content.
  - Includes methods to mark the email as read or mark it as spam.

- **Inbox**:
  - Stores a list of `Email` objects.
  - Populated with sample emails upon initialization.

- **Email Operations**:
  - List all emails with their status (read/unread).
  - Read an email and optionally delete it, mark it as spam, or return to the main menu.
  - View all unread emails.

## How to Use

1. **Initialization**:
   - The inbox is automatically populated with three sample emails when the script is run.

2. **Menu Options**:
   - The script provides a looped menu with the following options:
     1. **Read an Email**: Displays a list of emails, allows the user to select an email to read, and then provides options to delete, mark as spam, or return to the menu.
     2. **View Unread Emails**: Displays all emails that have not been marked as read.
     3. **Quit Application**: Exits the program.

3. **User Input**:
   - The user is prompted to enter a number corresponding to their choice from the menu.
   - If an invalid input is provided, an error message is displayed, and the menu is shown again.

## Code Overview

### Email Class

```python
class Email():
    def __init__(self, email_address, subject_line, email_content):
        self.email_address = email_address
        self.subject_line = subject_line
        self.email_content = email_content
        self.has_been_read = False
        self.is_spam = False

    def mark_as_read(self):
        self.has_been_read = True

    def mark_as_spam(self):
        self.is_spam = True
Attributes:

email_address: The email address of the sender.
subject_line: The subject of the email.
email_content: The body of the email.
has_been_read: Tracks whether the email has been read (default is False).
is_spam: Tracks whether the email has been marked as spam (default is False).
Methods:

mark_as_read(): Marks the email as read.
mark_as_spam(): Marks the email as spam.
Functions
populate_inbox(): Populates the inbox with three sample emails.
list_emails(): Lists all emails in the inbox with their read/unread status.
read_email(): Allows the user to read, delete, or mark an email as spam.
Main Loop
The script runs a loop where the user can interact with the menu until they choose to exit the application.

Running the Script
To run the script, simply execute the email.py file in a Python environment:


Copy code
python email.py
The program will then display the menu and await user input.

Dependencies
Python 3.x

Future Enhancements
Some possible future improvements to the email simulator could include:

Saving and Loading Emails: Persist the state of the inbox to a file so that it can be saved and reloaded between sessions.
Replying to Emails: Add functionality to reply to an email or forward it.
Search Functionality: Allow users to search for emails by sender, subject, or content.