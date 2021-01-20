import tkinter

data = {
    'I' : 1,
    'V' : 5,
    'X' : 10,
    'L' : 50,
    'C' : 100,
    'D' : 500,
    'M' : 1000
}

def checkValid(value):
    for char in value:
        if char not in data:
            return False
        else:
            return True
            

def convert():
    number = romanInput.get()
    isValid = checkValid(number)
    if isValid == False:
        answer.config(text="That number isn't valid")
    else:
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
        answer.config(text="{}".format(decimal))

# Creacion de ventana
window = tkinter.Tk()
window.resizable(False, False)
window.geometry("300x200")
window.title("Roman to Decimal converter")

label1 = tkinter.Label(window, text="Enter your roman number")
label1.pack(pady="10")

romanInput = tkinter.Entry(window)
romanInput.pack(ipady="5")

label2 = tkinter.Label(window, text="Decimal is equal to")
label2.pack(pady="10")

answer = tkinter.Label(window)
answer.pack(pady="0")

button = tkinter.Button(window, text="Press to convert", command = convert)
button.pack(ipady="5", ipadx="10")

# El mainloop lleva el registro de lo que sucede en la ventana
window.mainloop()