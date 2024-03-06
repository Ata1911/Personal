import cs50
import sys

text = cs50.get_string("Text: ")


if not text:
    print("No text have been inserted")
    sys.exit()


def counter(text):
    words = 1
    letters = 0
    sentences = 0
    for text in text:
        i = 0
        if text[i] == " ":
            words += 1
        if text[i] == "." or text[i] == "?" or text[i] == "!":
            sentences += 1

        if text[i].isalpha():
            letters += 1
    L = (letters / words) * 100
    S = (sentences / words) * 100
    index = round((0.0588 * L) - (0.296 * S) - 15.8)
    if index < 1:
        print("Before Grade 1")
    elif index > 16:
        print("Grade 16+")
    else:
        print(f"Grade {index}")


counter(text)
