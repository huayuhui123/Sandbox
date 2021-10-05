"""
CP1404/CP5632 - Practical
Pseudocode for temperature conversion
"""
def main():
    MENU = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"""
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
           fahrenheit =CtoF()
           print("Result: {:.2f} F".format(fahrenheit))
        elif choice == "F":
           celsius =FtoC()
           print("Result: {:.2f} C".format(celsius))
        else:
           print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you.")

def CtoF():
    celsius = float(input("Celsius: "))
    CtoF = celsius * 9.0 / 5 + 32
    return CtoF
def FtoC():
    fahrenheit = float(input("fahrenheit: "))
    FtoC= 5 / 9 * (fahrenheit - 32)
    return FtoC
main()
