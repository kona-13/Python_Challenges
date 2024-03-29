# -*- coding: utf-8 -*-
"""
Created on Fri Mar 29 11:33:44 2024

@author: Steven W
"""
import matplotlib.pyplot as plt

def setup():
    print("Enter a value for x:")
    x = float(input(">> "))

    print("Enter a value for y:")
    y = float(input(">> "))

    operator_state = int(input("Would you rather: 1.) Multiply or 2.) Divide:\n>> "))

    print("How many times would you like to do this operation?")
    how_many = int(input(">> "))

    results = [x]
    for i in range(1, how_many):
        if operator_state == 1:
            results.append(results[-1] * x)
        elif operator_state == 2:
            if y != 0:
                results.append(results[-1] / y)
            else:
                print("Error: Division by zero")
        else:
            print("Invalid operator state")
            return

    print("\nResults:")
    for result in results:
        print(result)

    plt.plot(range(1, how_many + 1), results, marker='o')  # Plotting the results as a line graph
    plt.xlabel('Iterations')
    plt.ylabel('Results')
    plt.title('Results of Operations')
    plt.grid(True)
    plt.show()

setup()


