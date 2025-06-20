# get_yes_no()

This function is a reusable input validation helper. It prompts the user with a yes/no question and **repeats the prompt** until the user enters either `"yes"` or `"no"` (in any capitalization).

The function should return:
- `True` if the user types **"yes"**
- `False` if the user types **"no"**

You should ignore case and surrounding spaces. Any other input should produce the message:

```

Please enter 'yes' or 'no'

```

### Example Usage

```

Do you want to continue? maybe
Please enter 'yes' or 'no'
Do you want to continue? YES
Great! Let's go on.

```

### Requirements

- Use a loop to re-prompt as needed
- Use `.lower()` and `.strip()` to normalize input
- Return a `bool`, not a string
