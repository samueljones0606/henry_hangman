"""

Exercises with variables (revision - we've done most of this before!

This script contains 3 exercises, each
one is contiained in a separate function. If you run the script, all three functions will be called (you can see this at the bottom of the script)
However at the moment they dont' print anythign at all, so it will look like nothig has happened. Your job is to go through each of the three functions and do what it says in the
instruction comments, so that each will print an answer. You can run the scriopt as many times as you like to check if your code is working.

when you have finishes, you might like to try adding a fourth function, by writing "def exercise_204()", and making it do whatever you like.

Good luck!

"""
import random

def exercise_200():

    seconds_per_minute = 60
    minutes_per_hour = 60

    # create variables called "hours_per_day" and "days_per_year" and assign them the right values

    hours_per_day = 24
    days_per_year = 365

    # at the moment, this line calcuates the number of seconds in an hour. using your new variables,
    # change it to calculate the number of seconds in a year
    
    answer = seconds_per_minute * minutes_per_hour * hours_per_day * days_per_year

    # write a line of code to print the results, using the "print" function
    print(answer)

    
def exercise_201():

    # Mummy gives each of Ed, Lucy and Henry £2.
    # Daddy gives each of Ed, Lucy and Henry $4.
    # Which of these two answers do you think is the total amoutn of pocket money?

    answer_1 = 2 + 4 * 3
    answer_2 = (2 + 4) * 3


    # Write a line of code to print the correct answer for the total amount of pocket money
    
    print(answer_2)

def exercise_202():

    fart = 100
    bum = 200
    bottom = 3

    toilet = bum
    fart = toilet
    print(toilet)
    print(bum)

    # what is the the value of "toilet"?
    # what is the value of "bum"
    # print the  value of "fart" added to the value of "toilet"
    lil_toilet_seat = fart + toilet
    print(lil_toilet_seat)

def exercise_203():

    # Grandads magic money machine prints 10 gold coins every day
    new_coins = 12

    # he runs it every day for a year
    days_in_a_year = 365

    # but every sunday, he gives 5 gold coins to Daddy
    daddys_coins = 10

    # there are 52 Sundays in a year
    weeks_in_a_year = 52

    # at the end of the year, Grandad gives all his leftover coins to Henry
    henrys_coins = new_coins * days_in_a_year - daddys_coins * weeks_in_a_year

    # Un-comment this line to find out how many coins Henry gets at the end of the year, and run the script to find out
    print("Henry had {} coins".format(henrys_coins))

    # Now change the machine so it makes 12 coins a day, and Grandad gives 10 coins every Sunday to Daddy.
    # How many coins does Henry get now? is Henry richer or poorer than before?

def exercise_204():
    n = random.randint(0, 2)
    foodz = ["Poop", "other poop", "more poop"]
    my_food = foodz[n]
    print("i eat {}".format(my_food))
    

exercise_200()
exercise_201()
exercise_202()
exercise_203()
exercise_204()
