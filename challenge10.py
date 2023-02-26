'''Create a function that receives a String 
of any type and and capitalizes the 
first letter of each word.'''

# Option 1
def stringg(stringg:str):
    list_word = [word[0].upper() + word[1::].lower() for word in stringg.split(" ")]

    return " ".join(list_word)

print(stringg("hello world"))
print(stringg("mOuRedEV bY brais mOUre."))
print(stringg("don't eat apples..."))


# Option 2
def string(string:str):
    mayuscula = [word.capitalize() for word in string.split()]
    total = " ".join(mayuscula)
    return total

print(string("hello wORLd"))
