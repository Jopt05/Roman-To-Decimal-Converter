import os

data = {
    'I' : 1,
    'V' : 5,
    'X' : 10,
    'L' : 50,
    'C' : 100,
    'D' : 500,
    'M' : 1000
}

def clear():
    os.system('clear')

def convert( number ):
    decimal = 0
    x = 0
    while x < len(number):
        v1 = data.get(number[x])
        if x + 1 < len(number):
            v2 = data.get(number[x+1])
            if v1 >= v2:
                decimal += v1
                x += 1
            else:
                decimal = decimal + v2 - v1
                x += 2
        else:
            decimal += v1
            x += 1
    print("Conversion equals to:", decimal)

while True:
    print("----------------------------------------")
    print("\tRoman to Decimal Converter")
    print("\t\tby Jopt05")
    print("----------------------------------------")

    print("")

    roman_number = input("Insert your roman number = ")

    for char in roman_number:
        if char not in data:
            print(char ,"is not valid. Try again")
            break
    

    convert( roman_number )
    break