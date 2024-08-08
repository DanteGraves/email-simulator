# Create Class for Email simulator.
class Email():

    # Create method with 3 arguments. 
    def __init__(self, email_address, subject_line, email_content):

        self.email_address = email_address
        self.subject_line = subject_line
        self.email_content = email_content

        # initialize variables and defualt to False.
        self.has_been_read = False
        self.is_spam = False

    # Create function to change default value to True when email has been read.
    def mark_as_read(self):
        self.has_been_read = True

    # Create function to change default value to True when email is marked as spam.
    def mark_as_spam(self):
        self.is_spam = True

# Create empty list to create inbox.
inbox = []

# Create function to populate inbox with sample emails.
def populate_inbox():

    sample_email1 = Email("HyperionDev@gmail.com", "Welcome to HyperionDev!", "Thank you for joining our platform.")
    sample_email2 = Email("dantegraves@gmail.com", "Great work on the bootcamp!", "The bootcamp has been impressive")
    sample_email3 = Email("HyperionDev@gmail.com", "Your excellent marks!", "Congratulations on your achievements!")

    # Append sample emails to inbox.
    inbox.extend([sample_email1, sample_email2, sample_email3])

# Create function to list emails by number.
def list_emails():

    print("View Inbox:\n")

    # Enumerate emails.
    for index, email in enumerate(inbox):
        # Print numbered emails and mark as read/unread.
        print(f"{index+1}. {email.subject_line} - {'Read' if email.has_been_read else 'Unread'}")
        
# Create function to open a chosen email.        
def read_email():

    # Call function to list all emails to choose from.
    list_emails()
    # Request from user to enter which email to open.
    email_choice = int(input("Enter the number of the email you wish to view: ")) - 1

    # Code block to open chosen email and mark email as read.
    if 0 <= email_choice < len(inbox):

        email = inbox[email_choice]

        if not email.has_been_read:
            email.mark_as_read()

        # Display email to user.
        print(f"\nFrom: {email.email_address}\nSubject: {email.subject_line}\nContent: {email.email_content}\n")
        
        # Request from user what action they wish to take with email.
        email_action = input("Enter 'D' to delete email, 'M' to mark email as spam, 'E' to exit to main menu: ").lower()

        # If user enters "D" the email is deleted from inbox.
        if email_action == 'd':
            inbox.pop(email_choice)
            print(f"Email has been deleted!\n")

        # If user enters 'M' the email is marked as spam.
        elif email_action == 'm':
            email.mark_as_spam()
            print(f"Email marked as spam!\n")

        # If user enters 'E' code will loop back to main menu.
        elif email_action == 'e':
            print("Returning to menu.")

        # Error message if user enters incorrectly.
        else:
            print("Invalid entry, email not deleted.\n")

    # Error message if user enters incorrectly.        
    else:
        print("Invalid email number!\n")

# Call function to populate inbox with sample emails.
populate_inbox()

# Start loop for menu options.
while True:

    # Print emails in inbox to user.
    list_emails()

    # Display how many emails are in the inbox.
    print(f"\nYou have {len(inbox)} emails in your inbox.\n")

    # Display menu options.
    print("Menu Options:")
    print("1. Read an email.")
    print("2. View unread emails.")
    print("3. Quit application.")

    # Request user to input menu choice to continue.
    user_choice = input("Enter the number you wish to proceed with: ")

    # If user enters 1 function will be called to read emails.
    if user_choice == '1':
        read_email()

    # If user enters 2 emails that have been left unread will be displayed.
    elif user_choice == '2':
        print("\nUnread Emails:\n")
        for email in inbox:
            if not email.has_been_read:
                print(f"From: {email.email_address}\nSubject: {email.subject_line}\n")

    # If user enters 3 code will exit.            
    elif user_choice == '3':
        print("Goodbye!!!")
        break

    # Error message if user enters incorrectly.
    else:
        print("Oops - incorrect input.\n")

# End code.