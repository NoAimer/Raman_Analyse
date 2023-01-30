import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt

from scipy.ndimage import uniform_filter1d
from pybaselines import Baseline

with open(str(os.getcwd()+"\\Ausgabe_file.txt")) as filenames:
    for file in filenames:
        files1= str(file.replace("\n", ""))
        with open(files1) as daten:
            data = pd.read_csv(daten, delimiter = ";", header=None) #ließt die Daten und trennt die beim ";" gibt keine Kopfzeile an
            x = data[0] #x Daten in der 1. Spalte
            y = data[1] #y Daten in der 2. Spalte
            
            
            baseline = 50 + 1 * np.exp(-x / 1000)
                    
            baseline_fitter = Baseline(x_data=x)
                    
            smooth_y = uniform_filter1d(y, 11)
                    
            plt.figure()
            plt.plot(y, label='data')
            lam = 1e6
            plt.plot(baseline_fitter.arpls(y, lam=lam)[0], label=f'lam={lam:.0f}')
            plt.legend()