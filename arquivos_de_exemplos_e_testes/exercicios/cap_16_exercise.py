#This exercise is about creating a set of functions to perform currency conversions
#based on speciﬁed rates using currying to create those functions.
#Write a function that will curry another function and a parameter in a similar
#manner to multby in this chapter—call this function curry().
#Now deﬁne a function that can be used to convert an amount into another
#amount based on a rate. The deﬁnition of this conversion function is very straight
#forward and just involves multiplying the number by the rate.
#Now create a set of functions that can be used to convert a value in one currency
#into another currency based on a speciﬁc rate. We do not want to have to remember
#the rate, only the name of the function. For example:
#dollars_to_sterling = curry(convert, 0.77)
#print(dollars_to_sterling(5))
#euro_to_sterling = curry(convert, 0.88)
#print(euro_to_sterling(15))
#sterling_to_dollars = curry(convert, 1.3)
#print(sterling_to_dollars(7))
#sterling_to_euro = curry(convert, 1.14)
#print(sterling_to_euro(9))
#If the above code is run the output would be:
#3.85
#13.2
#9.1
#10.26
def conversion(amount, rate):
    return amount*rate

def curry(conv, rate):
    return lambda y: conv(rate, y)

dollars_to_sterling = curry(conversion, 0.77)
print(dollars_to_sterling(5))

euro_to_sterling = curry(conversion, 0.88)
print(euro_to_sterling(15))

sterling_to_dollars = curry(conversion, 1.3)
print(sterling_to_dollars(7))

sterling_to_euro = curry(conversion, 1.14)
print(sterling_to_euro(9))


