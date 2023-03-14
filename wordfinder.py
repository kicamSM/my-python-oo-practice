"""Word Finder: finds random words from a dictionary."""

    # import os

# file = open('words.txt', 'r')
# print(file.name)
# file.close()
from random import choice

class WordFinder:

    def __init__(self, name_file):
        """initializing class which will take a file and create a empty list and call read_file method"""
        self.name_file = name_file
        self.word_list = self.read_file(name_file)
        self.read_file(name_file)
        self.print_num()
        
    def read_file(self, name_file): 
        """method opens file, reads file, returns list of words, and closes file"""
        file = open(name_file, 'r')
        lst = [word.strip() for word in file]
        file.close()
        return lst
    
    def print_num(self):
        """method prints the number of words in the list and calls the self.random()method"""
        print(f"{len(self.word_list)} words read")
        self.random()
            
    def random(self):
        """method gets a random line (in this case word because each word is on a different line and prints that word. It also allows for random() to be called afterwards and prints out an additional random word from original list)"""
        random_word = choice(self.word_list)
        print(random_word)
       
class SpecialWordFinder(WordFinder):
    
     def read_file(self, name_file):
        old_list = super().read_file(name_file)
        return [word for word in old_list if word and not word.startswith('#')]
    
        
# first_instance = WordFinder(name_file='words.txt')
# another_instance = SpecialWordFinder(name_file='words2.txt')
# another_instance.random()    
       
# class WordFinder:

#     def __init__(self, name_file):
#         """initializing class which will take a file and create a empty list and call read_file method"""
#         self.name_file = name_file
#         self.lst = []
#         self.read_file(name_file)
        
#     def read_file(self, name_file): 
#         """method opens file, reads file, takes each line of the file and counts them, returns number of lines read, calls random method and closes file"""
#         file = open(name_file, 'r')
#         for line in file:
#             line = line.strip()
#             self.lst.append(line)
#             num_words = len(self.lst)
#         print(f"{num_words} words read")
#         self.random()
#         file.close()
            
#     def random(self):
#         """method gets a random line (in this case word because each word is on a different line and prints that word. It also allows for random() to be called afterwards and prints out an additional random word from original list)"""