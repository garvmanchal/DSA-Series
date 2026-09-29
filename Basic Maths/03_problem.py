# Check Palindrome 

# here is the simplest python versin for checking palindrome

s = input("Enter a string: ")

if s == s[::-1]:
    print("Palindrome")
else:
    print("Not a palindrome")


# DSA version
def is_palindrome(s):
    left = 0
    right = len(s) - 1

    while left < right:
        if s[left] != s[right]:
            return False

        left += 1
        right -= 1

    return True


s = input("Enter a string: ")

if is_palindrome(s):
    print("Palindrome")
else:
    print("Not Palindrome")
