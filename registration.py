from tkinter import *

def validate_registration():
    name = name_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    confirm_password = confirm_password_entry.get()

    # Perform validation logic here
    # ...

    # If validation passes, perform further processing (e.g., database insertion)
    # ...

    # Clear form fields after successful registration
    name_entry.delete(0, END)
    email_entry.delete(0, END)
    password_entry.delete(0, END)
    confirm_password_entry.delete(0, END)

    # Display success message or redirect to another page
    success_label = Label(window, text="Registration successful!")
    success_label.pack()

window = Tk()
window.title("Registration Form")

# Create labels and entry fields
name_label = Label(window, text="Name:")
name_label.pack()
name_entry = Entry(window)
name_entry.pack()

email_label = Label(window, text="Email:")
email_label.pack()
email_entry = Entry(window)
email_entry.pack()

password_label = Label(window, text="Password:")
password_label.pack()
password_entry = Entry(window, show="*")
password_entry.pack()

confirm_password_label = Label(window, text="Confirm Password:")
confirm_password_label.pack()
confirm_password_entry = Entry(window, show="*")
confirm_password_entry.pack()

register_button = Button(window, text="Register", command=validate_registration)
register_button.pack()

window.mainloop()
