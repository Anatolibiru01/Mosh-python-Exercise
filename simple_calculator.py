description = """ \nThis calculator will evaluate and compute simple\noperation like +, -, *, /,//, power(**), and also \nit evaluate modulo (%) \n"""
print(description)
while True:
    try:
        inputs = eval(input(" Enter:  "))
        print(f" Answer = {round(inputs, 2)} \n ")
    except:
        print("error input it is not evaluated! please enter correct numbers")
