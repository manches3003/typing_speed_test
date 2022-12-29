from time import *
import random as r
import threading


def mistake(given_words, user_words):
    error = 0
    for i in range(len(user_words.split())):
        try:
            if(given_words.split()[i] != user_words.split()[i]):
                error = error + 1
        except:
            error = error + 1
    return error


def speed_test(time_set1, user_input):
    user_speed = (len(user_input.split())/(time_set1))*60
    return user_speed


arr = ['''this is a simple paragraph that is meant to be nice and easy to type which is why there will be
mommas no periods or any capital letters so i guess this means that it cannot really be considered a paragraph
but just a series of run on sentences this should help you get faster at typing as im trying not to use
too many difficult words in it although i think that i might start making it hard by including some more difficult
letters I'm typing pretty quickly so forgive me for any mistakes i think that i will not just tell you a story
about the time i went to the zoo and found a monkey and a fox playing together they''',
       '''you will be able to communicate more effectively in english both in written and spoken form. By decreasing your reading 
    size and focusing on a personalized language learning lesson your language levels will grow from simple vocabulary lists 
    to a built-in dictionary.''', '''hello bro do even code''']

test = r.choice(arr)

print("********typing speed test***********")
print()
print()
x = int(input("how many seconds you want to run this code? \n"))
print()
print()
print(test)

userinput = ""


def user():
    global userinput
    userinput = input()
    hey.cancel()


print()
print()

hey = threading.Timer(x, user)
hey.start()


while(True):

    if(hey.is_alive() == False):
        print("speed: ", speed_test(x, userinput), "Wpm")
        print("errors: ", mistake(test, userinput))
        break
