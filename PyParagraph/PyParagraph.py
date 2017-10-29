import re
import csv
import os

filepath = os.path.join("raw_data/paragraph_1.txt")

with open(filepath, 'r') as text:
    lines = text.read()

mystring = lines

word_count = mystring.split()

sentence_count = re.split(r'\.|\.\s|\.$', lines)

words = mystring.split()


average = sum(len(word) for word in words) / len(words)

avg_len = sum(len(x.split()) for x in sentence_count) / len(sentence_count)


print("Paragraph Analysis")
print("---------------------")
print ("Approximate Word Count: "  + str(len(word_count)))
print ("Approximate Sentence Count: " + str(len(sentence_count)))
print("Average Letter Count: " + str(average))
print("Average Sentence Length: " + str(avg_len))