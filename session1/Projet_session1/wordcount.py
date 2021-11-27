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

# +++your code here+++
# Define print_words(filename) and print_top(filename) functions.
# You could write a helper utility function that reads a file
# and builds and returns a word/count dict for it.
# Then print_words() and print_top() can just call the utility function.

###

# ***Début de ma solution***

def helper(filename): # fonction qui lit le fichier texte et le découpe en un liste de mots et retourne le nombre d'occurence de chaque mot du texte sous forme d'un dictionnaire
    word_counter = {}
    file = open(filename, 'r') # on ouvre le fichier 
    for line in file: # on lit chaque ligne du fichier jusque qu'il n'y en ai plus
        words = line.split() # on découpe chaque ligne en un liste de mot
        for element in words:
            element = element.lower() # on initialise chaque mot en minuscule
            if not element in word_counter:
                word_counter[element] = 1 # si l'élément n'a jamais été rencontré dans le texte alors on l'ajoute dans le dictionnaire de mots et on intialise la valeur à 1 (correspond au nombre d'occurence)
            else:
                word_counter[element] = word_counter[element] + 1
    file.close()
    return word_counter

def get_counter(word_counter_tuple):
    """Retourne le nombre d'occurence d'un mot en particulier contenu dans un fichier texte"""
    return word_counter_tuple[1]

def print_words(filename):
    """Affiche l'occurence de chaque mot contenu dans un fichier texte sous la forme d'un dictionnaire"""
    word_counter = helper(filename)
    words = sorted(word_counter.keys()) # on classe pas ordre alphabétique les mots du dictionnaire
    for element in words:
        print(element, word_counter[element]) # on affiche le mot (la clé) et son nombre d'occurence (valeur)
        
def print_top(filename):
  """Affiche les mots avec le plus grand occurence contenu dans un fihcier texte"""
  word_count = helper(filename)

  # On trie les mots de façon à ce que les grands nombres soient les premiers en utilisant la fonction key=get_count() pour extraire le nombre.
  items = sorted(word_count.items(), key=get_counter, reverse=True) # Reverse = True car par défaut la fonction sorted classe du plus petit au plus grand or nous voulons ici faire l'inverse

  # Affiche les 20 premiers mots avec la plus grande occurence
  for item in items[:20]:
    print (item[0], item[1])

        
# ***Fin de ma solution***

# print_words("C:/HUGO/Ecole/Telecom Paris/COURS/INF_721_Kit_Big_Data/google-python-exercises/basic/small.txt")
# print_top("C:/HUGO/Ecole/Telecom Paris/COURS/INF_721_Kit_Big_Data/google-python-exercises/basic/small.txt")


# This basic command line argument parsing code is provided and
# calls the print_words() and print_top() functions which you must define.
def main():
  if len(sys.argv) != 3:
    print ('usage: ./wordcount.py {--count | --topcount} file')
    sys.exit(1)

  option = sys.argv[1]
  filename = sys.argv[2]
  if option == '--count':
    print_words(filename)
  elif option == '--topcount':
    print_top(filename)
  else:
    print ('unknown option: ') + option
    sys.exit(1)

if __name__ == '__main__':
  main()