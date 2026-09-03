"""
Exercise 12: Date Validator & Pretty Formatter
Write a program that prompts the user to enter a date string in the format "DD/MM/YYYY".

Do not use any built-in date/time library functions.
Parse and split the string manually, and use a custom tuple of month names.
"""

MONTH_NAMES = (
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
)


def is_leap_year(year: int) -> bool:
    """A year is leap if divisible by 4, except century years not divisible by 400."""
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)


def get_days_in_month(month: int, year: int) -> int:
    """Returns the total number of valid days for a given month and year."""
    if month in (4, 6, 9, 11):
        return 30
    elif month == 2:
        return 29 if is_leap_year(year) else 28
    else:
        return 31


def main():
    date_str = input("Enter a date (DD/MM/YYYY): ").strip()

    # Split into components
    parts = date_str.split("/")
    if len(parts) != 3:
        print("Invalid Date")
        return

    # Validate numeric casting
    try:
        day = int(parts[0])
        month = int(parts[1])
        year = int(parts[2])
    except ValueError:
        print("Invalid Date")
        return

    # Check year validity
    if year <= 0:
        print("Invalid Date")
        return

    # Check month validity (1 to 12)
    if month < 1 or month > 12:
        print("Invalid Date")
        return

    # Check day validity for the given month and year
    max_days = get_days_in_month(month, year)
    if day < 1 or day > max_days:
        print("Invalid Date")
        return

    # Format pretty output using the month names tuple
    month_name = MONTH_NAMES[month - 1]
    # Preserve 2-digit day format or display as parsed int matching the sample output
    print(f"{month_name} {day:02d}, {year}")


if __name__ == "__main__":
    main()