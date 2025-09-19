from ch6ex11 import isLeapYear

def main():
	year = int(input("Enter a year: "))
	month = int(input("Enter a month: "))
	day = int(input("Enter a day: "))

	validDate = True
	if month ==2:
		if isLeapYear(year):
			if day > 29:
				validDate = False
		else:
			if day > 28:
				validDate = False

	print(validDate)
main()
