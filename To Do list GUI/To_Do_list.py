from tkinter import *
main_window = Tk()
main_window.title("To Do")
main_label = Label(main_window, text="Enter Tasks:" , relief="solid", bd=3)
main_label.grid(row=0, column=0, padx=3)
tasks = []
check_buttons = []
i = 0
Row = 1


def main_entry_function(event=None):
    global i
    global Row
    info = main_entry.get()
    main_entry.delete(0, END)
    tasks.append("l{}".format(i))
    tasks[i] = Label(main_window, text=str(info), relief="solid", bd=3)
    tasks[i].grid(row=Row, column=0, pady=3)
    check_buttons.append("c{}".format(i))
    check_buttons[i] = Checkbutton(main_window, onvalue=1, offvalue=0, height=1, width=1, bd=3, relief="solid")
    check_buttons[i].grid(row=Row, column=1, pady=3)
    b = check_buttons[i]
    ind = check_buttons.index(b)
    row = check_buttons[ind].grid_info()['row']
    check_buttons[ind].config(command=lambda : [check_buttons[ind].destroy(), Label(main_window, text="Done! \u2713", relief="solid", bd=3, bg="lime").grid(row=row, column=1)])
    i += 1
    Row += 1


main_entry = Entry(main_window, relief="solid", bd=3, width=40)
main_entry.bind("<Return>", main_entry_function)
main_entry.grid(row=0, column=1)
main_window.mainloop()
