#!/usr/bin/env python3

# Created by: Ahmad El-khawaldeh
# Created on: December 2020
# This program adds numbers user inputs


def main():
    while True:
        # input
        number_of_inputs_string = input
        ("How many numbers would you like to add together?: ")
        try:
            number_of_inputs = int(number_of_inputs_string)

            assert number_of_inputs > 0

            break

        except AssertionError:
            print("This number is negative")
        except Exception:
            ("This is not a number")

    sum = 0

    loop_counter = 0

    while loop_counter < number_of_inputs:
        loop_counter = loop_counter + 1

        while True:
            input_number_string = input("Enter number to add: ")

            try:
                input_number = int(input_number_string)
                assert input_number > 0
                break
            except AssertionError:
                print("This number is negative")
            except Exception:
                print("This is not a number")
        sum = sum + input_number

        if loop_counter < number_of_inputs:
            continue
        print("The sum of all positive numbers is: {}".format(sum))


if __name__ == "__main__":
    main()
