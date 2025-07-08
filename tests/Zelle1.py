principal = int(input("Enter the starting principal: "))
numYears = int(input("Enter the amount of years to calculate: "))
intRate = float(input("Enter annual interest rate: "))


def main():
    value = 0
    year = 0
    for year in range(numYears):
        value = principal + (principal * intRate)
        year += 1

        print(f"For year {year} the current principle is: {value}")


if __name__ == "__main__":
    main()
