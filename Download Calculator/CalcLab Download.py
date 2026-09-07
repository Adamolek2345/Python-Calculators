#All the code in here was written by me (Adamolek2345) for the Python Calculators repository on GitHub.
#Feel free to join my project and contribute, to make more of these !

#This is the one of the first calculators in my repository; It will be updated
#This is a download speed calculator made to calculate download speeds.
#I want to mention that this is Version 1.0 of this calculator; If you find any issues, report them to my GitHub.
#Thank you so much for downloading my project. It is a huge help, that will let me make more of these types of scripts.




#code:

from time import sleep

version = "1.1"
print(r"""
  /$$$$$$            /$$           /$$                 /$$      
 /$$__  $$          | $$          | $$                | $$      
| $$  \__/  /$$$$$$ | $$  /$$$$$$$| $$        /$$$$$$ | $$$$$$$ 
| $$       |____  $$| $$ /$$_____/| $$       |____  $$| $$__  $$
| $$        /$$$$$$$| $$| $$      | $$        /$$$$$$$| $$  \ $$
| $$    $$ /$$__  $$| $$| $$      | $$       /$$__  $$| $$  | $$
|  $$$$$$/|  $$$$$$$| $$|  $$$$$$$| $$$$$$$$|  $$$$$$$| $$$$$$$/
 \______/  \_______/|__/ \_______/|________/ \_______/|_______/ 
  
                                      """)

print("===== Welcome to Download Calculator =====\n")
sleep(1)
print("CalcLab Download Version", version)
sleep(1)
print("Proceeding to calculator...\n")

# Input Internet speed
data_unit = input(
    "First, enter your data unit (MB or Mb)\nCareful, there is a difference between MB and MBIT\nEnter data unit: ").strip().upper()

if data_unit == "MB":
    speed_in_MB = float(input("Alright! Now, please enter your internet speed in MB/s:\n"))
    download_size = float(input("Now, what is your download size in MB (1000MB is 1GB):\n"))
    elapsed_time_seconds = download_size / speed_in_MB
    elapsed_time_minutes = elapsed_time_seconds / 60
    print(f"Your download elapsed time is around {elapsed_time_minutes:.2f} minutes.")

elif data_unit == "MBIT" or data_unit == "MBPS" or data_unit == "MBPS":  # optional, see note
    speed_in_Mb = float(input("Alright! Now, please enter your internet speed in Mb/s:\n"))
    download_size = float(input("Now, what is your download size in MB (1000MB is 1GB):\n"))
    # Convert speed from Mb/s to MB/s
    speed_in_MB = speed_in_Mb / 8
    elapsed_time_seconds = download_size / speed_in_MB
    elapsed_time_minutes = elapsed_time_seconds / 60
    elapsed_time_hours = elapsed_time_minutes / 60
    print(f"Your download elapsed time is around {elapsed_time_minutes:.2f} minutes.\n")
    print("Your download elapsed time is around", elapsed_time_hours, "hours.\n")

else:
    print("Error: Wrong Data unit")
    print("Exiting in 3 seconds...")
    sleep(3)
    exit()

sleep(2)
#Big thanks to contributors AND users !
print("\n\nThank you for using PyCalc Download Calculator Version", version, "!")
print("If you find any bugs or issues, please report them on my GitHub profile (Adamolek2345)")
print("Also a huge thanks for the contributors of my project for the help !")
