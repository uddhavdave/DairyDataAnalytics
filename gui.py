from tkinter import *

root = Tk()
l1= Label(root, text="WELCOME to DAIRY MANAGEMENT",bg="black",fg="white")
l1.pack(fill=X)
l2= Label(root,text="Select from below",fg="black")
l2.pack(fill=X)
frame = Frame(root)
frame.pack()



button1= Button(frame,text="Insert Data",fg="blue")
button2= Button(frame,text="View Data",fg="blue")
button3= Button(frame,text="Updates",fg="green")
button4= Button(frame,text="View Graph",fg="red")
button5= Button(frame,text="QUIT",fg="red")

button1.grid(row=0)
button2.grid(row=1)
button3.grid(row=2)
button4.grid(row=3)

root.mainloop()