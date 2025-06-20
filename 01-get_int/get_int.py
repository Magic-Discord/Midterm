def get_int(prompt, min_val, max_val):
    """
    Retrieve a number from a user between the specified values.

    THIS IS A DOCSTRING!! "Good" Python functions will have them. Typically they
    will simply document what a function does and how to use it. It is simply a
    multi-line string starting and ending with three single- or double-quotes.

    Importantly, it must start on the FIRST LINE below the function definition
    line. The Python code you write to implement the function will start AFTER
    the docstring.
    """
    return int(input(prompt))  # REPLACE ME!!!


###############################################################################
# main function. Look but no need to touch.
###############################################################################


def main():
    """Main entry point for the program."""
    user_num = get_int("Enter a number between 1 and 5: ", 1, 5)
    print(user_num)
    user_num = get_int("Enter a number between 10 and 20: ", 10, 20)
    print(user_num)


if __name__ == "__main__":
    main()
