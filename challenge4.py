'''Clean the following text. After cleaning, count 
three most frequent words in the string.'''

# Option 1 to clean de text
sentence = '''%I $am@% a %tea@cher%, &and& I lo%#ve %tea@ching%;. There $is nothing; &as& mo@re rewarding as educa@ting &and& @emp%o@wering peo@ple. ; I found tea@ching m%o@re interesting tha@n any other %jo@bs. %Do@es thi%s mo@tivate yo@u to be a tea@cher!?'''
sentence_clean = sentence.translate({ord(i): None for i in '%@#&$;'}) 
print(sentence_clean)

# Option 2 to clean de text
sentence = "%I $am@% a %tea@cher%, &and& I lo%#ve %tea@ching%;. There $is nothing; &as& mo@re rewarding as educa@ting &and& @emp%o@wering peo@ple. ; I found tea@ching m%o@re interesting tha@n any other %jo@bs. %Do@es thi%s mo@tivate yo@u to be a tea@cher!?"
sentence_clean_2 = sentence.translate(str.maketrans(' ', ' ', '%$@&#;'))
print(sentence_clean_2)


# Use the .split method to split the string into a list
sentence_split = sentence_clean.split()

from collections import Counter
# Pass the list to instance of Counter class
counters_found = Counter(sentence_split)

# Use the .most_common() to produces n most common elements
most_common_elements = counters_found.most_common(3)
print(most_common_elements)

