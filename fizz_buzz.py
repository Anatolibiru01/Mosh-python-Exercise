from pprint import pprint
output = []
i = int(input("Enter number: "))


def fizzBuzz(i):
    if i % 3 == 0 and i % 5 == 0:
        return "fizzbuzz"
    elif i % 3 == 0:
        return "fizz"
    elif i % 5 == 0:
        return "buzz"
    else:
        return str(i)


for j in range(1, i+1):
    output.append(fizzBuzz(j))

pprint(output, width=1)
