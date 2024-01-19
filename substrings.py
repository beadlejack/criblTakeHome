"""
Jackson Beadle
January 19, 2024
Take Home Assessment
Data Engineer -- Cribl

Question 2 -- Consonant Substrings
to execute:
$ python substrings.py -s <str> -k <int>

Assumption: lowercase and uppercase characters should be treated as different characters
    i.e. aA != aa != AA != Aa
"""

import argparse

VOWELS = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']


def consonant_substrings_max_length(instr, k):
    """Function for finding all unique consonant substrings with length <= k.

    :param instr: Input string
    :type instr: str
    :param k: Maximum length of consonant substrings to find
    :type k: int
    :return: List of consonant substrings
    :rtype: list(str)
    """

    # case: empty string
    if not instr:
        return []

    # case: string starts vowel or non-alpha character
    if not instr[0].isalpha() or instr[0] in VOWELS:
        if len(instr) > 1:
            return consonant_substrings_max_length(instr[1:], k)
        else:
            return []

    # case: string starts with consonant
    # add starting letter as the first substring
    substrings = [instr[0]]
    i = 1

    # keep searching for longer consonant substrings until vowel/non-alpha character is found or length k is reached
    while i < k and i < len(instr):
        if not instr[i].isalpha() or instr[i] in VOWELS:
            break

        substrings.append(instr[:i+1])
        i += 1

    # continue searching for substrings starting at the next letter, combining lists
    if len(instr) > 1:
        # need to deduplicate list
        return list(set(substrings + consonant_substrings_max_length(instr[1:], k)))
    else:
        return substrings


if __name__ == '__main__':

    # get the runtime arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('-s', '--string', dest='str', default='')
    parser.add_argument('-k', '--substring-length', dest='k', default=1, type=int)
    args, unknown = parser.parse_known_args()

    # printing sorted list for readability
    print(sorted(consonant_substrings_max_length(args.str, args.k)))
