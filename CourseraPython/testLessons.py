def intToRomNum(num):
    year = [
        1000, 900, 500, 400,
        100, 90, 50, 40,
        10, 9, 5, 4, 1
    ]

    roman = [
        "M", "CM", "D", "CD",
        "C", "XC", "L", "XL",
        "X", "IX", "V", "IV", 
        "I"
     ]
     
    roman_numeral = ''
    i = 0
    while num > 0:
        for _ in range(num // year[i]):
            roman_numeral += roman[i]
            num -= year[i]
        i += 1
    return roman_numeral

number = int(input("Please enter the number you want to convert: "))
print(f"The Roman Numeral for {number} is {intToRomNum(number)}")
