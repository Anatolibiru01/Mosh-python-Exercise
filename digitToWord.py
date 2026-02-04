digit_to_word = {"0": "Zero", "1": "One", "2": "Two", "3": "Three", "4": "Four",
                 "5": "Five", "6": "Six", "7": "Seven",
                 "8": "eight", "9": "Nine"}

user_input = tuple(input("Please, enter your number: "))

last = []
for i in user_input:
    dict = digit_to_word[i]
    last.append(dict)

print("Output: ", end=" ")
for k in last:
    print(k, end=" ")