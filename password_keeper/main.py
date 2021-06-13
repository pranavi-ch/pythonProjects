# only imports classes and constants
from tkinter import *
from tkinter import messagebox
import random
import pyperclip

WHITE = "#FFFFFF"
FONT = "helvetica"
BUBBLE = "#E6EEFF"
# pre save email as user name
MY_EMAIL = "example321@gmail.com"


# ----------------- CHECK IF EXISTS-----------------------------------
def check_if_exists(website):
    with open("passwords.txt", "r") as f:
        lines = f.readlines()
    websites=[]
    for line in lines:
        websites.append(line.split(" |")[0])

    if website in websites:
        return True
    return False


# ------------------------------- REPLACE ENTRY -----------------------
def replace_entry(website,username,password):
    with open("passwords.txt","r") as f:
        lines = f.readlines()
    with open("passwords.txt","w") as f:
        for line in lines:
            if line == "\n":
                continue
            webs = line.split(" |")[0]
            print(webs)
            if webs != website:
                f.write(line)

        # write the new entry
        f.write(f"\n{website} | {username} | {password}")


# ----------------------------GENERATE PASSWORD------------------------
lowers = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
          'w', 'x', 'y', 'z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
capitals = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
            'V', 'W', 'X', 'Y', 'Z']


# ------------------ Random strong password generating algo, can be customized for max security -------------------
def generate_password():
    password_list = []
    for i in range(0, 3):
        password_list += random.choice(capitals)
        password_list += random.choice(numbers)
        password_list += random.choice(symbols)
        password_list += random.choice(lowers)
    random.shuffle(password_list)
    password = ""
    for ch in password_list:
        password += ch
    return password


def fill_password():
    generated_password = generate_password()
    password_entry.delete(0,END)
    password_entry.insert(0,generated_password)
    # copy the password onto clipboard using pyperclip.copy()
    pyperclip.copy(generated_password)
    messagebox.showinfo(title="🔔", message="✔Password copied to clipboard!")
    # save it to file
    save_to_file()


# -------clearing entries from entry boxes-------------------
def clear_entries():
    password_entry.delete(0, END)
    website_entry.delete(0, END)
    username_entry.delete(0, END)
    username_entry.insert(0, MY_EMAIL)
    website_entry.focus()


# ---------------- Saving data to file ----------------------
def save_to_file():
    # get the data from the entry data
    website = website_entry.get()
    username = username_entry.get()
    password = password_entry.get()
    pyperclip.copy(password)
    messagebox.showinfo(title="🔔", message="✔Password copied to clipboard!")
    if len(password) < 8:
        messagebox.showinfo(title="⚠",message="Password is weak!")
    # validation
    if len(website) == 0 or len(username) == 0 or len(password) == 0:
        messagebox.showerror(message="Don't leave any fields empty!", title="⚠")

    # display confirmation
    else:
        # check if credentials for this data already exists, ask if they want to replace
        if check_if_exists(website):
            should_replace = messagebox.askokcancel(title="‼", message="Credentials for this website already "
                                                                       "exist. Replace?")
            # if replace, call the func
            if should_replace:
                replace_entry(website,username,password)
                messagebox.showinfo(title="✔",message=f"Changed Password for {website}")
        else:
            # open in append mode and simply append the details
            with open('passwords.txt', "a") as f:
                f.write(f"\n{website} | {username} | {password}")

    # reset entries after/or cancel entry
    clear_entries()


# --------------------------UI SETUP-------------------------
# create tkinter window object
window = Tk()
window.title("Password Keeper")
window.config(padx=5, pady=15, bg=BUBBLE)
# make the canvas , initialize, canvas contains only the image
canvas = Canvas(height=195, width=450, highlightthickness=0, bg=BUBBLE, bd=3, )

# create PhotoImage object with image file location
bg_img = PhotoImage(file='logo-190.png')

# add the logo
canvas.create_image(230, 90, image=bg_img)
canvas.grid(row=0, column=0, columnspan=3, rowspan=1)

# labels-> website,email,password and add to grid
website_label = Label(window, text="Website:", bg=BUBBLE, font=(FONT, 11, "bold"))
website_label.grid(row=1, column=0)
username_label = Label(text="Username:", bg=BUBBLE, font=(FONT, 11, "bold"))
username_label.grid(row=2, column=0)
password_label = Label(text="Password:", bg=BUBBLE, font=(FONT, 11, "bold"))
password_label.grid(row=3, column=0)

# entries
FONT = ("courier", 11, "bold")
website_entry = Entry(width=40, bd=1, font=FONT)
website_entry.grid(row=1, column=1, columnspan=2)
# places cursor in this box by default
website_entry.focus()
username_entry = Entry(width=40, bd=1, font=FONT)
username_entry.grid(row=2, column=1, columnspan=2, pady=7)
# pre populating with email
username_entry.insert(0, MY_EMAIL)
password_entry = Entry(width=22, bd=1, font=FONT)
password_entry.grid(row=3, column=1, columnspan=1, pady=7)

# buttons
FONT = ("helvetica", 9, "bold")
gen_pwd_button = Button(text="Generate Password", font=FONT,command=fill_password)
gen_pwd_button.grid(row=3, column=2)
add_button = Button(text="➕ Add", width=30, bg="#3377FF", fg='#FFFFFF', font=FONT, command=save_to_file)
add_button.grid(row=4, column=1, columnspan=2, pady=10)

window.mainloop()
