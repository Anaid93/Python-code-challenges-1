'''Write a function that calculates whether a 
given number is an Armstrong number.'''

def arms_number(arms_number:int): 
    # transform the number into a str
    number_str = str(arms_number)
    final_number = 0

    # the len function does not work on numbers, like int or float
    len_number = len(number_str)
    for number in number_str:        
        final_number += int(number) ** len_number    

    if final_number == arms_number:   
        return True                  
    return False

print(arms_number(91)) 
print(arms_number(371)) 