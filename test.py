import database_of_students
from time import sleep
import random


def random_digit(word):
    if word == "5а":
        database_of_students.fifthAcount = random.randint(0, 3)
    elif word == "6а":
        database_of_students.sixthAcount = random.randint(0, 1)
