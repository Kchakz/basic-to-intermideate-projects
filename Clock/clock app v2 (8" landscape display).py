from time import strftime
import tkinter as tk
from tkinter import Label, Tk


def show_frame(frame):
    frame.tkraise()


window = tk.Tk()
window.geometry("430x90")
window.resizable(False, False)
window.title('Clock')

window.rowconfigure(0, weight=1)
window.columnconfigure(0, weight=1)



frame1 = tk.Frame(window, bg='black')
frame2 = tk.Frame(window, bg='black')

for frame in(frame1, frame2):
    frame.grid(row=0, column=0, sticky='nesw')


#=========Time=========
current_time = strftime("%H:%M               ")

frame1_title = tk.Label(frame1, text=current_time, bg="black", fg="cyan", font=("ds-digital", 85), relief='flat')
show_frame(frame1)
frame1_title.pack()
frame1.place(x=0, y=0)
frame1.anchor='CENTER'


def update_label():
    current_time = strftime("  %I:%M %p       ")
    frame1_title.configure(text=current_time)
    frame1_title.after(80, update_label)


update_label()

frame1_btn = tk.Button(frame1, text='Date', command=lambda:show_frame(frame2))
frame1_btn.pack()
frame1_btn.place(x=370, y=30)

#===Frame 2===

current_time = strftime("%a  %b  %y         ")

frame2_title = tk.Label(frame2, text=current_time, bg="black", fg="cyan", font=("ds-digital", 75), relief='flat')
show_frame(frame2)
frame2_title.pack()
frame2.place(x=0, y=0)
frame2.anchor='CENTER'

frame2_btn = tk.Button(frame2, text='Time', command=lambda:show_frame(frame1))
frame2_btn.pack()
frame2_btn.place(x=370, y=30)



window.mainloop()
