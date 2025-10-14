
from fintech.timer import timer

#a@timer
def checker(s, values, validation):
    """ Populates a list 'values' with strings 'True' or 'False'  verifying 
    the string 's' by the function given by 'validation' """
		
    for item in s:
        if validation(item):
            values.append('True')
        else:
            values.append('False')
    return values    
@timer
def executor(s, values, validation):
    """ Clears the values list, applies the checker function 
    and returns the appropriate value """
		
    values.clear()
    print(True if 'True' in checker(s, values, validation) else False)

if __name__ == '__main__':
    s = input()

values = []
executor(s, values, str.isalnum)
executor(s, values, str.isalpha)
executor(s, values, str.isdigit)
executor(s, values, str.islower)
executor(s, values, str.isupper)
