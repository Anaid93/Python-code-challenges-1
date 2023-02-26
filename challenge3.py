'''What is the most frequent word in the following paragraph?
I love teaching. If you do not love teaching what else can you love. I 
love Python if you do not love something which can give you all the 
capabilities to develop an application what else can you love.'''

from collections import Counter

def frequent_word(texto:str):
    
    # Use the method maketrans to replace '.' and ',' with a ' ' space
    string_without = texto.translate(str.maketrans(' ', ' ', '.,'))
    string_lower = string_without.lower()
    
    # Use the .split method to split the string into a list
    string_split = string_lower.split()
    
    # Pass the list of the word to instance of Counter class
    count = Counter (string_split)
    common = count.most_common(5)
    print(common)

frequent_word("I love teaching. If you do not love teaching what else can you love. I love Python if you do not love something which can give you all the capabilities to develop an application what else can you love.")