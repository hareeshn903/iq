import logging

# Configure logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

# 1. Reverse a string without using built-in functions.
def reverse_string(s):
    logging.info("Starting to reverse the string.")
    reversed_str = ""
    for char in s:
        logging.debug(f"Current character: {char}")
        reversed_str = char + reversed_str
        logging.debug(f"Reversed string so far: {reversed_str}")
    logging.info("Finished reversing the string.")
    return reversed_str

# Example usage
input_string = "hello"
result = reverse_string(input_string)
print(f"Original string: {input_string}")
print(f"Reversed string: {result}")


# 2. Check if a number is prime.
def is_prime(num):
    logging.info(f"Checking if {num} is a prime number.")
    if num <= 1:
        logging.debug(f"{num} is not prime (less than or equal to 1).")
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            logging.debug(f"{num} is divisible by {i}, so it is not prime.")
            return False
    logging.info(f"{num} is a prime number.")
    return True

# Example usage
number = 29
is_prime_result = is_prime(number)
print(f"Is {number} a prime number? {is_prime_result}")


# 3. Find the sum of digits of a number.
def sum_of_digits(n):
    logging.info(f"Calculating the sum of digits for {n}.")
    total = 0
    while n > 0:
        digit = n % 10
        logging.debug(f"Extracted digit: {digit}")
        total += digit
        n //= 10
        logging.debug(f"Intermediate sum: {total}, Remaining number: {n}")
    logging.info(f"Total sum of digits: {total}")
    return total

# Example usage
number = 12345
sum_result = sum_of_digits(number)
print(f"Sum of digits of {number}: {sum_result}")


# 4. Check if a number is a palindrome.
def is_palindrome_number(num):
    logging.info(f"Checking if {num} is a palindrome.")
    original_num = num
    reversed_num = 0

    while num > 0:
        digit = num % 10
        reversed_num = reversed_num * 10 + digit
        num //= 10
        logging.debug(f"Reversed number so far: {reversed_num}, Remaining number: {num}")

    if original_num == reversed_num:
        logging.info(f"{original_num} is a palindrome.")
        return True
    else:
        logging.info(f"{original_num} is not a palindrome.")
        return False
# 5. Find the factorial of a number (iterative & recursive).
# 6. Count vowels and consonants in a string.
# 7. Check if a string is anagram of another.
# 8. Print the Fibonacci series up to `n` terms.
# 9. Find the largest and smallest number in a list.
# 10. Remove duplicates from a list.
# 11. Count occurrences of each element in a list.
# 12. Swap two numbers without using a third variable.
# 13. Find the GCD (Greatest Common Divisor) of two numbers.
# 14. Find the LCM (Least Common Multiple) of two numbers.
# 15. Check if a year is a leap year.
# 16. Convert Celsius to Fahrenheit and vice versa.
# 17. Find the length of a string without using built-in functions.
# 18. Check if a string is a palindrome.
# 19. Find the second largest number in a list.
# 20. Merge two sorted lists into a single sorted list.
# 21. Find the sum of all elements in a list.
# 22. Reverse a list without using built-in functions.
# 23. Check if a list is sorted.
# 24. Find the common elements between two lists.
# 25. Flatten a nested list.
# 26. Find the first non-repeating character in a string.
# 27. Check if a string contains only digits.

