def is_palindrome(string: str) -> bool:
    """
    This function will identify if the string is a palindrome.
    A palindrome is a string that reads the same forwards as backwards.

    :param string: The text that the user will input.
    :return: The function will return the text if the input is a palindrome.
    """
    return string[::-1].casefold() == string.casefold()


def palindrome_sentence(sentence: str) -> bool:
    """
    Check if a sentence is a palindrome.

    The function ignores whitespace, capitalisation
    and punctuation in the sentence.

    :param sentence: The sentence the user will input
    :return: The function will return `True` if `sentence` is a palindrome, or will return `False` if `sentence` is not a palindrome.
    """

    string = ""
    for char in sentence:
        if char.isalnum():
            string += char
    return is_palindrome(string)


def fibonacci(n: int) -> int:
    """Return the `n` th Fibonacci number, for positive `n`."""
    if 0 <= n <= 1:
        return n

    n_minus1, n_minus2 = 1, 0

    result = None
    for f in range(n - 1):
        result = n_minus1 + n_minus2
        n_minus2 = n_minus1
        n_minus1 = result

    return result


def factorial(number: int) -> int:
    result = 1
    for i in range(0, number + 1):
        if i < 1:
            pass

        if i >= 1:
            result = i * result

    return result
