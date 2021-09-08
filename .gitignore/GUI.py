import tkinter as tk
from tkinter import *
from tkinter import messagebox


root = tk.Tk()
root.title('roPresence python')

window_width = 300
window_height = 200

# get the screen dimension
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# find the center point
center_x = int(screen_width/2 - window_width / 2)
center_y = int(screen_height/2 - window_height / 2)

# set the position of the window to the center of the screen
root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')




root.geometry('600x400+50+50')
root.resizable(False, False)
#root.iconbitmap('../screenshots/uploads/address.ico') # once I get a .ico logo tho

def subscribe():
    return tk.messagebox.showinfo('roPresence is now running, you can now minimize this application')


b = tk.Button(text ="Start", command=subscribe, bg="#393B3D" ,background="#393B3D", relief="sunken", padx=5, pady=10).place(relx=0.5, rely=0.5, anchor=CENTER)

root.mainloop()