import tkinter as tk
window= tk.Tk()

press=1

score= 0
 
def click(event):
    label= tk.Label(text=f"Score:{score}")
    label.pack()

button = tk.Button(
    text=f"+{press}",
    width=3,
    height=2,
    bg="blue",
    fg="yellow")

button.bind("<Button-1>", click)

label= tk.Label(text=f"Score:{score}")

button.pack()
label.pack()
window.mainloop()
