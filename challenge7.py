'''Write a function that receives a text and returns a Boolean 
depending on whether or not they are palindromes.
A palindrome is a word or expression that is the same whether 
it is read from left to right or right to left.'''

# Option 1
def text(text):
    text_join = text.replace(' ','')
    reverse_text = ''    
    len_text = len(text_join)      
    for letter in range(0, len_text):
        reverse_text += text_join[len_text - letter - 1]     

    if text_join == reverse_text:
        return True
    else:
        return False
print(text('ana lleva al oso la avellana')) 
print(text('ana lleva al oso la avellanaa')) 


# Option 2
def text_2(text_2):
    reverse_text_2 = ''
    text_join_2 = text_2.replace(' ','')      
    for letter in text_join_2[::-1]:
        reverse_text_2 += letter
    
    if text_join_2 == reverse_text_2:
        return True
    return False         
print(text_2('a nut for a jar of tuna'))


# Option 3
def palindromo(text:str):
    text_without = text.replace(' ', '')
    reverse_text = text_without[::-1]

    if text_without == reverse_text:
        return True
    return False


print(palindromo('a nut for a jar of tuna')) 
print(palindromo('a nut for a jar of tune')) 
