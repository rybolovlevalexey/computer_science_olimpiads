import tkinter as tk

window = tk.Tk()
greeting = tk.Label(text="Привет, Tkinter!")
greeting.pack()
button = tk.Button(
    text="Нажми на меня!",
    width=25,
    height=10,
    bg="white",
    fg="black",
)
button.pack()
entry = tk.Entry(fg="black", bg="white", width=50)
entry.pack()
window.mainloop()