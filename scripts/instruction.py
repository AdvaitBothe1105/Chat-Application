import tkinter as tk
from tkinter import messagebox

class Application:
    def __init__(self, master):
        self.master = master
        self.master.geometry("400x300")
        self.master.title("Step-by-Step Instructions")

        self.instructions = [
            "Step 1: Open the application.",
            "Step 2: Click on the 'File' menu.",
            "Step 3: Select 'Open' from the menu.",
            "Step 4: Choose the file you want to open.",
            "Step 5: Click 'Open' to confirm.",
            "Step 6: Follow the on-screen instructions to complete the process."
        ]
        self.current_step = 0

        self.show_message_box()

    def show_message_box(self):
        response = messagebox.askokcancel("Welcome", "Welcome to the application. Click 'Next' to see step-by-step instructions.")

        if response:
            self.show_next_step()
        else:
            self.destroy()

    def show_next_step(self):
        while (self.current_step != 6):
            if self.current_step < len(self.instructions):
                 messagebox.showinfo("Step {}".format(self.current_step + 1), self.instructions[self.current_step])
                 self.current_step += 1
            else:
                messagebox.showinfo("End of Instructions", "You have reached the end of the instructions.")
                self.master.destroy()
            
        

def main():
    root = tk.Tk()
    app = Application(root)
    root.mainloop()

if __name__ == "__main__":
    main()

