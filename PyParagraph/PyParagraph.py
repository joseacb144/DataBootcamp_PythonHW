import re
import csv
import os

#Create file path to read in the text file
filepath = os.path.join("raw_data/paragraph_1.txt")

with open(filepath, 'r') as text:
    lines = text.read()

#The file is called 'lines'

#Split the text to equal word_count
word_count = lines.split()

#Split the text to equal sentence_count
sentence_count = re.split(r'\.|\.\s|\.$', lines)

#Find the average letter count
average = sum(len(word) for word in word_count) / len(word_count)

#Find the average sentence length
avg_len = sum(len(x.split()) for x in sentence_count) / len(sentence_count)

#Print out answer
print("Paragraph Analysis")
print("---------------------")
print ("Approximate Word Count: "  + str(len(word_count)))
print ("Approximate Sentence Count: " + str(len(sentence_count)))
print("Average Letter Count: " + str(average))
print("Average Sentence Length: " + str(avg_len))