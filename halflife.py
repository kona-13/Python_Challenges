# -*- coding: utf-8 -*-
"""
Created on Fri Mar 29 12:09:13 2024

@author: Steven W
"""

import matplotlib.pyplot as plt

def setup():
    print("Enter the initial quantity of the element:")
    initial_quantity = float(input(">> "))

    print("Enter the half-life of the element (in units of time):")
    half_life = float(input(">> "))

    print("How many time units would you like to observe the decay?")
    time_units = int(input(">> "))

    results = [initial_quantity]
    remaining_quantity = initial_quantity
    for i in range(1, time_units + 1):
        remaining_quantity /= 2
        results.append(remaining_quantity)

    print("\nResults:")
    for result in results:
        print(result)

    print("\nGraph:")
    plt.plot(range(time_units + 1), results, marker='o')  # Plotting the results as a line graph
    plt.xlabel('Time Units')
    plt.ylabel('Remaining Quantity')
    plt.title('Decay of Element Over Time')
    plt.grid(True)  # Add grid lines for better readability
    plt.show()

setup()
