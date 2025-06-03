
from pathlib import Path
from tkinter import font

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
import subprocess
import sys

def run_other_script():
    # Run the other Python script using subprocess
    data = entry_1.get()
    print(data)
    window.destroy()
    subprocess.run([sys.executable, './scripts/Auth1.py',data])
    
def run_login():
    data2 = entry_1.get()
    window.destroy()
    subprocess.run([sys.executable, './scripts/Login.py',data2])
  


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = Path(r"assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("700x700")
window.configure(bg = "#F8F0FB")

canvas = Canvas(
    window,
    bg = "#F8F0FB",
    height = 700,
    width = 700,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
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
    350.5,
    187.0, image=entry_image_1
)
entry_1 = Entry(
    bd=0, bg="#ACBED8", fg="#000716", highlightthickness=0
)



entry_1.place(
    x=79.0,
    y=164.0,
    width=543.0,
    height=44.0
)


button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=run_other_script,
    relief="flat"
)
button_1.place(
   x=115.0,
    y=240.0,
    width=204.0,
    height=34.0
)
button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=run_login,
    relief="flat"
)
button_2.place(
    x=384.0,
    y=243.0,
    width=204.0,
    height=34.0
)

canvas.create_text(
    63.0,
    115.0,
    anchor="nw",
    text="Nature's calling! What's your wild username?",
    fill="#FFFFFF",
    font=font.Font(family="Galindo",size=20 * -1,weight="bold")
)
canvas.create_text(
    384.0,
    211.0,
    anchor="nw",
    text="Already registered?",
    fill="#FFFFFF",
    font=font.Font(family="Galindo",size=20 * -1,weight="bold")
)

canvas.create_text(
    63.0,
    34.0,
    anchor="nw",
    text="WILD WHISPERS",
    fill="#FFFFFF",
    font=font.Font(family="Galindo",size=65 * -1,weight="bold")
)


window.resizable(False, False)
window.mainloop()
