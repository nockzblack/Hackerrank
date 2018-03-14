#!/usr/local/bin/python3

import sys


def repeatedString(s, n):
    # First know the pos of all a's in the word
    letters_a = letters_in_word("a", s)
    # how many words are in n letters
    words_in_n = n // len(s)
    # nuber of letters in just one word
    n_of_a = len(letters_a)
    # make the word incompleted could be empty
    incompleted_word = s[0:n % len(s)]
    # get pos of the a's in the incompleted word
    others_a = letters_in_word("a", incompleted_word)
    total = n_of_a * words_in_n + len(others_a)

    return total

	
# this func receives a letter and a word. Return an array with pos
# of the letters
def letters_in_word(letter, word):
    letters_pos = []
    for i in range(len(word)):
        if word[i] == letter:
            letters_pos.append(i)

    return letters_pos


if __name__ == "__main__":
    s = input().strip()
    n = int(input().strip())
    result = repeatedString(s, n)
    print(result)
