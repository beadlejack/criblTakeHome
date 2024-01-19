# Jackson Beadle
# January 19, 2024
# Take Home Assestment
# Data Engineer -- Cribl

# Question 2 -- Consonant Substrings
# to execute: 
# $ python substrings.py -s <str> -k <int>

import argparse

VOWELS = ['a', 'e', 'i', 'o', 'u']


def consonant_substrings_max_length(instr, k):

    # case: empty string
    if not instr:
        return []

    # case: string starts with vowel
    if instr[0] in VOWELS:
        if len(instr) > 1:
            return consonant_substrings_max_length(instr[1:], k)
        else:
            return []

    # case: string starts with consonant
    # add starting letter as the first substring
    substrings = [instr[0]]
    i = 1

    # keep searching for longer consonant substrings until vowel is found or length k is reached
    while i < k and i < len(instr):
        if instr[i] in VOWELS:
            break

        substrings.append(instr[:i+1])
        i += 1

    # continue searching for substrings starting at the next letter, combining lists
    if len(instr) > 1:
        return substrings + consonant_substrings_max_length(instr[1:], k)
    else:
        return substrings


if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('-s', '--string', dest='str', default='')
    parser.add_argument('-k', '--substring-length', dest='k', default=1, type=int)
    args, unknown = parser.parse_known_args()

    print(consonant_substrings_max_length(args.str, args.k))
