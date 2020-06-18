def Fizzbuzzer(i): #défini la fonction fizzbuzzer()
    if i%3 == 0 and i%5 == 0:
        return("FizzBuzz")
    elif i%5 == 0:
        return("Buzz")
    elif i%3 == 0:
        return("Fizz")
    else:
        return(i)