import time

print("Please enter a decimal for x: ")
x = float(input(">> "))
initial_x = x
print("Please enter a decimal for y:")
y = float(input(">> "))
initial_y = y
print("Please enter a value for which you wish to increase x by each time:")
addition_x = float(input(">> "))
print("Please enter a value for which you wish to increase y by each time:")
addition_y = float(input(">> "))
count = int(0)
print("Please enter how many times you want this calculation to happen:")
user_count = int(input(">> "))
start = time.time()


while user_count >= count:
    x += addition_x
    y += addition_y
    print(x * y)
    count += 1
    #time.sleep(0.1)

end = time.time()
print("Time taken: ", end - start, " seconds")
print("\nEntered values: ", "\nx: ", initial_x, "\ny: ", initial_y, "\nx increase: ", addition_x, "\ny increase: ", addition_y, "\nNumber of calculations: ", user_count)
