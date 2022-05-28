#the program computes the The Collatz Sequence, where by the rules defined in the
#function collatz, you can start with any integer and eventually end at 1

#function definition
def collatz(number):
    if number % 2 == 0:
        return number // 2
    else:
        return 3 * number + 1

#user input
print('Enter an integer: ')
num = int(input())

#main program loop
while True:
    result = collatz(num)
    print(result)
    num = result
    if result == 1: #if we end up at 1, break out of the loop
        break
