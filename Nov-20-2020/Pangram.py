import string, sys


def pangram(str1, alphabet=string.ascii_lowercase):
    alphaset = set(alphabet)
    return alphaset <= set(str1.lower())


print(pangram('The quick brown fox jumps over the lazy dog'))
