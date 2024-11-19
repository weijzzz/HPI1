# weijie
# Mappings for numbers to words
below_20 = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten",
            "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
tens = ["", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
thousands = ["", "Thousand", "Million", "Billion"]


def number_to_words(num):
    """
    Converts a number to its English word representation.

    Args:
    - num (int): The positive integer to convert to words.

    Returns:
    - str: The English word representation of the number.
    """
    if num == 0:
        return "Zero"

    def helper(num):
        """Helper function to convert numbers below 1000 to words."""
        if num == 0:
            return ""
        elif num < 20:
            return below_20[num]
        elif num < 100:
            return tens[num // 10] + " " + helper(num % 10)
        else:
            return below_20[num // 100] + " Hundred " + helper(num % 100)

    res = ""
    for i in range(len(thousands)):
        if num % 1000 != 0:
            res = helper(num % 1000) + " " + thousands[i] + " " + res
        num //= 1000

    return res.strip()


# Get the number from the user input
num = input("Give me a number: ")

# Convert the input to an integer
try:
    num = int(num)  # Convert input to integer
    print(f"The number {num} in words is: {number_to_words(num)}")
except ValueError:
    print("Please enter a valid number.")
