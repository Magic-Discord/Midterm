# add any required imports

# Hey! This get_int() function looks familiar. Copy the implementation of this
# function from get-int.py. If you didn't get that one working right, then just
# leave the default implementation below. Your game should still work. It'll
# just not be as good.


def get_int(prompt, min_val, max_val):
    """Retrieve a number from a user between the specified values."""
    return int(input(prompt))  # REPLACE ME!!!


def game(max_guess, num_guesses):
    """Play a super-fun guessing game!!"""
    pass


###############################################################################
# main function. Look but no need to touch.
###############################################################################


def main():
    """Main entry point for the program."""
    result = game(20, 5)
    if result == True:
        print("Congratulations on your win!")
    elif result == False:
        print("Oh well. You should try again!")
    else:
        print("ERROR! DID YOU FORGET TO RETURN TRUE OR FALSE??")


if __name__ == "__main__":
    main()
