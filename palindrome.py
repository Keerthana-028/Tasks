#It is a simple python script which is used to check whether the given string is palindrome or not.

class Palindromeclass:
    """
    The class is used to check the given string is palindrome.
    """

    def __init__(self, palindromeInput):
        """It initialies the palindromeclass with the input string.
        """
        self.palindromeInput = palindromeInput
    #Defining function
    def palindromeChecker(self):
        """check the input string is palindrome.
        prints It is a panlindrome if it is same forwards and backwards,
        Else it will print It is not a palindrome"""
        #using if-else statement
        if self.palindromeInput == self.palindromeInput[::-1]:
            print("It is a Palindrome")
        else:
            print("It is not a palindrome")

def main():
    """It will runs the palindrome check .
    And ask the user to give the input string,creates an instance of Palindromeclass
    and call te palindromeChecker to check the input is palindrome or not
    """
    palindromeInput = input("enter the input: ")
    palindromeObj = Palindromeclass(palindromeInput=palindromeInput)
    #using the function
    return palindromeObj.palindromeChecker()

if __name__ == "__main__":
    main()

