from wordcount import *


def test_wordcount_good():
    exa = "I hope this works"
    exp = 4
    res = wordcount(exa)
    assert res == exp


def test_wordcount_bad():
    exa = "This should not work"
    exp = 5
    res = wordcount(exa)
    assert res == exp


def test_wordcount_nums():
    exa = "1 2 3 4 5"
    exp = 5
    res = wordcount(exa)
    assert res == exp