import tkinter as tk


def click1(event):
    st = entry.get()
    if len(st) == 0:
        lbl = tk.Label(text='Вы ничего не ввели')
        lbl.pack()
    else:
        lbl = tk.Label(text=f'Приветствую, {st}')
        lbl.pack()


def click2(event):
    st = entry.get()
    if len(st) == 0:
        lbl = tk.Label(text='Вы ничего не ввели')
        lbl.pack()
    else:
        lbl = tk.Label(text=f'Всего доброго, {st}')
        lbl.pack()


window = tk.Tk()
window.geometry('400x400+500+500')
greeting = tk.Label(text="Запишите имя пользователя в поле для ввода")
greeting.pack()
button1 = tk.Button(
    text="Приветствие\nпользователя",
    width=15,
    height=5,
    bg="white",
    fg="black",
)
button1.bind("<Button-1>", click1)
button1.pack(side=tk.LEFT)
button2 = tk.Button(
    text="Прощание\nс пользователем",
    width=15,
    height=5,
    bg="white",
    fg="black",
)
button2.bind("<Button-1>", click2)
button2.pack(side=tk.RIGHT)
entry = tk.Entry(fg="black", bg="white", width=500)
entry.pack(side=tk.BOTTOM)
window.mainloop()