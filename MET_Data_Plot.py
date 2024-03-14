# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 19:34:48 2024

@author: Steven W
"""

import tkinter as tk
from tkinter import filedialog
import csv
import matplotlib.pyplot as plt
import numpy as np

opened_file = None

def browse():
    global opened_file
    print("Browse Clicked")
    opened_file = filedialog.askopenfile(mode='r', filetypes=[('Met_Data_Plot', '*.csv')])
    if opened_file is not None: 
        print(".csv Obtained") 
        
def plot():
    print("Plot Clicked")
    global opened_file
    if opened_file is not None:
        opened_file.seek(0)  # Reset file pointer to beginning
        csv_reader = csv.reader(opened_file)
        
        # Skip the header row
        next(csv_reader)
        
        years = []
        months = []
        rainfall = []
        
        for row in csv_reader:
            years.append(float(row[0]))  # Assuming year is in column 0
            months.append(float(row[1]))  # Assuming month is in column 1
            rainfall.append(float(row[5]))  # Assuming rainfall is in column 5
            
        colormap = plt.get_cmap('tab10')
        unique_months = np.unique(months)
        num_months = len(unique_months)
        colors = [colormap(i/num_months) for i in range(num_months)]
        
        # Plotting
        plt.figure(figsize=(8, 4))
        for month, color in zip(unique_months, colors):
            indices = [i for i, m in enumerate(months) if m == month]
            plt.scatter([years[i] for i in indices], [rainfall[i] for i in indices], c=color, label=int(month))
        plt.xlabel('Year')
        plt.ylabel('Rainfall (mm)')
        plt.title('Rainfall Over Years')
        plt.grid(True)  # Add gridlines
        
        # Set custom increments for x-axis and y-axis gridlines
        plt.xticks(np.arange(min(years), max(years)+1, 5) , rotation='vertical')  # Custom x-axis gridlines every 5 years
        plt.yticks(np.arange(0, max(rainfall)+1, 5))  # Custom y-axis gridlines every 50 mm
        
        plt.legend(title='Month', bbox_to_anchor=(1.05, 1), loc='upper left')  # Move legend outside of plot
        plt.tight_layout()  # Adjust layout to prevent overlapping
        plt.show()
        
    else:
        print("No file has been opened yet.")

def test():
    global opened_file
    print("Test clicked")
    if opened_file is not None:
        csv_reader = csv.reader(opened_file)
        second_row = next(csv_reader)  # Get the second row
        print("Second entry:", second_row)
    else:
        print("No file has been opened yet.")    

root = tk.Tk()
root.title("MET Office Rainfall plotter")
canvas = tk.Canvas(root, width=400, height=100)
canvas.grid(columnspan=3, rowspan=7)

browse_btn = tk.Button(root, text="Browse", command=browse)
browse_btn.grid(row=0, column=0)

plot_btn = tk.Button(root, text="Plot", command=plot)
plot_btn.grid(row=0, column=1)

test_btn = tk.Button(root, text="Test", command=test)
test_btn.grid(row=0, column=2)

root.mainloop()
