#def Fizzbuzzer(i): #défini la fonction fizzbuzzer()
#    if i%3 == 0 and i%5 == 0:
#        return("FizzBuzz")
#    elif i%5 == 0:
#        return("Buzz")
#    elif i%3 == 0:
#        return("Fizz")
#    else:
#        return(i)


def Fizz(i):
    if i%3 == 0:

        return("Fizz")
    else:
        return(i)

def Buzz(i):
    if i%5 == 0:
        return("Buzz")
    else:
        return(i)

def Bang(i):
    if i%7 == 0:
        return("Bang")
    else:
        return(i)

def Fizzbuzzbang(i):
    concat = ""
    if Fizz(i) == "Fizz" or Buzz(i) == "Buzz" or Bang(i) =="Bang":
        if Fizz(i) == "Fizz":
            concat = Fizz(i)
        if Buzz(i) == "Buzz":
            concat = concat + "Buzz"
        if Bang(i) == "Bang":
            concat = concat + "Bang"
        return(concat)
    else:
        return (i)