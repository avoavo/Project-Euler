# Function to solve Project Euler problem 1

def multiples_of_3_5():
    for number in range(1000):
        #print (number)
        if (number % 3) == 0  or (number % 5) == 0:
                yield (number)

print(sum(multiples_of_3_5()))