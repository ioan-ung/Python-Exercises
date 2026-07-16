import re


def count_words(text):
    words = re.split(r"[ ,;?!\.]+", text)

    words = [word for word in words if word]
    return len(words)


text = "Ana, are un câine! El este mare."
print(count_words(text))