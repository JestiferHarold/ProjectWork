import tkinter as tk
from tkinter import ttk

class App(tk.Tk):
    def __init__(self):
        super().__init__()

        # Set up the main application window
        self.title("Tkinter with Frames and Classes")
        self.geometry("400x300")

        # Container to hold all frames
        container = tk.Frame(self)
        container.pack(fill="both", expand=True)

        # Dictionary to hold references to all frames
        self.frames = {}

        # Initialize and display frames
        for F in (StartFrame, OtherFrame):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        # Show the StartFrame initially
        self.show_frame(StartFrame)

    def show_frame(self, frame_class):
        """Bring the specified frame to the front."""
        frame = self.frames[frame_class]
        frame.tkraise()

class StartFrame(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        # Label and button for the StartFrame
        label = tk.Label(self, text="Start Page", font=("Arial", 16))
        label.pack(pady=20)

        button = tk.Button(
            self, text="Go to Other Frame",
            command=lambda: controller.show_frame(OtherFrame)
        )
        button.pack()

class OtherFrame(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        # Label and button for the OtherFrame
        label = tk.Label(self, text="Other Page", font=("Arial", 16))
        label.pack(pady=20)

        button = tk.Button(
            self, text="Back to Start Frame",
            command=lambda: controller.show_frame(StartFrame)
        )
        button.pack()

if __name__ == "__main__":
    app = App()
    app.mainloop()
