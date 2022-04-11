from tkinter import *
from tkinter import messagebox

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def Generate_Password():
    pass

# ---------------------------- SAVE PASSWORD ------------------------------- #

def Save_Password():
    website_name = website_name_variable.get()
    email_name = email_entry.get()
    password_name = password_entry_variable.get()

    if len(website_name) == 0 or len(email_name) == 0 or len(password_name) == 0:
        messagebox.showinfo(title="Error 404", message="Please check for empty fields and fill them.")

    else:
        is_ok = messagebox.askokcancel(title=website_name, message=f"These are the details entered: "
                                                                          f"\nEmail: {email_name} "
                                                                          f"\nPassword: {password_name} "
                                                                          f"\nIs it ok to save? ")
        if is_ok:
            data_file = open("password_data.txt", "a")
            data_file.write(f"\n{website_name}  |  {email_name}  |  {password_name}")
            data_file.close()
            website_entry.delete(0, END)
            email_entry.delete(0, END)
            password_entry.delete(0, END)



# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Generator")
window.config(padx=50, pady=50, bg="white")

canvas = Canvas(width=200, height=200, bg="white", highlightthickness=0)
lock_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_image)
canvas.grid(column=1, row=0)

website_label = Label(text="Website:", bg="white",  font=("Arial", 18, "bold"))
website_label.grid(column=0, row=1)

email_label = Label(text="Email/Username:", bg="white",  font=("Arial", 18, "bold"))
email_label.grid(column=0, row=2)

password_label = Label(text="Password:", bg="white",  font=("Arial", 18, "bold"))
password_label.grid(column=0, row=3)

generate_password_button = Button(text="Generate password", command=Generate_Password)
generate_password_button.grid(column=2, row=3)


website_name_variable = StringVar()
website_entry = Entry(width=35, textvariable=website_name_variable)
website_entry.grid(column=1, row=1, columnspan=2)
website_entry.focus()

email_entry_variable = StringVar()
email_entry = Entry(width=35, textvariable=email_entry_variable)
email_entry.grid(column=1, row=2, columnspan=2)
email_entry.insert(0, "testing@gmail.com")

password_entry_variable = StringVar()
password_entry = Entry(width=21, textvariable=password_entry_variable)
password_entry.grid(column=1, row=3)

save_password_button = Button(text="Add password", width=36, command=Save_Password)
save_password_button.grid(column=1, row=4, columnspan=2)


window.mainloop()