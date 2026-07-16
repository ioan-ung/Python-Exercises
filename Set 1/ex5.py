def has_special_chars(text):
    special_chars = "\r\t\n\a\b\f\v"

    for char in text:
        if char in special_chars:
            return True

    return False


text = "Hello\nWorld"

print(has_special_chars(text))