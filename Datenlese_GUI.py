import glob
import pandas as pd
import os
import customtkinter
from tkinter import *

with open(os.getcwd()+"\\Test_filedialog.txt", 'r') as file1:
    data = file1.read()
    data = data.replace(', ', "\n")
with open(os.getcwd()+"\\Test_filedialog.txt", 'w') as file2:
    file2.write(data)

global ausgabe
global ausgabe1
global ausgabe2

g = open(os.getcwd()+"\\Ausgabe_file.txt", 'w')
g.close() 


with open(str(os.getcwd()+"\\test_filedialog.txt")) as text1:
    colnames=['Test']    
    text2 = pd.read_csv(text1, header=None, names=colnames ,sep=",")
    text = list()
    text3 = list(text2.values.tolist())
    if os.stat(str(os.getcwd()+"\\test_filedialog.txt")).st_size == 0:
        ausgabe = ("Es wurden 0 CSV-Datein mithilfe des Filedialoges erkannt.")
    else:
        for word in text3:
            platz = str(word)
            probe = platz.replace('"', "").replace("'","").replace(r"/", "\\").replace(r"(","").replace(r")","").replace(r"[","").replace(r"]","")
            if probe.endswith('.csv') == True:
                text.append(probe)
            else:
                pass
        ausgabe = ("Es wurden "+ str(len(text)) +" CSV-Datein mithilfe des Filedialoges erkannt.")
    with open(str(os.getcwd()+'\\Ausgabe_file.txt'), 'w+') as file3:
            file3.write('\n'.join(text))
            halter = 1
    
with open(str(os.getcwd()+"\\test_entry.txt")) as lesen:
    filenames = "" 
    entry = pd.read_csv(lesen, names=colnames ,header=None)
    if os.stat(str(os.getcwd()+"\\test_entry.txt")).st_size == 0:
        ausgabe1 = "Es wurden 0 CSV-Datein mithilfe des Paths erkannt."
    else:
        test1 = entry._get_value(0, "Test")
        filenames = glob.glob(test1 + r"\*.csv")
        ausgabe1 ="Es wurden "+ str(len(filenames)) +" CSV-Datein mithilfe des Paths erkannt."
        with open(str(os.getcwd()+'\\Ausgabe_file.txt'), 'w') as file: 
            if halter == 0:
                file.write('\n'.join(filenames))
                print("hinzugefügt")
            else:       
                with open(str(os.getcwd()+'\\Ausgabe_file.txt'), 'w+') as file:             
                    text = list(set(text + filenames))
                    file.write('\n'.join(text))
ausgabe2 = "Es wurden "+ str(len(text)) +" unique CSV-Datein erkannt."
            
   
class GUI(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        
        self.geometry("400x100") #bestimmt die Größe des Windows 
        self.title("Bestätigen der ausgewählten Daten")
        self.minsize(300, 200)

        self.label = customtkinter.CTkLabel(master=self,  text=ausgabe)
        self.label.pack(pady=1, padx=1)

        self.label1 = customtkinter.CTkLabel(master=self, text=ausgabe1)
        self.label1.pack(pady=1, padx=1)

        self.label2 = customtkinter.CTkLabel(master=self, text=ausgabe2)
        self.label2.pack(pady=1, padx=1)

        self.button = customtkinter.CTkButton(master=self, text="Analyisieren" , command=self.close)
        self.button.pack(padx=1, pady=1)


    def close(self):
        quit()

if __name__ == "__main__":
    app = GUI()
    app.mainloop() 