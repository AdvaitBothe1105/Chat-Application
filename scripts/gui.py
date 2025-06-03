
from pathlib import Path
import socket
import threading
import tkinter as tk
from tkinter import scrolledtext
from tkinter import messagebox
from tkinter import *
from tkinter import font
from tkinter.filedialog import askopenfilename
import sys
from pathlib import Path
from tkinter import font
import psycopg2

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage

HOST = '127.0.0.1'
PORT = 1234

client  = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


OCEAN_BLUE = '#464EB8'
WHITE = "#FFFFFF"
BLACK = "#000000"
FONT = ("Helvetica", 17)
SMALL_FONT = ("Helvetica", 13)
BUTTON_FONT = ("Helvetica",15)
PINK = "#CBACD2"

conn = psycopg2.connect(
    dbname="postgres",
    user="postgres",
    password="postgres123",
    host="localhost"
)

def add_message(message):
    message_box.config(state=tk.NORMAL)
    message_box.insert(tk.END, message + '\n')
    message_box.config(state=tk.DISABLED)

def connect():
    # Connect to the server
    try:
        client.connect((HOST,PORT))
        print("Succesfully connected to server")
        add_message("[SERVER] Succesfully connected to server")
        

    except:
        messagebox.showerror("Unable to connect to server {HOST}{PORT}")
        exit(0)

    username = username_label.cget("text")
    if username != '':
        client.sendall(username.encode('utf-8'))
        with conn.cursor() as cursor:
            cursor.execute("SELECT MAX(MID) FROM current_room")
            current_id = cursor.fetchone()[0]
            if current_id is None:
                current_id = 0
            next_id = current_id + 1
            cursor = conn.cursor()
            cursor.execute("INSERT INTO current_room (mid,username) VALUES ('%d','%s')" %(next_id,username,))
            conn.commit()
        update_labels()

    else:
        messagebox.showerror("Invalid username","Username cannot be empty")
        exit(0)
    add_message("[SERVER]" +username + " added to the chat")
    username_label.config(state=tk.DISABLED)
    join_button.config(state=tk.DISABLED)


    threading.Thread(target=listen_for_messages_from_server, args=(client, )).start()


def send_message():

        message = message_textbox.get()
        if message != '':
            client.sendall(message.encode())
            message_textbox.delete(0, len(message)+10)
            update_labels()
        else:
            messagebox.showerror("Empty Message","Empty message")

def delete_chat():
    username = username_label.cget("text")
    print(username)
    with conn.cursor() as cursor:
              cursor.execute("DELETE FROM CHAT WHERE sender = ('%s')" %(username))
              conn.commit()
    messagebox.showinfo("Chat History Deleted!!")
              
def listen_for_messages_from_server(client):

    while 1:

        message = client.recv(2048).decode('utf-8')
        if message != '':
            username = message.split("~")[0]         
            content = message.split("~")[1]
            add_message(f"[{username}]{content}")

        else:
            messagebox.showerror("Message recieved from the client is empty")
            
            
            
def remove_user():
    
    username = username_label.cget('text')
    if entry_9 == username:
        entry_9.delete(0)
    elif entry_8 == username:
        entry_8.delete(0)
    elif entry_7 == username:
        entry_7.delete(0)
    elif entry_6 == username:
        entry_6.delete(0)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM current_room WHERE username = %s", (username,))
    conn.commit()
    window.destroy()

# Function to update the labels with logged-in users
def update_labels():
    cursor = conn.cursor()
    cursor.execute("SELECT MAX(mid) FROM current_room")
    result = cursor.fetchone()[0]
    if result == 1:
    # Get the username of the first user
        cursor.execute("SELECT username FROM current_room")
        user = cursor.fetchone()
        if user:
            entry_9.config(text= user[0],font=font.Font(family="Galindo",size=14 * -1))
            
    elif result == 2:
        cursor.execute("SELECT username FROM current_room")
        users = cursor.fetchall()
        entry_9.config(text=users[0][0],font=font.Font(family="Galindo",size=14 * -1))
        entry_8.config(text=users[1][0],font=font.Font(family="Galindo",size=14 * -1))
    
    elif result == 3:
        cursor.execute("SELECT username FROM current_room")
        users = cursor.fetchall()
        entry_9.config(text=users[0][0],font=font.Font(family="Galindo",size=14 * -1))
        entry_8.config(text=users[1][0],font=font.Font(family="Galindo",size=14 * -1))
        entry_7.config(text=users[2][0],font=font.Font(family="Galindo",size=14 * -1))
    elif result == 4:
        cursor.execute("SELECT username FROM current_room")
        users = cursor.fetchall()
        entry_9.config(text=users[0][0],font=font.Font(family="Galindo",size=14 * -1))
        entry_8.config(text=users[1][0],font=font.Font(family="Galindo",size=14 * -1))
        entry_7.config(text=users[2][0],font=font.Font(family="Galindo",size=14 * -1))
        entry_6.config(text=users[3][0],font=font.Font(family="Galindo",size=14 * -1))
            
        


button_image_1 = None
button_image_2 = None
button_image_3 = None
button_image_4 = None
button_image_5 = None
button_image_6 = None
button_image_7 = None
button_image_8 = None
button_image_9 = None
button_image_10 = None
button_image_11 = None
button_image_12 = None
button_image_13 = None
button_image_14 = None
button_image_15 = None
button_image_16 = None

def add_emoji():
    OUTPUT_PATH = Path(__file__).parent
    ASSETS_PATH = Path(r"builds\Build for Emojis\assets\frame0")
    emo = Toplevel()

    emo.geometry("300x300")
    emo.configure(bg = "#EAE1EE")

    def relative_to_assets(path: str) -> Path:
        return ASSETS_PATH / Path(path)





    canvas = Canvas(
        emo, bg = "#EAE1EE", height = 300, width = 300, bd = 0, highlightthickness = 0, relief = "ridge"
    )

    canvas.place(x = 0, y = 0)
    canvas.create_text(
        100.0, 12.0, anchor="nw", text="EMOJIS", fill="#FFFFFF", font=font.Font(family="Galindo",size=20 * -1,weight="bold")
    )

    global button_image_1
    button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
    button_1 = tk.Button(
        emo, image=button_image_1, borderwidth=0, highlightthickness=0, text="😊", command=lambda: button_click(1), relief="flat"
    )
    button_1.place(
        x=26.016693115234375, y=52.0, width=42.983306884765625, height=45.0
    )

    global button_image_2
    button_image_2= PhotoImage(
        file=relative_to_assets("button_2.png"))
    button_2 = Button(
        emo, image=button_image_2, borderwidth=0, highlightthickness=0, text="😍", command=lambda: button_click(2), relief="flat"
    )
    button_2.place(
        x=229.0, y=52.0, width=42.983306884765625, height=45.0
    )

    global button_image_3
    button_image_3 = PhotoImage(
        file=relative_to_assets("button_3.png"))
    button_3 = Button(
        emo, image=button_image_3, borderwidth=0, highlightthickness=0, text="😎", command=lambda: button_click(3), relief="flat"
    )
    button_3.place(
        x=161.0, y=52.0, width=42.983306884765625, height=45.0
    )

    global button_image_4
    button_image_4  = PhotoImage(
        file=relative_to_assets("button_4.png"))
    button_4 = Button(
        emo, image=button_image_4, borderwidth=0, highlightthickness=0, text="😭", command=lambda: button_click(4), relief="flat"
    )
    button_4.place(
        x=93.98330688476562, y=112.0, width=42.983306884765625, height=45.0
    )

    global button_image_5
    button_image_5 = PhotoImage(
        file=relative_to_assets("button_5.png"))
    button_5 = Button(
        emo, image=button_image_5, borderwidth=0, highlightthickness=0, text="🤭", command=lambda: button_click(5), relief="flat"
    )
    button_5.place(
        x=26.0,
        y=112.0,
        width=42.983306884765625,
        height=45.0
    )

    global button_image_6
    button_image_6  = PhotoImage(
        file=relative_to_assets("button_6.png"))
    button_6 = Button(
        emo, image=button_image_6, borderwidth=0, highlightthickness=0, text="😡", command=lambda: button_click(6), relief="flat"
    )
    button_6.place(
        x=228.98330688476562, y=112.0, width=42.983306884765625, height=45.0
    )

    global button_image_7
    button_image_7= PhotoImage(
        file=relative_to_assets("button_7.png"))
    button_7 = Button(
        emo, image=button_image_7, borderwidth=0, highlightthickness=0, text="🤥", command=lambda: button_click(7), relief="flat"
    )
    button_7.place(
        x=160.98330688476562, y=112.0, width=42.983306884765625, height=45.0
    )

    global button_image_8
    button_image_8 = PhotoImage(
        file=relative_to_assets("button_8.png"))
    button_8 = Button(
        emo, image=button_image_8, borderwidth=0, highlightthickness=0, text="💀", command=lambda: button_click(8), relief="flat"
    )
    button_8.place(
        x=94.0, y=176.0, width=42.983306884765625, height=45.0
    )

    global button_image_9
    button_image_9 = PhotoImage(
        file=relative_to_assets("button_9.png"))
    button_9 = Button(
        emo, image=button_image_9, borderwidth=0, highlightthickness=0, text="😱", command=lambda: button_click(9), relief="flat"
    )
    button_9.place(
        x=26.016693115234375, y=176.0, width=42.983306884765625, height=45.0
    )

    global button_image_10
    button_image_10 = PhotoImage(
        file=relative_to_assets("button_10.png"))
    button_10 = Button(
        emo, image=button_image_10, borderwidth=0, highlightthickness=0, text="😈", command=lambda: button_click(10), relief="flat"
    )
    button_10.place(
        x=229.0, y=176.0, width=42.983306884765625, height=45.0
    )

    global button_image_11
    button_image_11 = PhotoImage(
        file=relative_to_assets("button_11.png"))
    button_11 = Button(
        emo, image=button_image_11, borderwidth=0, highlightthickness=0, text="😷", command=lambda: button_click(11), relief="flat"
    )
    button_11.place(
        x=161.0, y=176.0, width=42.983306884765625, height=45.0
    )

    global button_image_12
    button_image_12 = PhotoImage(
        file=relative_to_assets("button_12.png"))
    button_12 = Button(
        emo, image=button_image_12, borderwidth=0, highlightthickness=0, text="😘", command=lambda: button_click(12), relief="flat"
    )
    button_12.place(
        x=93.98330688476562, y=236.0, width=42.983306884765625, height=45.0
    )

    global button_image_13
    button_image_13= PhotoImage(
        file=relative_to_assets("button_13.png"))
    button_13 = Button(
        emo, image=button_image_13, borderwidth=0, highlightthickness=0, text="😇", command=lambda: button_click(13), relief="flat"
    )
    button_13.place(
        x=26.0, y=236.0, width=42.983306884765625, height=45.0
    )

    global button_image_14
    button_image_14 = PhotoImage(
        file=relative_to_assets("button_14.png"))
    button_14 = Button(
        emo, image=button_image_14, borderwidth=0, highlightthickness=0, text="🤑", command=lambda: button_click(14), relief="flat"
    )
    button_14.place(
        x=228.98330688476562, y=236.0, width=42.983306884765625, height=45.0
    )

    global button_image_15
    button_image_15 = PhotoImage(
        file=relative_to_assets("button_15.png"))
    button_15 = Button(
        emo, image=button_image_15, borderwidth=0, highlightthickness=0, text="😞", command=lambda: button_click(15), relief="flat"
    )
    button_15.place(
        x=160.98330688476562, y=236.0, width=42.983306884765625, height=45.0
    )

    global button_image_16
    button_image_16 = PhotoImage(
        file=relative_to_assets("button_16.png"))
    button_16 = Button(
        emo, image=button_image_16, borderwidth=0, highlightthickness=0, text="😅", command=lambda: button_click(16), relief="flat"
    )
    button_16.place(
        x=95.0, y=52.0, width=42.0, height=45.0
    )
    emo.resizable(False, False)
    
    def button_click(button_num):
            if button_num == 1:
                emoji = button_1.cget("text")
                message_textbox.insert(tk.END, emoji)


            elif button_num == 2:
                emoji = button_2.cget("text")
                message_textbox.insert(tk.END, emoji)


            elif button_num == 3:
                emoji = button_3.cget("text")
                message_textbox.insert(tk.END, emoji)


            elif button_num == 4:
                emoji = button_4.cget("text")
                message_textbox.insert(tk.END, emoji)

            elif button_num == 5:
                emoji = button_5.cget("text")
                message_textbox.insert(tk.END, emoji)

            elif button_num == 6:
                emoji = button_6.cget("text")
                message_textbox.insert(tk.END, emoji)

            elif button_num == 7:
                emoji = button_7.cget("text")
                message_textbox.insert(tk.END, emoji)
            elif button_num == 8:
                emoji = button_8.cget("text")
                message_textbox.insert(tk.END, emoji)

            elif button_num == 9:
                emoji = button_9.cget("text")
                message_textbox.insert(tk.END, emoji)

            elif button_num == 10:
                emoji = button_10.cget("text")
                message_textbox.insert(tk.END, emoji)

            elif button_num == 11:
                emoji = button_11.cget("text")
                message_textbox.insert(tk.END, emoji)

            elif button_num == 12:
                emoji = button_12.cget("text")
                message_textbox.insert(tk.END, emoji)

            elif button_num == 13:
                emoji = button_13.cget("text")
                message_textbox.insert(tk.END, emoji)

            elif button_num == 14:
                emoji = button_14.cget("text")
                message_textbox.insert(tk.END, emoji)

            elif button_num == 15:
                emoji = button_15.cget("text")
                message_textbox.insert(tk.END, emoji)

            elif button_num == 16:
                emoji = button_16.cget("text")
                message_textbox.insert(tk.END, emoji)

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = Path(r"builds\Build for Chat Window\assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH_FOR_FAQ = Path(r"builds\Build for FAQ Page\assets\frame0")

image_image_1_faq = None
button_image_1_faq = None
button_image_2_faq = None
button_image_3_faq = None



def display_faq():
    adar = Toplevel()

    adar.geometry("600x600")
    adar.configure(bg = "#EAE2EE")
    adar.resizable(False,False)
    
    
    def relative_to_assets_for_faq(path: str) -> Path:
        return ASSETS_PATH_FOR_FAQ / Path(path)

    def how_ans():
        if label3.cget("text"):
            label3.config(text="")
        else:
            label3.config(text="Yes, your chat history is usually saved unless you manually delete it. \n You can access your chat history by scrolling up in the chat window  \n or searching for specific messages using the search bar.", font=font.Font(family="Galindo",size=14 * -1), pady=10)
    def his_ans():
        if label2.cget("text"):
            label2.config(text="")
        else:
            label2.config(text="Yes, most chat applications encrypt your messages to ensure privacy and \n security. Encryption algorithms are used to encode your messages before they\n  are sent over the internet, making it difficult for unauthorized \n  users to intercept and read them.",font=font.Font(family="Galindo",size=14 * -1), pady=10)
    def con_ans():
        if label4.cget("text"):
            label4.config(text="")
        else:
            label4.config(text="If you're interested in contributing to the development of the chat application \n or reporting bugs, you can usually find the source code on a version control \n  platform like GitHub.", font=font.Font(family="Galindo",size=14 * -1),pady=10)

    canvas = Canvas(
    adar, bg = "#EAE2EE", height = 600, width = 600, bd = 0, highlightthickness = 0, relief = "ridge"
    )

    canvas.place(x = 0, y = 0)
    global image_image_1_faq
    image_image_1_faq = PhotoImage(
        file=relative_to_assets_for_faq("image_1.png"))
    image_1 = canvas.create_image(
        300.0, 300.0, image=image_image_1_faq
    )
    

    canvas.create_text(
        10.0, 22.0, anchor="nw", text="FREQUENTLY ASKED QUESTIONS\n                     (FAQ)", fill="#FFFFFF", font=font.Font(family="Galindo",size=32 * -1,weight="bold")
    )

    global button_image_1_faq
    button_image_1_faq = PhotoImage(
        file=relative_to_assets_for_faq("button_1.png"))
    button_1 = Button(
        adar, image=button_image_1_faq, borderwidth=0, highlightthickness=0, command=his_ans, relief="flat"
    )
    button_1.place(
        x=6.0, y=269.0, width=589.0, height=65.0
    )
    label2 = tk.Label(adar, text="", font=FONT ,bg=PINK, fg= BLACK) 
    label2.place(
        x=6.0, y=345.0, width= 589.0
    )
    
    global button_image_2_faq
    button_image_2_faq = PhotoImage(
        file=relative_to_assets_for_faq("button_2.png"))
    button_2 = Button(
        adar, image=button_image_2_faq, borderwidth=0, highlightthickness=0, command=how_ans, relief="flat"
    )
    button_2.place(
        x=6.0, y=124.0, width=589.0, height=46.0
    )
    label3 = tk.Label(adar, text="", font=FONT ,bg=PINK, fg= BLACK) 
    label3.place(
        x=6.0, y=180.0, width= 589.0
    )
    
    

    global button_image_3_faq
    button_image_3_faq = PhotoImage(
        file=relative_to_assets_for_faq("button_3.png"))
    button_3 = Button(
        adar, image=button_image_3_faq, borderwidth=0, highlightthickness=0, command=con_ans, relief="flat"
    )
    button_3.place(
        x=6.0, y=452.0, width=589.0, height=67.0
    )
    label4 = tk.Label(adar, text="", font=FONT ,bg=PINK, fg= BLACK) 
    label4.place(
        x=6.0, y=520.0, width= 589.0
    )

class Application:
    def __init__(self):


        self.instructions = [
            "Step 1: Open the application.",
            "Step 2: Enter your username.",
            "Step 3: Click on the 'JOIN' button.",
            "Step 4: Type your desired message in the text box provided at the bottom of the screen.",
            "Step 5: After typing the message you have the option to add emojis by clicking on the 😊 button ",
            "Step 6: Click on the 'SEND' button to send you message.",
            "Step 7: There is a button for FAQ's as well if you're stuck at any stage."

        ]
        self.current_step = 0

        self.show_message_box()

    def show_message_box(self):
        response = messagebox.askokcancel("Welcome", "Welcome to the application. Click 'Next' to see step-by-step instructions.")

        if response:
            self.show_next_step()
        else:
            self.current_step = 6
            self.show_next_step()

    def show_next_step(self):
        while (self.current_step != 7):
            if self.current_step < len(self.instructions):
                 messagebox.showinfo("Step {}".format(self.current_step + 1), self.instructions[self.current_step])
                 self.current_step += 1
            else:
                messagebox.showinfo("End of Instructions", "You have reached the end of the instructions.")


window = Tk()

window.geometry("925x650")
window.configure(bg = "#FFFFFF")


canvas = Canvas(
    window, bg = "#FFFFFF", height = 650, width = 925, bd = 0, highlightthickness = 0, relief = "ridge"
)

canvas.place(x = 0, y = 0)
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    462.0, 329.0, image=image_image_1
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    519.0, 58.5, image=entry_image_1
)
username_label = Label(
    bd=0, bg="#ACBED8", fg="#000716", text=sys.argv[1], font=font.Font(family="Galindo",size=14 * -1),highlightthickness=0
)
username_label.place(
    x=317.0, y=33.0, width=404.0, height=49.0
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    478.0, 565.5, image=entry_image_2
)
message_textbox = Entry(
    bd=0, bg="#ACBED8", fg="#000716", highlightthickness=0
)
message_textbox.place(
    x=276.0, y=540.0, width=404.0, height=49.0
)

image_1_join = PhotoImage(
    file=relative_to_assets("button_1.png"))
join_button = Button(
    image=image_1_join, borderwidth=0, highlightthickness=0, command=connect, relief="flat"
)
join_button.place(
    x=766.0, y=43.0, width=94.0, height=30.0
)

image_2_dis = PhotoImage(
    file=relative_to_assets("button_2.png"))
faq_button = Button(
    image=image_2_dis, borderwidth=0, highlightthickness=0, command=display_faq, relief="flat"
)
faq_button.place(
    x=12.0, y=506.0, width=94.0, height=30.0
)

image_3_send = PhotoImage(
    file=relative_to_assets("button_3.png"))
send_button = Button(
    image=image_3_send, borderwidth=0, highlightthickness=0, command=send_message, relief="flat"
)
send_button.place(
    x=786.0, y=545.0, width=94.0, height=30.0
)

image_4_del = PhotoImage(
    file=relative_to_assets("button_4.png"))
delete_chat_history_button = Button(
    image=image_4_del, borderwidth=0, highlightthickness=0, command=delete_chat, relief="flat"
)
delete_chat_history_button.place(
    x=117.0, y=496.0, width=129.0, height=56.0
)
image_4_leave = PhotoImage(
    file=relative_to_assets("leave.png"))
leave_room__button = Button(
    image=image_4_leave, borderwidth=0, highlightthickness=0, command=remove_user, relief="flat"
)
leave_room__button.place(
    x=43.0, y=566.0, width=129.0, height=56.0
)


entry_image_3 = PhotoImage(
    file=relative_to_assets("entry_3.png"))
entry_bg_3 = canvas.create_image(
    141.50972747802734, 62.5, image=entry_image_3
)


entry_image_4 = PhotoImage(
    file=relative_to_assets("entry_4.png"))
entry_bg_4 = canvas.create_image(
    563.0, 324.5, image=entry_image_4
)
message_box = Text(
    bd=0,
    bg="#BCD4DE", fg="#000716", highlightthickness=0
)
message_box.place(
    x=276.0, y=150.0, width=574.0, height=357.0
)

entry_image_5 = PhotoImage(
    file=relative_to_assets("entry_5.png"))
entry_bg_5 = canvas.create_image(
    132.0, 148.5, image=entry_image_5
)

entry_image_6 = PhotoImage(
    file=relative_to_assets("entry_6.png"))
entry_bg_6 = canvas.create_image(
    136.0, 438.5, image=entry_image_6
)
entry_6 = Label(
    bd=0, bg="#D9D9D9", fg="#000716", highlightthickness=0
)
entry_6.place(
    x=30.0, y=420.0, width=190.0, height=25.0
)

entry_image_7 = PhotoImage(
    file=relative_to_assets("entry_7.png"))
entry_bg_7 = canvas.create_image(
    136.0, 357.5, image=entry_image_7
)
entry_7 = Label(
    bd=0, bg="#D9D9D9", fg="#000716", highlightthickness=0
)
entry_7.place(
    x=30.0, y=344.0, width=190.0, height=25.0
)

entry_image_8 = PhotoImage(
    file=relative_to_assets("entry_8.png"))
entry_bg_8 = canvas.create_image(
    136.0, 287.5, image=entry_image_8
)
entry_8 = Label(
    bd=0, bg="#D9D9D9", fg="#000716", highlightthickness=0
)
entry_8.place(
    x=30.0, y=274.0, width=190.0, height=25.0
)

entry_image_9 = PhotoImage(
    file=relative_to_assets("entry_9.png"))
entry_bg_9 = canvas.create_image(
    136.0, 216.5, image=entry_image_9
)
entry_9 = Label(
    bd=0, bg="#D9D9D9", fg="#000716", highlightthickness=0
)
entry_9.place(
    x=30.0, y=203.0, width=190.0, height=25.0
)

image_5_emo = PhotoImage(
    file=relative_to_assets("button_5.png"))
emoji_button = Button(
    image=image_5_emo, borderwidth=0, highlightthickness=0, command=add_emoji, relief="flat"
)
emoji_button.place(
    x=719.0, y=540.0, width=47.0, height=52.0
)

def main():
    Application()
    window.mainloop()
window.resizable(False, False)


if __name__ == '__main__':
    main()

