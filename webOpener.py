import webbrowser

print("1, Telegram \n2, Google \n3, YouTube \n4, Chatgpt")

webchoice = {"1": "https://web.telegram.org", "2": "https://google.com",
             "3": "https://youtube.com", "4": "https://chatgpt.com"}
choice = input("Choose the web you want to open: ")
print(webbrowser.open(webchoice[choice]))