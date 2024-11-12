
import string

FILE_PATH = "test.txt"
"""
with open (FILE_PATH, "w") as f:
    f.write("zadany soubory")
"""

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

#TASK 2/3

with open ("test.txt", "r") as test:
    lines = test.readlines()

lines.reverse()

with open ("task2_file", "w") as task2:
    task2.writelines(lines)


