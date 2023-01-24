import hashlib
from tkinter import *
from tkinter import filedialog
import os
from tkinter import ttk
main_window = Tk()
main_window.title("Checksum Utility")
main_window.config(bg="yellow2")
l1 = Label(main_window, text="MD5 Checksum :", relief="solid", bg="yellow green")
l1.grid(row=0, column=0, padx=3, pady=3)
e1 = Entry(main_window, bd=3, width=60, bg="burlywood1")
e1.grid(row=0, column=1, padx=3, pady=3)
l2 = Label(main_window, text="File/Checksum : ", relief="solid", bg="yellow green")
l2.grid(row=1, column=0, padx=3, pady=3)
e2 = Entry(main_window, bd=3, width=60, bg="burlywood1")
e2.grid(row=1, column=1, padx=3, pady=3)
os.chdir("/home/hassamrajpoot")


def func():
   global new_dialouge_box
   new_dialouge_box = filedialog.askopenfilename(parent=main_window, initialdir=os.getcwd(), title="files")
   e2.insert(0, str(new_dialouge_box))
   b1.config(state="disabled")


def generating_checksum():
   progress_bar = ttk.Progressbar(main_window, orient=HORIZONTAL, length=140, mode="determinate")
   progress_bar.grid(row=2, column=3, pady=0)
   for i in range(140):
      progress_bar["value"] += 5
   file_path = str(e2.get())
   hasher = hashlib.md5()
   with open(file_path, 'rb') as opened_file:
      content = opened_file.read()
      hasher.update(content)
   e2.delete(0, END)
   e2.insert(0, hasher.hexdigest())


def verifying():
  global lf
  global la
  if e1.get() == "" and e2.get() == "":
     la = Label(main_window, text="Please fill the first two information boxes !", relief="solid")
     la.grid(row=10, column=1, pady=3)
  elif e1.get() == "":
     try:
        la.destroy()
        la = Label(main_window, text="Please fill the first  information box !", relief="solid")
        la.grid(row=10, column=1, pady=3)
     except NameError:
        la = Label(main_window, text="Please fill the first  information box !", relief="solid")
        la.grid(row=10, column=1, pady=3)
  elif e2.get() == "":
     try:
        la.destroy()
        la = la = Label(main_window, text="Please fill the second  information box !", relief="solid")
        la.grid(row=10, column=1, pady=3)
     except NameError:
        la = la = Label(main_window, text="Please fill the second  information box !", relief="solid")
        la.grid(row=10, column=1, pady=3)
  else:
     original_checksum = str(e1.get())
     calculated_checksum = str(e2.get())
     if "/" in calculated_checksum:
        lf = Label(main_window, text="Please press 'Generate Checksum' key first and then verify", relief="solid")
        lf.grid(row=10, column=1, padx=3, pady=0)
     else:
        try:
           if original_checksum == calculated_checksum:
              lf.destroy()
              Label(main_window, text="Checksum matched!", relief="solid").grid(row=10, column=1, padx=3, pady=3)
           else:
              lf.destroy()
              Label(main_window, text="Checksum  doesn't match!", relief="solid").grid(row=10, column=1, padx=3, pady=3)
        except NameError:
           la.destroy()
           if original_checksum == calculated_checksum:
              Label(main_window, text="Checksum matched!", relief="solid").grid(row=10, column=1, padx=3, pady=3)
           else:
              Label(main_window, text="Checksum  doesn't match!", relief="solid").grid(row=10, column=1, padx=3, pady=3)


b1 = Button(main_window, text="Browse", bd=3,  relief="solid", command=func, bg="aquamarine2")
b1.grid(row=2, column=1, padx=(410, 0), pady=4)
b2 = Button(main_window, text="Generate Checksum", relief="solid", bd=2, width=14, command=generating_checksum, bg="aquamarine2")
b2.grid(row=1, column=3)

b3 = Button(main_window, text="Verify", bd=3, relief="solid", width=10, command=verifying, bg="aquamarine2")
b3.grid(row=3, column=1, pady=3)
main_window.mainloop()
