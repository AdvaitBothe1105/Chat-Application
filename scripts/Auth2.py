
from pathlib import Path
from tkinter import font
import sys
import pyotp
import subprocess
from tkinter import messagebox
from email.message import EmailMessage
import smtplib
import psycopg2
import time



# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = Path(r"builds\Build for OTP Page\assets\frame0")

conn = psycopg2.connect(
    dbname="postgres",
    user="postgres",
    password="postgres123",
    host="localhost"
)



def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def auth_user_and_open():
    input_code = entry_1.get()
    print(totp.now())
    username = sys.argv[2]
    email = sys.argv[1]
    password = username + "ww12" 
    if totp.verify(input_code):
        with conn.cursor() as cursor:
              cursor.execute("SELECT MAX(UID) FROM USERN")
              current_id = cursor.fetchone()[0]
              if current_id is None:
                  current_id = 0
              next_id = current_id + 1
                   
              cursor.execute("INSERT INTO USERN (UID,USERNAME,EMAIL,EPASSWORD) VALUES ('%d','%s','%s','%s')" %(next_id,username,email,password))
              conn.commit()
        window.destroy()
        subprocess.run([sys.executable, './scripts/gui.py',sys.argv[2]])
    else:
        messagebox.showerror("Incorrect OTP. Please try again")

        
        


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

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    199.0, 124.0, image=entry_image_1
)
entry_1 = Entry(
    bd=0, bg="#ACBED8", fg="#000716", highlightthickness=0
)
entry_1.place(
    x=41.0, y=107.0, width=316.0, height=32.0
)

canvas.create_text(
    76.0,
    17.0, anchor="nw", text="AUTHENTICATION", fill="#FFFFFF", font=font.Font(family="Galindo",size=24 * -1,weight="bold"))

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=auth_user_and_open,
    relief="flat"
)
button_1.place(
    x=147.0, y=146.0, width=94.0, height=37.0
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    199.5, 78.5, image=entry_image_2
)

window.resizable(False, False)
def send_email(message,recipient):
    me = "wildwhispers12@gmail.com"

    msg = EmailMessage()
    msg['Subject'] = "New Message"
    msg['From'] = me
    msg['To'] = recipient
    msg.set_content(f"""\
    Greetings from the Wild Whispers team! 🌿

    Thank you for choosing Wild Whispers for your authentication needs. Your One-Time Password (OTP) is:

    {message}

    Please use this OTP to complete your authentication process. If you did not request this OTP, please ignore this message.

    If you have any questions or need further assistance, feel free to reach out to us.

    Best Regards,
    The Wild Whispers Team
    """)

    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.login("wildwhispers12@gmail.com", "qkoy lnqv pozt qysa")
    server.send_message(msg)
    server.quit()
    window.mainloop()


key = "WildWhispers"
totp = pyotp.TOTP(key)
message = totp.now()
recipient = sys.argv[1]
send_email(message,recipient)






