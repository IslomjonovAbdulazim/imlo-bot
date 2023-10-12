from uzwords import words
from difflib import get_close_matches


def check_word(word, word_list=words):
    w = word.lower()
    matches = set(get_close_matches(word, word_list))
    available = False

    if w in matches:
        available = True
        matches = word
    return {"available": available, "matches": matches}
