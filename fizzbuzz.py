for number in range(1,100):
    if number%3==0 and number%5==0:
        print("Fizzbuzz")
    elif number%3==0:
        print("Fizz")
    elif number%5==0:
        print("buzz")
    else:
        print(number)
