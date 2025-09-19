import time
#ch3ex13
#Arthur Belanger
#Find sum of input numbers
#2-05-25
#In class exercise
#--------------------------------

def main():
    n = int(input("How many numbers do you want the sum of? "))
    sum = 0    
    for _ in range(n):
        number = int(input("Please enter number: "))
        sum = sum + number
    print(f"The sum of the numbers is {sum}")
main()


#---End of code------------------
#Arthur Belanger
#Programming Fundamentals CIS-110
print(time.ctime())
