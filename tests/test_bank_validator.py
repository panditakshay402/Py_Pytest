# tests/test_bank_validator.py

import pytest

from src.bank_validator import *


# =========================
# TASK 1 EMAIL TESTS
# =========================

@pytest.mark.parametrize("email, expected", [

    ("user@mail.com", True),
    ("test.user@company.co.uk", True),

    ("", False),
    ("notanemail", False),
    ("@nodomain", False),
    ("missingdomain@", False)

])

@pytest.mark.regression
def test_email_validation(email, expected):
    assert is_valid_email(email) == expected


# =========================
# TASK 2 PASSWORD TESTS
# =========================

@pytest.mark.parametrize("password, expected", [

    ("Short1!", False),
    ("Valid@123", True),
    ("lowercase1@", False),
    ("UPPERCASE1@", False),
    ("NoNumber@", False),
    ("NoSpecial123", False),
    ("ValidPass1@", True)

], ids=[

    "too-short",
    "valid-1",
    "no-uppercase",
    "no-lowercase",
    "no-digit",
    "no-special",
    "valid-2"

])

def test_password_validation(password, expected):
    assert is_valid_password(password) == expected


# =========================
# TASK 3 AMOUNT TESTS
# =========================

@pytest.mark.parametrize("amount, expected", [

    (0.00, False),
    (0.01, True),
    (250.00, True),
    (500.00, True),
    (500.01, False),
    (-10.00, False)

])

@pytest.mark.regression
def test_amount_validation(amount, expected):
    assert is_valid_transfer_amount(amount) == expected


# =========================
# TASK 4 FEE TESTS
# =========================

def test_fee_for_small_amount():
    assert calculate_transfer_fee(50.00) == 1.00


def test_fee_for_medium_amount():
    assert calculate_transfer_fee(150.00) == 2.50


def test_fee_for_large_amount():
    assert calculate_transfer_fee(400.00) == 5.00


def test_fee_for_boundary_amounts():
    assert calculate_transfer_fee(100.00) == 1.00
    assert calculate_transfer_fee(100.01) == 2.50


def test_fee_raises_for_invalid_amount():
    with pytest.raises(ValueError):
        calculate_transfer_fee(0.00)


# =========================
# TASK 5 MASK TESTS
# =========================

def test_mask_long_account_number():
    assert mask_account_number("12345678") == "****5678"


def test_mask_exactly_four_digits():
    assert mask_account_number("1234") == "1234"


def test_mask_short_account_number():
    assert mask_account_number("12") == "12"


# =========================
# TASK 6 FIXTURE TEST
# =========================

def test_transfer_data_is_valid(valid_transfer_data):

    amount = valid_transfer_data["amount"]

    assert is_valid_transfer_amount(amount) is True

    assert calculate_transfer_fee(amount) == 2.50


# =========================
# TASK 7 MARKERS
# =========================

@pytest.mark.smoke
def test_valid_email_accepted():
    assert is_valid_email("abc@test.com") is True


@pytest.mark.xfail(reason="International fee not implemented")
def test_international_transfer_fee():
    assert calculate_transfer_fee(500.00, currency="USD") == 7.50