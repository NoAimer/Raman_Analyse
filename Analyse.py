import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
from scipy.signal import find_peaks

colnames = ["Test"]

with open(str(os.getcwd()+"\\Ausgabe_file.txt")) as filenames:
    for file in filenames:
        files1= str(file.replace("\n", ""))
        with open(files1) as daten:
            data = pd.read_csv(daten, delimiter = ";", header=None) #ließt die Daten und trennt die beim ";" gibt keine Kopfzeile an
            x = data[0] #x Daten in der 1. Spalte
            y = data[1] #y Daten in der 2. Spalte
            fig, ax1=plt.subplots()
            plt.plot(x,y, color="red")
            plt.autoscale() #Hier muss noch etwas verändert werden, bei großen x-Werten wird es ein schwarzer Balken
                    
            plt.show()
        
            condition=np.logical_and() #Hier ist irgendwas verkehrt aber keine Ahnung was!
            newy=np.extract(condition,y)
            newx=np.extract(condition,x)
                        
            integral=np.trapz(newy,newx)
                        
            poly=Polygon([*zip(newx,newy)])
            ax1.add_patch(poly)
                    
            print(integral)
            #find_peaks fehlt noch.
            