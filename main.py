from tkinter import *

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

class Generate_Password():
    pass

# ---------------------------- SAVE PASSWORD ------------------------------- #

class Save_Password():
    combination_of_entries = ""
    data_file = open("password_data.txt", "a")
    combination_of_entries += website_name_variable.get()
    combination_of_entries += email_entry.get()
    combination_of_entries += password_entry.get()
    data_file.write(f"{combination_of_entries}")
    data_file.close()
    #
    # data_file = open("password_data.txt", "a")
    # data_file.write(f"{website_entry.get()}  I  {email_entry.get()}  I  {password_entry.get()}")
    # data_file.close()
    #



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



website_entry = Entry(width=35, textvariable=website_name_variable)
website_entry.grid(column=1, row=1, columnspan=2)
website_entry.focus()


email_entry = Entry(width=35)
email_entry.grid(column=1, row=2, columnspan=2)
email_entry.insert(0, "testing@gmail.com")

password_entry = Entry(width=21)
password_entry.grid(column=1, row=3)

save_password_button = Button(text="Add password", width=36, command=Save_Password())
save_password_button.grid(column=1, row=4, columnspan=2)


window.mainloop()