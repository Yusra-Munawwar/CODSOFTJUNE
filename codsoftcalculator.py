from tkinter import *
win = Tk()
win.geometry("380x530")
win.resizable(0, 0)
win.title("Calculator By Yusra")
win.wm_iconbitmap("C:\\Users\\Munawwar Shamim\\Downloads\\R.ico")

def click(event):
    global scvalue
    text = event.widget.cget("text")
    print(text)
    if text == "=":
        try:
            if scvalue.get().isdigit():
                value = int(scvalue.get())
            else:
                try:
                    value = eval(scvalue.get())
                except Exception:
                    value = "Error"
        except ZeroDivisionError:
            value = "Division by zero!"
        scvalue.set(value)
        win.update()
    elif text == "C":
        scvalue.set("")
        win.update()
    else:
        scvalue.set(scvalue.get() + text)
        win.update()


display_frame = Frame(win, width=300, height=50, bd=10, highlightbackground="GREY",
                      highlightcolor="BLACK", highlightthickness=2)
scvalue = StringVar()
scvalue.set("")
input_field = Entry(display_frame, font=('arial', 18, 'bold'), textvariable=scvalue, width=50,
                    bg="#eee", bd=5,highlightcolor="grey", justify=RIGHT)
input_field.pack(ipady=10)
display_frame.pack(side=TOP)

button_frame = Frame(win, width=300, height=395, bd=10, highlightbackground="GREY",
                     highlightcolor="black", highlightthickness=2)

button_labels = [
    ("C", "%", "/", "*"),
    ("7", "8", "9", "-"),
    ("4", "5", "6", "+"),
    ("1", "2", "3", "."),
    ("(", "0", ")", "=")]

for row_labels in button_labels:
    row_frame = Frame(button_frame)
    row_frame.pack(side=TOP)

    for label in row_labels:
        button = Button(row_frame, text=label, padx=20, pady=20, width=5, height=2, font= ('arial', 10, 'bold'),
                        bd=5, highlightcolor= "grey", cursor="hand2")
        button.bind("<Button-1>", click)
        button.pack(side=LEFT)

button_frame.pack(side=BOTTOM)
win.mainloop()