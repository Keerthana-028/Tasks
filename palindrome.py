#  It is a simple python script which is used to check whether
# the given string is palindrome or not.

import re
import pytest


class Palindromeclass:
    """The class is used to check if the given string is a palindrome."""
    def __init__(self, palindromeInput):
        """Initialize the Palindromeclass with the input string."""
        self.palindromeInput = palindromeInput

    def palindromeChecker(self):
        """Check if the input string is a palindrome."""
        cleaned_input = re.sub(
            r'[^a-zA-Z0-9]', '', self.palindromeInput.lower()
        )
        return cleaned_input == cleaned_input[::-1]


def main():
    """Run the palindrome check."""
    palindromeInput = input("Enter the input: ")
    palindromeObj = Palindromeclass(palindromeInput=palindromeInput)
    if palindromeObj.palindromeChecker():
        print("It is a palindrome")
    else:
        print("It is not a palindrome")


if __name__ == "__main__":
    main()


def test_palindrome():
    """Test the Palindromeclass palindromeChecker
    method with various inputs."""
    palindrome_obj = Palindromeclass("madam")
    assert palindrome_obj.palindromeChecker() == True
    palindrome_obj = Palindromeclass("amma")
    assert palindrome_obj.palindromeChecker() == True
    palindrome_obj = Palindromeclass("malayalam")
    assert palindrome_obj.palindromeChecker() == True
    palindrome_obj = Palindromeclass("1234321")
    assert palindrome_obj.palindromeChecker() == True
    palindrome_obj = Palindromeclass(
        "Madam, I'm Adam!!"
    )
    assert palindrome_obj.palindromeChecker() == True
    palindrome_obj = Palindromeclass("happy")
    assert palindrome_obj.palindromeChecker() == False
    palindrome_obj = Palindromeclass("sad")
    assert palindrome_obj.palindromeChecker() == False
    palindrome_obj = Palindromeclass("cat")
    assert palindrome_obj.palindromeChecker() == False
