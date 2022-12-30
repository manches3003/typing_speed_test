from threading import Thread
import random as r
import time
import os
import msvcrt

arr = ['''authors traditionally divide their thoughts and arguments into sequences of paragraphs''',
       '''The real wealth of an individual is hard work and nobody can become successful without it.''',
       '''A paragraph is a collection of words strung together to make a longer unit than a sentence''',
       ''' The application is a minimalistic and customizable typing test. ''']

answer = ""
test = ""


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


def ask():
    global start_time, answer, test
    start_time = time.time()
    test = r.choice(arr)
    empty_string = ""
    print(test)
    while(empty_string != "\n"):
        empty_string = msvcrt.getch().decode('ASCII')
        answer += empty_string

    time.sleep(0.001)


def timing(run_time):
    time_limit = run_time
    while True:
        time_taken = time.time() - start_time
        if time_taken > time_limit:
            print(answer)
            print("----> speed: ", speed_test(x, answer), "Wpm")
            print("-----> errors: ", mistake(test, answer))
            os._exit(1)
        time.sleep(0.001)


x = int(input("how many seconds you want to run this code? \n"))
t1 = Thread(target=ask)
t2 = Thread(target=lambda run_time=x: timing(run_time))
t1.start()
t2.start()
