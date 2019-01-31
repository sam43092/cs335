#!/usr/bin/python -tt
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

"""Wordcount exercise
Google's Python class

The main() below is already defined and complete. It calls print_words()
and print_top() functions which you write.

1. For the --count flag, implement a print_words(filename) function that counts
how often each word appears in the text and prints:
word1 count1
word2 count2
...

Print the above list in order sorted by word (python will sort punctuation to
come before letters -- that's fine). Store all the words as lowercase,
so 'The' and 'the' count as the same word.

2. For the --topcount flag, implement a print_top(filename) which is similar
to print_words() but which prints just the top 20 most common words sorted
so the most common word is first, then the next most common, and so on.

Use str.split() (no arguments) to split on all whitespace.

Workflow: don't build the whole program at once. Get it to an intermediate
milestone and print your data structure and sys.exit(0).
When that's working, try for the next milestone.

Optional: define a helper function to avoid code duplication inside
print_words() and print_top().

"""

import sys
import string


# +++your code here+++
# Define print_words(filename) and print_top(filename) functions.
# You could write a helper utility function that reads a file
# and builds and returns a word/count dict for it.
# Then print_words() and print_top() can just call the utility function.

def create_dict(filename):
  count_words = {}
  infile = open(filename, 'r')
  
 
  
  for entry in infile:
    words = entry.strip().split()
    for word in words:
      word = word.lower()
      word = word.translate(None, string.punctuation)
  
  # if the word has not been seen yet count = 1
  # if it has, match the word and increase count by 1
      if not word in count_words:
        count_words[word] = 1
      else:
        count_words[word] += 1
    
  return count_words
 
#******************** 
def print_words(filename):
  
  count_words = create_dict(filename)
  
  new_words = sorted(count_words.keys())
  
  for word in new_words:
    print word, count_words[word]

#*********************
def count(Tuple):
  return Tuple[1]  

#*********************
def print_top(filename):
  count_words = create_dict(filename)
  highcount = sorted(count_words.items(), key=count, reverse = True)
  
  for item in highcount[:20]:
    print item[0], item[1]
  
  
# This basic command line argument parsing code is provided and
# calls the print_words() and print_top() functions which you must define.
def main():
  if len(sys.argv) != 3:
    print 'usage: ./wordcount.py {--count | --topcount} file'
    sys.exit(1)

  option = sys.argv[1]
  filename = sys.argv[2]
  if option == '--count':
    print_words(filename)
  elif option == '--topcount':
    print_top(filename)
  else:
    print 'unknown option: ' + option
    sys.exit(1)

if __name__ == '__main__':
  main()
