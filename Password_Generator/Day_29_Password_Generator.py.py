from tkinter import *
from tkinter import messagebox
from random import *
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    """
    Generates a random password from a combination of the symbols in 'letters', 'numbers' and
    'symbols'.
    :return: nothing
    """
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letter = [choice(letters) for i in range(randint(8, 10))]

    password_symbols = [choice(symbols) for j in range(randint(2, 4))]

    password_numbers = [choice(numbers) for k in range(randint(2, 4))]

    password_list = password_letter + password_symbols + password_numbers

    shuffle(password_list)

    password = "".join(password_list)

    password_entry.insert(0, string=password)


# ---------------------------- SEARCH FUNCTION ------------------------------- #
def search():
    """
    Extracts the name of a website from the website entry of the GUI.
    Compares the entry with all the website names in the JSON file.
    If there is a match, the corresponding email address and password are shown in a new info window.
    :return:
    """
    user_website = website_entry.get()
    try:
        with open("Password_Manager_List.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Warning", message="No password dictionary found!")
    else:
        if user_website in data:
            messagebox.showinfo(title=f"{user_website} Email & Password",
                                message=f"Your login data for {user_website} are: \n"
                                        f"Email: {data[user_website]['email']} \n"
                                        f"Password: {data[user_website]['password']}")
        else:
            messagebox.showinfo(title="Warning", message=f"No data for {user_website} found.")


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    """
    Reads the user data from the TKInter entry fields and saves them into a JSON file.
    If no JSON files exists, the file is created.
    :return: nothing
    """
    user_website = website_entry.get()
    user_email = email_user_entry.get()
    user_password = password_entry.get()
    new_data = {
        user_website: {
            "email": user_email,
            "password": user_password,
        }
    }

    if len(user_website) == 0 or len(user_password) == 0:
        messagebox.showinfo(title="Warning", message="Please don't leave any fields empty!")

    else:
        is_ok = messagebox.askokcancel(title=user_website,
                                       message=f"These are the details entered: \nEmail: {user_email}"
                                               f"\nPassword: {user_password} \nIs it ok to save?")

        if is_ok:
            try:
                with open("Password_Manager_List.json", "r") as data_file:
                    # Reading old data
                    data = json.load(data_file)
                with open("Password_Manager_List.json", "w") as data_file:
                    # Saving updated data
                    json.dump(data, data_file, indent=4)
            except FileNotFoundError:
                with open("Password_Manager_List.json", "w") as data_file:
                    # Saving updated data
                    json.dump(new_data, data_file, indent=4)
            else:
                # Updating old data with new data
                data.update(new_data)

                with open("Password_Manager_List.json", "w") as data_file:
                    # Saving updated data
                    json.dump(data, data_file, indent=4)
            finally:
                website_entry.delete(0, END)
                password_entry.delete(0, END)
                pyperclip.copy(user_password)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, bg="white")

canvas = Canvas(width=200, height=200, bg="white")
lock_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_image)
canvas.grid(sticky="w", column=1, row=0)

website_lb = Label(text="Website:", bg="white")
website_lb.grid(column=0, row=1)

email_user_lb = Label(text="Email/Username:", bg="white")
email_user_lb.grid(column=0, row=2)

password_lb = Label(text="Password:", bg="white")
password_lb.grid(column=0, row=3)

website_entry = Entry(width=30)
website_entry.grid(sticky="w", column=1, row=1, columnspan=2)
website_entry.focus()

search_button = Button(text="Search", width=10, command=search)
search_button.grid(sticky="e", column=1, row=1)

email_user_entry = Entry(width=43)
email_user_entry.grid(sticky="w", column=1, row=2, columnspan=2)
email_user_entry.insert(0, "test.address@test.com")

password_entry = Entry(width=30)
password_entry.grid(sticky="w", column=1, row=3, columnspan=2)

generate_button = Button(text="Generate Password", command=generate_password)
generate_button.grid(sticky="e", column=1, row=3, columnspan=2)

add_button = Button(text="Add", width=36, command=save)
add_button.grid(column=1, row=4)

window.mainloop()
