import customtkinter
from tkinter import *
from tkinter import filedialog

g = open('test_entry.txt', 'w')
g.close()
f = open('test_filedialog.txt', 'w')
f.close()

class Startseite(customtkinter.CTk):
    def bestätigen(self):
        g = open('test_entry.txt', 'w')
        g.write(str(self.entry.get()))
        g.close()

    def openfile(self):
        path = filedialog.askopenfilenames(title="Datei auswählen", filetypes=[("CSV-Datein (.csv)", "*.csv"),("Alle Datein", "*.*")])
        f = open('test_filedialog.txt', 'w')
        f.write(str(path))
        f.close()

    def close(self):
        quit()

    def __init__(self):
        super().__init__()

        self.geometry("400x150") #bestimmt die Größe des Windows 
        self.title("Eingabe des Paths")
        self.minsize(300, 200)

        self.grid_rowconfigure(0, weight=3) #erstellt ein grid
        self.grid_columnconfigure((0, 1), weight=1)

        self.label = customtkinter.CTkLabel(master=self, text="Hier den Path einfügen!")
        self.label.grid(row=0, column=0, padx=1, pady=1)

        self.button = customtkinter.CTkButton(master=self, command=self.bestätigen, text="Path bestätigen")
        self.button.grid(row=2, column=0, padx=1, pady=1)

        self.entry = customtkinter.CTkEntry(master=self)
        self.entry.grid(row=1, column=0, padx=1, pady=1)
        global entry

        self.label1 = customtkinter.CTkLabel(master=self, text="Einzelne Datein raussuchen!")
        self.label1.grid(row=0, column=1, padx=1, pady=1)

        self.button0 = customtkinter.CTkButton(master=self, command=self.openfile, text="Suchen")
        self.button0.grid(row=1, rowspan=2, column=1, padx=1, pady=1)

        self.button1 = customtkinter.CTkButton(master=self, text="Fortfahren", command=self.close)
        self.button1.grid(row=3, column=0, columnspan=2, padx=10, pady=12)

if __name__ == "__main__":
    app = Startseite()
    app.mainloop()  