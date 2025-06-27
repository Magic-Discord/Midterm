def get_yes_no(prompt):
    """
    Repeatedly prompt the user until they type 'yes' or 'no' (case-insensitive).
    Returns True if 'yes', False if 'no'.
    """
    while True:
        response = input(prompt).strip().lower()
        if response == "yes":
            return True
        elif response == "no":
            return False
        else:
            print("Please enter 'yes' or 'no'")
