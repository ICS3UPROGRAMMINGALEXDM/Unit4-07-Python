#!/usr/bin/env python3

# Created By: Alex De Meo
# Date: 03/25/2022
# Description: Displays every number between 1000-2000 and only prints
# five numbers per line
def main():
    for number in range(1000, 2001):
        if (number != 1000) and (number % 5 == 0):
            print("\n{} ".format(number), end="")
        else:
            print("{} ".format(number), end="")


if __name__ == "__main__":
    main()
