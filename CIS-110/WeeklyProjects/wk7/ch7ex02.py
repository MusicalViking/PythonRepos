"""
Program Name : ch7ex02
Program description : Creates the Syracuse sequence
Author: Arthur Belanger
Date created: 3-13-25
Notes:The "Syracuse sequence," also known as the Collatz conjecture or the 3n+1 problem, got its name from the mathematician Helmut Hasse, who spread the problem to Syracuse University in the United States-Courtesy of Google :) thought that was a pretty cool fact

"""
print("--------------------------------")
import time

def main():
    print("let's find the Syracuse Sequence!")
    
    n = int(input("Enter a start value: "))    
    while n != 1:
        print(n, end=' ')
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1       
    print(1)  

if __name__ == "__main__":
    main()

print("--------------------------------")
print("Arthur Belanger")
print("CIS-110 - ch7ex02 ")
print(time.ctime())
    

