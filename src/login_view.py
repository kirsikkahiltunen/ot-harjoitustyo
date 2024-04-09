from tkinter import Tk, ttk, constants

class UI:
    def __init__(self, root):
        self._root = root
        self._username = None
        self._password = None
    

    def login(self):
        heading_label = ttk.Label(master=self._root, text="Kirjaudu sovellukseen")

        username_label = ttk.Label(master=self._root, text="Käyttäjänimi")
        self._username_entry = ttk.Entry(master=self._root)

        password_label = ttk.Label(master=self._root, text="Salasana")
        self._password_entry = ttk.Entry(master=self._root, show="*")

        button = ttk.Button(master=self._root, text="Kirjaudu", command=self._login_handler)

        heading_label.grid(row=0, column=0, columnspan=2, sticky=constants.W, padx=5, pady=5)

        username_label.grid(row=1, column=0, padx=5, pady=5)
        
        self._username_entry.grid(row=1, column=1, sticky=(constants.E, constants.W), padx=5, pady=5)

        password_label.grid(row=2, column=0, padx=5, pady=5)
        
        self._password_entry.grid(row=2, column=1, sticky=(constants.E, constants.W), padx=5, pady=5)

       
        button.grid(row=3, column=0, columnspan=2, sticky=(constants.E, constants.W), padx=5, pady=5)

        self._root.grid_columnconfigure(1, weight=1, minsize=300)

    
    def _login_handler(self):
        self._username = self._username_entry.get()
        self._password = self._password_entry.get()

        if self._username == "Testi" and self._password == "Testi":
            self.welcome()

    def welcome(self):
        self._welcome_frame.grid()


                

window = Tk()
window.title("Fysiikankertaus sovellus")

ui = UI(window)
ui.login()

window.mainloop()