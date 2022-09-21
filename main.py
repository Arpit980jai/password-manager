from tkinter import *
from tkinter import messagebox
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

nr_letters = random.randint(8, 10)
nr_symbols = random.randint(2, 4)
nr_numbers = random.randint(2, 4)


def generate():
    password_list = []

    for char in range(nr_letters):
        password_list.append(random.choice(letters))

    for char in range(nr_symbols):
        password_list += random.choice(symbols)

    for char in range(nr_numbers):
        password_list += random.choice(numbers)

    random.shuffle(password_list)

    password = ""
    for char in password_list:
        password += char
    password_input.insert(0,password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def add():
    website=website_input.get()
    email=email_input.get()
    password=password_input.get()
    newData={
        website : {
            "email":email,
            "password":password
        }
    }
    is_empty=password!=""and email!=""and website!=""
    if is_empty:
        is_ok=messagebox.askyesno(message="Are you sure want to save ?")
    else:
        messagebox.showerror(title="Empty Feild", message="Please enter the values")

    if is_ok:
        try:
            with open("data.json",mode="r") as file:
                data=json.load(file)
        except:
            with open("data.json", mode="w") as file:
                json.dump(newData, file, indent=4)
        else:
            data.update(newData)
            with open("data.json", mode="w") as file:
                json.dump(data, file, indent=4)

        website_input.delete(0,END)
        password_input.delete(0,END)

#----------------------------------------Search----------------------------#
def search():
    website = website_input.get()
    email = email_input.get()
    password = password_input.get()
    with open("data.json","r")as file:
        searchdata=json.load(file)
        for i in searchdata:
            try:
                if i==website:
                    print(searchdata[i])
                    messagebox.showinfo(title=i,message=f"Email : {searchdata[i]['email']}\nPassword: {searchdata[i]['password']} ")

            except:
                pass


# ---------------------------- UI SETUP ------------------------------- #
window=Tk()
window.title("Password Manager")
window.config(padx=50,pady=50)




canvas = Canvas(width=200, height=200,highlightthickness=0,)
logo_img=PhotoImage(file="logo.png")
canvas.create_image(100,100,image=logo_img,)
canvas.grid(column=1,row=0)

website=Label(text="Website: ")
website.grid(row=1,column=0)
email=Label(text="Email/Username: ")
email.grid(row=2,column=0)
password=Label(text="Password: ")
password.grid(row=3,column=0)

website_input=Entry(width=24)
website_input.grid(row=1,column=1,columnspan=2)
website_input.focus()
email_input=Entry(width=35)
email_input.grid(row=2,column=1,columnspan=2)
email_input.insert(0,"arpit980jaiswal@gmail.com")

password_input=Entry(width=24)
password_input.grid(row=3,column=1)

generate=Button(text="Generate",command=generate)
generate.grid(row=3,column=2)
search=Button(text="Search",command=search)
search.grid(row=1,column=2)

add=Button(text="Add",width=31,command=add)
add.grid(row=4,column=1,columnspan=2)

window.mainloop()