#!/usr/bin/env python3

# Created by Amir Mersad
# Created on September 2019
# This program checks if the entered number is the same as the random number

import random


def main():
    # This program checks if the entered number is the same as the random
    #     random
    number_random = random.randint(1, 5)  # a number between 1 and 5

    while True:
        # Input
        number_user = input("Enter a number:  ")
        print("")

        # Process & Output
        try:
            number_int = int(number_user)

            if number_int == number_random:
                print("You are right! ")
                break
            else:
                print("You are wrong!")
                print("")

        except Exception:
            print("Wrong input!!!")


if __name__ == "__main__":
    main()
