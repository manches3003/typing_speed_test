from time import *
import random as r


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


arr = ["hey i am keshav kansara",
       "hey do u know how to code", "hello bro do even code"]

test = r.choice(arr)

print("********typing speed test***********")
print()
print()
print(test)


def countdown(timesec):
    while(timesec > 0):
        timesec = timesec - 1
        time.sleep(1)


time_1 = countdown(10)
userinput = input()
print("speed: ", speed_test(time_1, userinput), "Wpm")
print("errors: ", mistake(test, userinput))
