def main():
    """
    Repeatedly ask the user for numbers. Stop when the user enters 0.
    At the end, print how many *positive* numbers were entered.
    """
    count = 0
    while True:
        try:
            number = int(input("Enter a number: "))
            if number == 0:
                break
            if number > 0:
                count += 1
        except ValueError:
            print("Please enter a valid number.")
    print(f"You entered {count} positive number(s).")
