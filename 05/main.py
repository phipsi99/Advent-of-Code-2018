import string

from tqdm import tqdm
from helpers.get_input import get_lines

def do_main(debug_mode=False):
    lines = get_lines('05', debug_mode)

    letters_lower = list(string.ascii_lowercase)
    letters_upper = list(string.ascii_uppercase)
    lookup_zip = []
    lookup_zip.extend(zip(letters_lower, letters_upper))
    lookup_zip.extend(zip(letters_upper, letters_lower))

    lookup = []
    for l, u in lookup_zip:
        lookup.append(l+u)

    point_sum = 0

    polymer = lines[0][:]

    old_len = 0
    new_len = len(polymer)
    while old_len != new_len:
        old_len = new_len
        for c in lookup:
            if c in polymer:
                polymer = polymer.replace(c, '')
        new_len = len(polymer)
    print(len(polymer))

    min_polymer = new_len
    for letter in tqdm(letters_lower):
        polymer = lines[0][:]
        polymer = polymer.replace(letter, '')
        polymer = polymer.replace(letter.upper(), '')
        old_len = 0
        new_len = len(polymer)
        while old_len != new_len:
            old_len = new_len
            for c in lookup:
                if c in polymer:
                    polymer = polymer.replace(c, '')
            new_len = len(polymer)
        min_polymer = min(min_polymer, len(polymer))

    print(min_polymer)


if __name__ == '__main__':
    do_main(False)