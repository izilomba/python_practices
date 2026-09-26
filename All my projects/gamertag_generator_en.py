def header():
    """Displays the application header."""
    border = "="
    side = "|"
    title = f"""{border * 89}
{side}                                                              {side}
{side}   ____                                _                      {side}
{side}  / ___|  __ _  _ __ ___    ___  _ __ | |_  __ _   __ _  ___  {side}
{side} | |  _  / _` || '_ ` _ \\  / _ \\| '__|| __|/ _` | / _` |/ __| {side}
{side} | |_| || (_| || | | | | ||  __/| |   | |_| (_| || (_| |\\__ \\ {side}
{side}  \\____| \\__,_||_| |_| |_| \\___||_|    \\__|\\__,_| \\__, ||___/ {side}
{side}                                                  |___/       {side}
{side}                                                              {side}
{border * 89}"""
    print(title)


def create_basic_tag(name):
    """
    Creates a basic gamertag using the first 4 letters.

    Parameter:
    name (str): User's name

    Returns:
    str: Basic gamertag
    """
    return name[:4]


def create_reversed_tag(name):
    """
    Creates a gamertag by reversing the full name.

    Parameter:
    name (str): User's name

    Returns:
    str: Reversed gamertag
    """
    return name[::-1]


def create_interleaved_tag(name, surname):
    """
    Creates a gamertag combining name and surname.

    Parameters:
    name (str): User's name
    surname (str): User's surname

    Returns:
    str: Interleaved gamertag
    """
    first_letter_name = name[0]
    first_letter_surname = surname[0]
    rest_name = name[1:]
    rest_surname = surname[1:]

    tag = (
        first_letter_name
        + first_letter_surname
        + rest_name
        + rest_surname
    )

    return tag


def create_elite_tag(name):
    """
    Creates an "elite" gamertag using the start and end of the name.

    Example:
    "Pablo" -> "Palo"

    Parameter:
    name (str): User's name

    Returns:
    str: Elite gamertag
    """
    return name[:2] + name[-2:]


def create_numeric_tag(name, favorite_number):
    """
    Creates a gamertag using the first 5 letters of the name
    and the favorite number.

    Parameters:
    name (str): User's name
    favorite_number (int): User's favorite number

    Returns:
    str: Numeric gamertag
    """
    return name[:5] + str(favorite_number)


def show_statistics(name):
    """
    Displays statistics about the given name.

    Parameter:
    name (str): Name to analyze

    Returns:
    None
    """
    name_length = len(name)

    print("\n📊 YOUR NAME STATISTICS:")
    print(f"FULL NAME: {name}")
    print(f"NAME LENGTH: {name_length}")
    print(f"FIRST LETTER: {name[0]}")
    print(f"LAST LETTER: {name[-1]}")


def generate_all_options(name, surname, favorite_number):
    """
    Generates and displays all gamertag options.

    Parameters:
    name (str): User's name
    surname (str): User's surname
    favorite_number (int): User's favorite number

    Returns:
    None
    """
    basic_tag = create_basic_tag(name)
    reversed_tag = create_reversed_tag(name)
    interleaved_tag = create_interleaved_tag(name, surname)
    elite_tag = create_elite_tag(name)
    numeric_tag = create_numeric_tag(name, favorite_number)

    print("\n========================================")
    print("🎯 YOUR GAMERTAG OPTIONS:")
    print("========================================")

    print(f"1. BASIC TAG: {basic_tag}")
    print(f"2. REVERSED TAG: {reversed_tag}")
    print(f"3. INTERLEAVED TAG: {interleaved_tag}")
    print(f"4. ELITE TAG: {elite_tag}")
    print(f"5. NUMERIC TAG: {numeric_tag}")


# ===========================================
# MAIN APPLICATION
# ===========================================

header()

name = input("Enter your name: ")
surname = input("Enter your surname: ")

while True:
    number_input = input("Enter your favorite number: ")
    if number_input.isdigit():
        favorite_number = int(number_input)
        break
    print("Please enter a valid integer.")

show_statistics(name)

generate_all_options(
    name,
    surname,
    favorite_number
)
