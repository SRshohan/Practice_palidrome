
def palindrome(x):
    if x < 0:
        return False

    original = x
    reversed_num = 0 # Initializing the reverse_num. Because we gonna use the formula

    while x > 0:
        digit = x % 10
        reversed_num = reversed_num * 10 + digit  # Formula to reverse
        x //= 10

    return original == reversed_num

print(palindrome(121))  # True
print(palindrome(-121)) # False
print(palindrome(10))   # False