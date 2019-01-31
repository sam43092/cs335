import string
fhand = open("Hemingway.txt")
for fline in fhand:
    fline = fline.rstrip()
    print(fline.translate(string.punctuation))