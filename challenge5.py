'''Create a program that is able to transform natural text 
to morse code and vice versa. It should automatically detect 
what type it is and perform the conversion. the conversion.'''

# You can transform every character and stored in the diccionary 
dicci_morse = {
    'a':'.-',
    'h':'....',
    'o':'---',
    'l':'.-..',
    "b": "-···",
    "c": "-·-·",    
    "r": "·-·",
    " ": " "
    }

# Option 1 for transform text into morse code
def text_morse(text_morse):
    translated_phrase = ""
    for letter in text_morse.lower():
        #use .get to return the value (morse code) of the key (in this case the letter)
        letter_morse = dicci_morse.get(letter)
        if letter ==' ':
            translated_phrase += '  '
        else:
            translated_phrase += f'{letter_morse}'
    print('The text', text_morse, 'in morse code is: ', translated_phrase)

text_morse('cabra')


# Option 2 for transform text into morse code
def texto_morse(texto):
    texto_morse = ' '
    for letter in texto:
        dic = dicci_morse[letter]        
        texto_morse += dic             
    print('The text', texto, 'in morse code is: ', texto_morse)

texto_morse('hola lola')