# " Caesar Cipher decryption and encrypt, 3 letter forward"
import string

print("Select:- \n 1. decrytion. \n 2. encryption.")

while True:
    select = input("  :- ")
    if select == "1" or select == "2":
        break
    else:
        print("Invalid!!")
        continue
print(" Make sure the maximum base is 26.")
base = int(input(" base: "))

user = input("Enter input: ")

lower = string.ascii_lowercase
upper = string.ascii_uppercase
words = []


def character():
    for i in range(len(user)):
        if (user[i] in lower) or (user[i] in upper):
            if user[i] in lower:
                decrypt_or_encrypt(lower, i)
            else:
                decrypt_or_encrypt(upper, i)
        else:
            words.append(user[i])


def decrypt_or_encrypt(chart, indexs):
    num = chart.index(user[indexs]) + base
    if num > 26:
        j = num - 26
    else:
        if select == "1":
            j = chart.index(user[indexs]) - base
        else:
            j = chart.index(user[indexs]) + base
    words.append(chart[j])


character()
print(f"The word is: {"".join(words)}")
