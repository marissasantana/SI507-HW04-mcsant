from random import randrange
import random

def Magic():
    myboolean = True
    while myboolean == True:
        question = input("What is your question? To quit, enter 'quit'")

        if question == 'quit':
            break

        elif "?" not in question:
            print("I'm sorry, I can only answer questions.")
            myboolean==False

        else:
            random_words = ["It is certain", "It is decidedly so", "Without a doubt", "Yes definitely", "You may rely on it", "As I see it, yes", "Most likely", "Outlook good", "Yes", "Signs point to yes", "Reply hazy, try again", "Ask again later", "Better not tell you know", "Cannot predict now", "concentrate and ask again"]
            magic_random = randrange(0, len(random_words))
            print(random_words[magic_random])

Magic()
