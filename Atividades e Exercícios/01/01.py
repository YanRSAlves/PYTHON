import tkinter as tk
from tkinter import messagebox

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.quit_button = tk.Button(self, text="Quit", fg="red",
                                     command=self.master.destroy)
        self.quit_button.pack(side="bottom")

        self.hello_label = tk.Label(self, text="Hello World!")
        self.hello_label.pack(side="top")

        self.my_button = tk.Button(self, text="Clique aqui!",
                                   command=self.show_message)
        self.my_button.pack(side="top")

    def show_message(self):
        tk.messagebox.showinfo("Mensagem", "Olá! Você clicou no botão!")


root = tk.Tk()
app = Application(master=root)
app.mainloop()