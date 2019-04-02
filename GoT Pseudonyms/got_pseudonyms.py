"""Generate Funny GoT Themed Names by Randomly Combining First and Last Names"""
import random
from termcolor import colored
from first_names import first
from last_names import last


def main():
    """Choose First/Last names at random from 2 lists of names and print to Teminal"""
    while True:
        print("Winter is coming to Westeros! ")
        print("Only you can save us: \n")

        first_name = random.choice(first)
        last_name = random.choice(last)

        print("\n\n")
        # Use 'colored' from termcolor to color the name red
        print(colored('{} {}', 'red').format(first_name, last_name))
        print("\n\n")

        try_again = input("\n\nPress Enter to Try Again or 'q' to quit\n ")
        if try_again.lower() == 'q':
            break

if __name__ == "__main__":
    main()
