#!/usr/bin/env python

import argparse

parser = argparse.ArgumentParser(description="Main program")

parser.add_argument('--test', type=bool, default=False)

args = parser.parse_args()

def runLoop():
    while True:
        word = input("Input: ")

        if word == 'exit':
            print(f"Exit program!")
            break
        elif word == 'help' or word == '?':
            printMenu()
        else:
            print(f"{word}")

if __name__ == '__main__':
    runLoop()