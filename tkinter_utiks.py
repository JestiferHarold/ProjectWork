from tkinter import *

class App(Tk):

    def __init__(self):
        super().__init__()
        self.geometry("700x600")
        # self.title()
        # self.iconbitmap()
        docker = Frame(self).pack()
        self.frames = {}
        for m in (
            Start,
            Login,
            Forgot_Password, 
            Create_New_Account, 
            Dashboard, 
            Make_File, 
            Get_File, 
            File_Details
            ):
            frame = m(docker, self)
            self.frames[m] = frame
            frame.pack()
        self.on_top(Start)

    def on_top(self, frame_name):
        self.frames[frame_name].tkraise()

    def Day_Night_cycle(self):
        m = 0
        if m % 2 == 0:
            self.foreground = "Black"
            self.background = "White"
        else:
            self.foreground = "White"
            self.background = "Black"
        m += 1

class Start(Frame):
    def __init__(self, Parent, Controller):
        super().__init__(Parent)
        self.Control = Controller
        k = Label(text = "Click the Button Below to start").pack()
        e = Button(self, text = "START", command = lambda: self.Control.destroy()).pack()

class Login(Frame):
    def __init__(self, Parent, Controller):
        super().__init__(Parent)

class Forgot_Password(Frame):
    def __init__(self, Parent, Controller):
        super().__init__(Parent)

class Create_New_Account(Frame):
    def __init__(self, Parent, Controller):
        super().__init__(Parent)

class Dashboard(Frame):
    def __init__(self, Parent, Controller):
        super().__init__(Parent)

class Make_File(Frame):
    def __init__(self, Parent, Controller):
        super().__init__(Parent)

class Get_File(Frame):
    def __init__(self, Parent, Controller):
        super().__init__(Parent)

class File_Details(Frame):
    def __init__(self, Parent, Controller):
        super().__init__(Parent)

