from time import strftime
from tkinter import Label, Tk

window = Tk()
window.title("Clock")
window.geometry("350x155")
window.configure(bg="black")
window.resizable(False, False)


clock_label = Label(window, bg="black", fg="cyan", font=("ds-digital", 50), relief='flat')
clock_label.place(x=0, y=0)


def update_label():
    current_time = strftime("   %a %d %b %y\n \n  %I:%M:%S  %p")
    clock_label.configure(text=current_time)
    clock_label.after(80, update_label)



update_label()
window.mainloop()
