def length_converter():
    length = float(input("Enter length in meter: "))
    km = length/1000
    cm = length * 100
    mm = length * 1000
    return f" 1. In kilometer: {km}km \n 2. In centimeter: {cm}cm \n 3. In millimeter: {mm}mm"


def weight_converter():
    weight = float(input("Enter weight in Kg: "))
    gram = weight * 1000
    milligram = weight * 1000000
    return f" 1. In Gram: {gram}g \n 2. In milligram: {milligram}mg"


def temperature_converter():
    Celsius = float(input("Enter a temperature in celsius: "))
    C_F = 9/5*Celsius + 32
    C_K = Celsius + 273.15
    return f" 1. Temp.Fahrenheit is: {round(C_F, 2)} \n 2. Temp.kelvin is: {C_K}"


print("Select a conversion category")
print(" 1. Length \n 2. Weight \n 3. Temperature ")
choice = input("Enter the number of your choice: ")

if choice == "1":
    print("You chose length convertion\n")
    print(length_converter())
elif choice == "2":
    print("You chose weight convertion\n")
    print(weight_converter())
elif choice == "3":
    print("You chose Temperature convertion\n")
    print(temperature_converter())
else:
    print("Your choice is out of the option")