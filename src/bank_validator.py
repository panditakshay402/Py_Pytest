import re


def is_valid_email(email: str) -> bool:
    if "@" not in email:
        return False

    parts = email.split("@")

    if len(parts) != 2:
        return False

    domain = parts[1]

    return "." in domain


def is_valid_password(password: str) -> bool:
    # length 8-16
    if len(password) < 8 or len(password) > 16:
        return False

    # uppercase
    if not re.search(r"[A-Z]", password):
        return False

    # lowercase
    if not re.search(r"[a-z]", password):
        return False

    # digit
    if not re.search(r"[0-9]", password):
        return False

    # special char
    if not re.search(r"[@#$!%]", password):
        return False

    return True


def is_valid_transfer_amount(amount: float) -> bool:
    return 0.01 <= amount <= 500.00


def calculate_transfer_fee(amount: float) -> float:
    if not is_valid_transfer_amount(amount):
        raise ValueError("Invalid amount")

    if 0.01 <= amount <= 100:
        return 1.00

    elif 100.01 <= amount <= 250:
        return 2.50

    elif 250.01 <= amount <= 500:
        return 5.00


def mask_account_number(account_number: str) -> str:
    if len(account_number) <= 4:
        return account_number

    stars = "*" * (len(account_number) - 4)

    return stars + account_number[-4:]