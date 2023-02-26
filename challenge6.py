'''Creates a program that checks if the parentheses, braces and 
square brackets of an expression are balanced.
- Balanced expression: { { [ a * ( c + d ) ] - 5 }
- Unbalanced expression: { [ [ a * ( c + d ) ] - 5 }'''

def expression(expression):        
    if expression.count('(') == expression.count(')') and expression.count('{') == expression.count('}') and expression.count('[') == expression.count(']'):
        print('Balanced expression') 
    else:
        print('Unbalanced expression')

expression('{ [ a * ( c + d ) ] - 5 }') 
expression('{ [ a * ( c + d ) ] - (5) }') 
expression('{ a * ( c + d ) ] - 5 }') 