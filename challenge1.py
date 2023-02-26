'''Create a program that reverses the order of a string without 
using language functions that do it automatically.'''

# Option 1
def string_reverse(text):
    reverse_text = ''
    x = len(text)
    for idx in range(0, x):        
        reverse_text += text[x - idx - 1] 
        # the x is the len of the text (11) and idx is the position of every letter or character(from 0 to 10)
        # so 11 - 0 (the position of the firt letter - H) - 1 = 10 
        # and 10 is the position of the letter d, so this is the first character that is stored in 'reverse_text'
        # and this continue for all positions of all characters
    return reverse_text

print(string_reverse('Hello World'))


# Option 2
def inversa(reverse:str):
    #a little trick '[::-1]' to make it faster
    reverse_text = reverse[::-1]
    return reverse_text

print(inversa("Hello World"))