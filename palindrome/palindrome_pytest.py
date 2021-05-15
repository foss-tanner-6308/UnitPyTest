from palindrome import *


def test_palindrome_good():
    # shamelessly taken from the internet for an intersting example
    exa = "Lisa Bonet ate no basil"
    exp = True
    res = pali(exa)
    assert res == exp


def test_palindrome_bad():
    exa = "Lisa Bonet ate no basilL"
    exp = True
    res = pali(exa)
    assert res == exp


def test_palindrome_nums():
    exa = "12321"
    exp = True
    res = pali(exa)
    assert res == exp