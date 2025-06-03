
from pathlib import Path
from tkinter import font


# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
import psycopg2
import subprocess
import sys
from tkinter import messagebox




conn = psycopg2.connect(
    dbname="postgres",
    user="postgres",
    password="postgres123",
    host="localhost"
)


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = Path(r"builds\Build for Login Page\assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def check_user_and_open():
    username = entry_2.get()
    password = entry_1.get()
    
    with conn.cursor() as cursor:
              cursor.execute("SELECT * FROM USERN WHERE username =%s AND epassword = %s", (username,password))
              result = cursor.fetchone()
              if result:
                      window.destroy()  
                      subprocess.run([sys.executable, './scripts/gui.py',username])
              else:
                  messagebox.showerror("Please enter valid e-mail and Password")
              conn.commit()

def show_password():
    password = entry_1.get()
    messagebox.showinfo("Masked Password", password)


window = Tk()

window.geometry("700x700")
window.configure(bg = "#F8F0FB")


canvas = Canvas(
    window, bg = "#F8F0FB", height = 700, width = 700, bd = 0, highlightthickness = 0, relief = "ridge"
)

canvas.place(x = 0, y = 0)
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    368.0, 386.0, image=image_image_1
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    506.0, 174.0, image=entry_image_1
)
entry_1 = Entry(
    bd=0, bg="#ACBED8", fg="#000716", show="*", highlightthickness=0
)
entry_1.place(
    x=401.0, y=151.0, width=210.0, height=44.0
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    174.0, 174.0, image=entry_image_2
)
entry_2 = Entry(
    bd=0, bg="#ACBED8", fg="#000716", highlightthickness=0
)
entry_2.place(
    x=78.0, y=151.0, width=192.0, height=44.0
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button( image=button_image_1, borderwidth=0, highlightthickness=0, command=check_user_and_open, relief="flat"
)
button_1.place(
    x=228.0, y=252.0, width=204.0, height=34.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2, borderwidth=0, highlightthickness=0, command=show_password, relief="flat"
)
button_2.place(
    x=404.0, y=207.0, width=204.0, height=34.0
)

canvas.create_text(
    67.0, 2.0, anchor="nw", text="WILD WHISPERS", fill="#FFFFFF", font=font.Font(family="Galindo",size=65 * -1,weight="bold")
)

canvas.create_text(
    68.0, 104.0, anchor="nw", text="Username", fill="#FFFFFF", font=font.Font(family="Galindo",size=20 * -1,weight="bold")
)

canvas.create_text(
    392.0, 89.0, anchor="nw", text="Password (Your password \n is your username + ww12)", fill="#FFFFFF", font=font.Font(family="Galindo",size=20 * -1,weight="bold")
)



window.resizable(False, False)
window.mainloop()
