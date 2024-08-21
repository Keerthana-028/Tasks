
def is_palindrome(input):
    return input == input[::-1]
def main():
    user_input = input("Enter the string:")
    output = is_palindrome(input=user_input)
    if output:
        print('The given string is a palindrome.')
    else:
        print('It is not a palindrome.')

if __name__ == "__main__":
    main()
