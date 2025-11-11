#All the code in here was written by me (Adamolek2345) for the Python Calculators repository on GitHub.
#Feel free to join my project and contribute, to make more of these !

#This is the first calculator in my repository; It will be updated
#This is a battery calculator to calculate battery capacity and battery bank building
#I want to mention that this is Version 1.0; If you find any issues, report them to my GitHub.
#Thank you so much for downloading my project. It is a huge help, that will let me make more of these types of scripts.




#Code:

from time import sleep
version = "1.0"


print("=====Welcome to the Battery Calculator=====\n")
sleep(1)
print("PyCalc Battery Version", version)
sleep(1)
print("Proceeding to calculator...\n")

#Input voltage, capacity and weight of the batteries
battery_voltage = float(input("First, enter the voltage of your battery cells:\n"))
sleep(1)
battery_capacity = float(input("Now, enter your battery cell's capacity in mAH:\n"))
battery_weight = float(input("Now, enter your battery cell's weight in grams:\n"))
sleep(2)

#Calculate needed battery bank voltage
desired_voltage = float(input("Alright. Now, enter your desired battery bank's voltage:\n"))
needed_bank_voltage = desired_voltage / battery_voltage
sleep(1)
print("In that case, You would need", needed_bank_voltage, "batteries in series to achieve", desired_voltage, "!")
sleep(2)

#Calculate needed battery bank capacity
desired_capacity = float(input("Now, enter your desired battery bank's capacity\n"))
needed_bank_capacity = desired_capacity / battery_capacity
sleep(1)
print("In that case, you would need", needed_bank_capacity, "batteries overall to achieve your desired capacity of", desired_capacity, "mAH")
print("You need ", needed_bank_capacity, "batteries in series of", needed_bank_voltage, "batteries.")
sleep(2)

#Calculate needed battery weight
desired_weight = float(input("Please enter you battery bank's desired weight\n"))
needed_bank_weight = desired_weight / battery_weight


sleep(2)
#Big thanks to contributors AND users !
print("\n\nThank you for using PyCalc Battery Calculator Version", version, "!")
print("If you find any bugs or issues, please report them on my GitHub profile (Adamolek2345)")
print("Also a huge thanks for the contributors of my project for the help !")
