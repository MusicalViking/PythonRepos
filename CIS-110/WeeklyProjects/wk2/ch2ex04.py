import time
#ch2ex04
#Arthur Belanger
#Converts celsius to fahrenheit 5 times
#1-29-25

#--------------------------------

def main():
    for i in range(5):
        celsius = float(input("What is the Celsius temperature? "))
        fahrenheit = 9/5 * celsius + 32
        
        if fahrenheit > 90:
            print(f"There is a heat warning for today, the temperature is {fahrenheit}")
        elif fahrenheit < 30:
            print(f"The weather requires an extra layer or two due to cold temps, the temperature is {fahrenheit}")
        else:
            print(f"The  temperature is {fahrenheit} :")

    
main()




#---End of code------------------
#Arthur Belanger
#Programming Fundamentals CIS-110
print(time.ctime())
