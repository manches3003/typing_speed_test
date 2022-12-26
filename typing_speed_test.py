from time import *
import random as r
import threading

def mistake(given_words, user_words):
    error = 0
    for i in range(len(given_words)):
        try:
            if(given_words[i] != user_words[i]):
                error = error + 1
        except:
            error = error + 1
    return error


def speed_test(time_set1, user_input):
    user_speed = len(user_input)/time_set1
    return round(user_speed)


arr = ['''this is a simple paragraph that is meant to be nice and easy to type which is why there will be 
mommas no periods or any capital letters so i guess this means that it cannot really be considered a paragraph 
but just a series of run on sentences this should help you get faster at typing as im trying not to use 
too many difficult words in it although i think that i might start making it hard by including some more difficult
letters I'm typing pretty quickly so forgive me for any mistakes i think that i will not just tell you a story 
about the time i went to the zoo and found a monkey and a fox playing together they''',
"hey do u know how to code", "hello bro do even code"]

test = r.choice(arr)

print("********typing speed test***********")

print()
x = int(input("how many seconds you want to run this code? \n"))
print()
print(test)

userinput = input()
hey = threading.Timer(x,userinput)
y=hey.start()
z= hey.is_alive()
if (z == False):
    print("speed: ", speed_test(x,userinput), "Wpm")
    print("errors: ", mistake(test, userinput))

# print("speed: ", speed_test(x,userinput), "Wpm")
# print("errors: ", mistake(test, userinput))
