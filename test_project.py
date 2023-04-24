import pytest
from project import check_num_passwords
from project import check_pw_is_valid_length
from project import check_is_valid_numbers
from project import check_is_valid_symbols

def main():
     test_amount_passwords()
     test_size()
     test_valid_num()
     test_valid_symb()

def test_amount_passwords():
     with pytest.raises(OSError):
          amount_passwords = 0
          assert check_num_passwords() == "Amount of passwords must at least be 1."

def test_size():
     with pytest.raises(OSError):
          number_letters = 2
          assert check_pw_is_valid_length() == "Input of characters must be at least 5."

def test_valid_num():
     with pytest.raises(OSError):
          assert check_is_valid_numbers(2) == "Input of letters must be at least 5."
     with pytest.raises(OSError):
          assert check_is_valid_numbers("zero") == 0

def test_valid_symb():
     with pytest.raises(OSError):
          number_symbols = -2
          assert check_is_valid_symbols(5, 15) == "Please enter a non-negative integer"

if __name__ == "__main__":
    main()
