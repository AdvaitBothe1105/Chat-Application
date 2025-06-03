

from pathlib import Path
from tkinter import font
import sys


# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
import time
import pyotp
from email.message import EmailMessage
import smtplib
import subprocess



# print(totp.now())

# input_code = input("Enter your code:")
# print(totp.verify(input_code))


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = Path(r"builds\Build for e-mail Page\assets\frame0")

username = sys.argv[1]

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)
def on_button_click():
    recipient = entry_1.get()
    window.destroy()
    subprocess.run([sys.executable, "./scripts/Auth2.py",recipient,username])
    # message = totp.now()
    # send_email(message, recipient)



window = Tk()

window.geometry("400x400")
window.configure(bg = "#EAE2EE")


canvas = Canvas(
    window, bg = "#EAE2EE", height = 400, width = 400, bd = 0, highlightthickness = 0, relief = "ridge"
)

canvas.place(x = 0, y = 0)
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    206.0, 235.0, image=image_image_1
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1, borderwidth=0, highlightthickness=0, command=on_button_click, relief="flat"
)
button_1.place(
    x=147.0, y=136.0, width=94.0, height=30.0 )

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    200.0, 110.0, image=entry_image_1
)
entry_1 = Entry(
    bd=0, bg="#ACBED8", fg="#000716", highlightthickness=0
)
entry_1.place(
    x=42.0, y=93.0, width=316.0, height=32.0
)

canvas.create_text(
    85.0, 25.0, anchor="nw", text="AUTHENTICATION", fill="#FFFFFF", font=font.Font(family="Galindo",size=24 * -1,weight="bold")
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    203.5, 72.0, image=entry_image_2
)

window.resizable(False, False)
window.mainloop()
