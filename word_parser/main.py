__author__ = 'funso'

import argparse

OPTION_ENGLISH_DICTIONARY = 0
OPTION_SELECTED_WORDS = 1

spell_check_means = OPTION_SELECTED_WORDS

known_words = [
    "race", "racer", "dark", "skin", "skinned", "ugly", "good", "looking", "good-looking",
    "rich", "generous", "small", "dick", "cum", "cums", "in", "ten", "tens",
    "minute", "minutes", "or", "for", "less", "excess", "ice", "cream", "icecream"
]

results = []

def spell_check(word):
    if spell_check_means == OPTION_SELECTED_WORDS:
        return is_known_word(word)
    else:
        return is_word_in_dict(word)

def is_word_in_dict(word):
    return True

def is_known_word(word):
    return word in known_words

def break_string_to_words(string):
    break_string(string, len(string), "")

def break_string(string, size, accumulator):
    for i in range(1, size + 1):
        sub_string = string[:i]
        if spell_check(sub_string):
            if i == size:
                accumulator += sub_string
                results.append(accumulator)
                break
            break_string(string[i:], size - i, accumulator + sub_string + " ")


def run():
    parser = argparse.ArgumentParser(description="Breaks String Into Possible Words :)")
    parser.add_argument('-o', '--option', type=int, default=0,
                        help="Spell Check Option: use 0 to enable Dictionary Check "
                             "\n\t\t use 1 to enable Word List Check")
    parser.add_argument('-s', '--string', type=str,
                        default="darkskinneduglygoodlookingrichgeneroussmalldickcumsintenminutesorless",
                        help="The String to break into words")
    args = parser.parse_args()
    global spell_check_means
    spell_check_means = args.option
    string = args.string
    break_string_to_words(string)
    if results:
        print "String Parsed Successfully!"
        for sentence in results:
            print sentence
    else:
        print "String Parsing Failed! Check the string for nonexistent words :("

if __name__ == '__main__':
    run()
