#!/usr/bin/env python

import argparse

parser = argparse.ArgumentParser(description="Main program")
parser.add_argument('--test', type=bool, default=False)

args = parser.parse_args()

PROGRAM_NAME = "loop"

def gen_menu_entry(keyword, description):
    return f" * {keyword:<20s} - {description}"

def print_menu():
    print("============================")
    print(gen_menu_entry("exit", "Exit program"))
    print(gen_menu_entry("help (?)", "Print help menu"))
    print("============================")

def run_loop():
    while True:
        word = input("Input: ")

        if word == 'exit':
            print(f"Exit program!")
            break
        elif word == 'help' or word == '?':
            print_menu()
        else:
            print(f"{word}")

if __name__ == '__main__':
    run_loop()
