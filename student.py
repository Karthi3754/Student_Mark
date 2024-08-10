from tkinter import *
parent = Tk()
parent.title("MARKSHEET")
parent.geometry("700x250")
e1 = Entry(parent)
e2 = Entry(parent)
e3 = Entry(parent)
e4 = Entry(parent)
e5 = Entry(parent)
e6 = Entry(parent)
e7 = Entry(parent)
def display():
 total = 0
 if e4.get() == "A":
  Label(parent, text="40").grid(row=3, column=4)
  total += 40
 if e4.get() == "B":
  Label(parent, text="36").grid(row=3, column=4)
  total += 36
 if e4.get() == "C":
  Label(parent, text="32").grid(row=3, column=4)
  total += 32
 if e4.get() == "D":
  Label(parent, text="28").grid(row=3, column=4)
  total += 28
 if e5.get() == "A":
  Label(parent, text="40").grid(row=4, column=4)
  total += 40
 if e5.get() == "B":
  Label(parent, text="36").grid(row=4, column=4)
  total += 36
 if e5.get() == "C":
  Label(parent, text="32").grid(row=4, column=4)
  total += 32
 if e5.get() == "D":
  Label(parent, text="28").grid(row=4, column=4)
  total += 28
 if e6.get() == "A":
  Label(parent, text="40").grid(row=5, column=4)
  total += 40
 if e6.get() == "B":
  Label(parent, text="36").grid(row=5, column=4)
  total += 36
 if e6.get() == "C":
  Label(parent, text="32").grid(row=5, column=4)
  total += 32
 if e6.get() == "D":
  Label(parent, text="28").grid(row=5, column=4)
  total += 28
 if e7.get() == "A":
  Label(parent, text="40").grid(row=6, column=4)
  total += 40
 if e7.get() == "B":
  Label(parent, text="36").grid(row=6, column=4)
  total += 36
 if e7.get() == "C":
  Label(parent, text="32").grid(row=6, column=4)
  total += 32
 if e7.get() == "D":
  Label(parent, text="28").grid(row=6, column=4)
  total += 28
 Label(parent, text=str(total)).grid(row=7, column=4)
 Label(parent, text=str(total/16)).grid(row=8, column=4)
Label(parent, text="Name").grid(row=0, column=0)
Label(parent, text="Reg.No").grid(row=0, column=3)
Label(parent, text="Roll.No").grid(row=1, column=0)
Label(parent, text="subject").grid(row=2, column=1)
Label(parent, text="M1").grid(row=3, column=1)
Label(parent, text="M2").grid(row=4, column=1)
Label(parent, text="M3").grid(row=5, column=1)
Label(parent, text="M4").grid(row=6, column=1)
Label(parent, text="Grade").grid(row=2, column=2)
e1.grid(row=0, column=1)
e2.grid(row=0, column=4)
e3.grid(row=1, column=1)
e4.grid(row=3, column=2)
e5.grid(row=4, column=2)
e6.grid(row=5, column=2)
e7.grid(row=6, column=2)
Label(parent, text="CREDIT").grid(row=2, column=3)
Label(parent, text="4").grid(row=3, column=3)
Label(parent, text="4").grid(row=4, column=3)
Label(parent, text="4").grid(row=5, column=3)
Label(parent, text="4").grid(row=6, column=3)
Label(parent, text="Mark").grid(row=2, column=4)
button1 = Button(parent, text="submit", fg="blue", 
command=display)
button1.grid(row=8, column=1)
Label(parent, text="Total credit").grid(row=7, column=3)
Label(parent, text="CGPA").grid(row=8, column=3)
parent.mainloop()
