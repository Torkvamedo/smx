print('Task 3 (like a chat-bot)')
while True:
    print("========If you wonna quit,  press 'x' for exit=========")
    phrase = input("message: ")
    if phrase == "x":
       break
    elif phrase == "Hello" or phrase == "Hi" or phrase == "qq":
        print("Hello , how are you  ?")
    elif phrase == "fine thanks" or phrase == "good":
        print("this is great :D")
    elif phrase == "and you ?":
        print("Oh, I'am good too :D")
    elif phrase == "I'm tired":
        print("you no longer want to talk with me?")
    elif phrase =="yeah" or phrase == "yeap" or phrase == "yes":
        print("this is bad... I'm sad")
    elif phrase == "oh comeon" or phrase == "not again":
        print("you are so cruel")
    elif phrase == "no" or phrase == "yes":
        print("always like this")
    elif phrase == "ok bye" or phrase == "bye":
        print("bye")
    phrase = input("message: ")
    if phrase == "bye":
            break
    else:
         print("I don't understand you")
#есть вопросы касаемо повтороного ввода
#хотел бы узнать как можно это обойти )))
# Заранее благодарен )
