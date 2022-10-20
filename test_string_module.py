import string

# print(string.digits)
# print(string.octdigits)  #8 ричная система исчисления
# print(string.hexdigits)  #16тиричная система исчисления
# print(string.ascii_uppercase)
# print(string.ascii_lowercase)
# print(string.ascii_letters)
# print(string.printable)
# print(string.punctuation)
# print(string.whitespace)

ls = [i * 10 for i in range(10)]
print(ls)

ls = [i * i for i in range(10)]
print(ls)

s = "hjvgkjsfgsdjbf"
ls = [i * 3 for i in s]
print(ls)

##############################
#найти символ из STR в s

STR = "qri"
s = "rjvgkjqfgsdjbf"
#ls = [i in STR for i in s]
ls = [0,0]
print(ls)
print(all(ls))
print(any(ls))

#all функия принимает любой итерируемый объект.
# Если все значения тру, то вернет тру. Если хотя бы один фолс, то вернет фолс
