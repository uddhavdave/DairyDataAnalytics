import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg,NavigationToolbar2TkAgg
from matplotlib.figure import Figure

import tkinter as tk
from tkinter import ttk
import tkinter.messagebox as tm

LARGE_FONT = ("Verdana", 12)



class Cowdata(tk.Tk):
    def __init__(self, *args,**kwargs):
        tk.Tk.__init__(self, *args,**kwargs)
        tk.Tk.iconbitmap(self,default="download.ico")
        tk.Tk.wm_title(self,"Dairy Manager")
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        self.frames = {}

        for F in (startpage,insertgui,ViewGraph,login):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0,column=0,sticky="nsew")
        self.show_frame(startpage)


    def show_frame(self, cont: object) -> object:
        frame = self.frames[cont]
        frame.tkraise()


class startpage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Start Page", font=LARGE_FONT)
        label.pack()

        button1 = ttk.Button(self, text="Insert Data",command=lambda:controller.show_frame(login))
        button2 = ttk.Button(self, text="View Data",command=lambda:controller.show_frame(insertgui))
        button3 = ttk.Button(self, text="Updates", command=lambda:controller.show_frame(insertgui))
        button4 = ttk.Button(self, text="View Graph",command=lambda:controller.show_frame(ViewGraph))


        button1.pack()
        button2.pack()
        button3.pack()
        button4.pack()

class login(tk.Frame):

    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        self.controller = controller
        label = tk.Label(self,text="LOGIN", font=LARGE_FONT)
        label.pack(pady=10,padx=10)
        label2 = tk.Label(self, text="Username")
        label2.pack()
        self.E1= tk.Entry(self, bd=5)
        self.E1.pack()
        label3 = tk.Label(self,text="Password")
        label3.pack()
        self.E2 = tk.Entry(self,bd=5,show="*")
        self.E2.pack()
        logbut= ttk.Button(self,text="Login",command=self.Buttonclick)
        logbut.pack()
        b3 = ttk.Button(self, text="Go to Start", command=lambda: controller.show_frame(startpage))
        b3.pack()



    def Buttonclick(self):
        user = self.E1.get()
        pass1 = self.E2.get()
        print(pass1)
        if user == "dipak" and pass1 == "ashapura":

                tm.showinfo("Login Successfull")
                self.controller.show_frame(insertgui)

        else:
            tm.showinfo("Login Failed")








class insertgui(tk.Frame):

    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self,text="Insert Data", font=LARGE_FONT)
        label.pack(pady=10,padx=10)
        b1 = ttk.Button(self, text="Insert new Cow data")
        b2 = ttk.Button(self, text="Insert Data to existing Cow")
        b3 = ttk.Button(self,text="Go to Start",command=lambda:controller.show_frame(startpage))
        b1.pack()
        b2.pack()
        b3.pack()

class ViewGraph(tk.Frame):

    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self,text="GRAPH", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        b3 = ttk.Button(self,text="Go to Start",command=lambda:controller.show_frame(startpage))

        b3.pack()

        f= Figure(figsize=(5,5),dpi=100)
        a=f.add_subplot(111)
        a.plot([1,2,3,4,5,6,7,8],[5,6,1,3,8,9,3,5])
        canvas = FigureCanvasTkAgg(f,self)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.TOP,fill=tk.BOTH,expand=True)

        toolbar = NavigationToolbar2TkAgg(canvas,self)
        toolbar.update()
        canvas._tkcanvas.pack(side=tk.TOP,fill=tk.BOTH,expand=True)


app = Cowdata()
app.mainloop()
