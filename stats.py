def get_num_words(text):
    words = text.split()
    return len(words)

def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars

def sort_on(dict):
    return dict["num"]

def sort_chars_list(dict):
    result = []
    for c in dict:
        result.append({"char": c, "num": dict[c]})
    result.sort(reverse=True, key=sort_on)
    return result