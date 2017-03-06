import re


def clean_sequence(sequence):
    """Remove from the sequence characteres like dashes or spaces
    """

    return sequence.replace('-', '')


def validate_credit_card(sequence):
    """Validate credit card number giver the following rules:

    It must start with a 4, 5 or 6.
    It must contain exactly 16 digits.
    It must only consist of digits (0-9).
    It may have digits in groups of 4, separated by one hyphen "-".
    It must NOT use any other separator like ' ' , '_', etc.
    It must NOT have 4 or more consecutive repeated digits.
    """

    regex = r'^([456]\d{3})(-?)(\d{4})\2(\d{4})\2(\d{4})$'
    result = re.match(regex, sequence)

    if result is not None:
        return True
    else:
        return False


def validate_consecutive_digits(sequence):
    """Validate if the quantity of consecutive numbers are less than 4
    """
    count = 1

    sequence = clean_sequence(sequence)

    for i in range(1, len(sequence)):
        if sequence[i - 1] == sequence[i]:
            count += 1

            if count >= 4:
                return False
        else:
            count = 1
    return True
