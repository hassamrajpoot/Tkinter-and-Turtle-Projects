from tkinter import *
from random import choice
main_window = Tk()
main_window.title("MCQs")
main_window.config(bg="yellow")
num_of_mcqs = 0
the_number = 0
l1 = Label(main_window, text="Enter number of MCQs :", relief="solid")
l1.grid(row=0, column=0, padx=4)
e1 = Entry(main_window, bd=3, width=7)
e1.grid(row=0, column=1, padx=3)
l2 = Label(main_window, text="Enter number:", relief="solid")
l2.grid(row=1, column=0, padx=4)
e2 = Entry(main_window, bd=3, width=7)
e2.grid(row=1, column=1, padx=3)
correct = 0
incorrect = 0


def capture_num_of_mcqs():
    global num_of_mcqs
    num_of_mcqs = int(e1.get())
    e1.delete(0, END)


entry_widgets = []
answers = []
my_answers = []


def questions():
    to_choose_from = [j for j in range(1, 100)]
    for j in range(3, 3+num_of_mcqs):
        entry_widgets.append("e{}".format(j))
    for i in range(3, 3+num_of_mcqs):
        random_num = choice(to_choose_from)
        answers.append(the_number * random_num)
        Label(main_window, text="{} * {} = ?".format(the_number, random_num), relief="solid").grid(row=i, column=0, padx=4, pady=3)
    k = 0
    while k != len(entry_widgets):
        entry_widgets[k] = Entry(main_window, bd=3, width=7)
        entry_widgets[k].grid(row=k+3, column=1)
        k += 1
    global b3
    b3 = Button(main_window, text="Check", bd=3, command=capturing_answers, bg="aquamarine2", relief="solid")
    b3.grid(row=3 + num_of_mcqs + 1, column=1, padx=3)


def capturing_answers():
    l = 0
    b3.config(state="disabled")
    global correct
    global incorrect
    while l != len(entry_widgets):
        entry = entry_widgets[l]
        if entry.get() == "":
            my_answers.append(0)
        else:
            my_answers.append(int(entry.get()))
        l += 1
    m = 0
    while m != len(entry_widgets):
        if answers[m] == my_answers[m]:
            correct += 1
        elif answers[m] != my_answers[m]:
            incorrect += 1
        m += 1
    Label(main_window, text="Correct :{}   Incorrect :{}".format(correct, incorrect), relief="solid").grid(row=3+num_of_mcqs+3, column=0)
    Label(main_window, text="Total :{}".format(num_of_mcqs), relief="solid").grid(row=3+num_of_mcqs+3, column=1)

    def destroying():
        main_window.destroy()
    exit_button = Button(main_window, text="Exit", bd=3, command=destroying, relief="solid", bg="red", width=4)
    exit_button.grid(row=3+num_of_mcqs+3, column=2)


def starting():
    global the_number
    global random_num
    the_number = int(e2.get())
    e2.delete(0, END)
    e1.config(state="disabled")
    b1.config(state="disabled")
    e2.config(state="disabled")
    b2.config(state="disabled")
    e2.delete(0, END)
    questions()


b1 = Button(main_window, text=" OK  ", bd=3, command=capture_num_of_mcqs, bg="aquamarine2", relief="solid")
b1.grid(row=0, column=2, padx=3)
b2 = Button(main_window, text="Start", bd=3, command=starting, bg="aquamarine2", relief="solid")
b2.grid(row=1, column=2, padx=3)

main_window.mainloop()
