
import string

FILE_PATH = "test.txt"

with open (FILE_PATH, "w") as f:
    f.write("zadany soubory")

long_words = []

with open(FILE_PATH, "r") as f:
    text = f.read()
    text = text.translate(str.maketrans('', '', string.punctuation))
    words = text.split()
    for n in words:
        if len(n) >=7:
            long_words.append(n)


NOVY = "task1_file"
with open (NOVY, "w") as new:
    for i in long_words:
        new.write(i + "\n")

