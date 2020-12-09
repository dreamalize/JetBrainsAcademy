# greeting
def bot_greeting():
    print("Hello! My name is Aid.")
    print("I was created in 2020.")


bot_greeting()


# asking user's name
def with_name(name):
    print("What a great name you have, " + name + "!")


print("Please, remind me your name.")
user_name = input()
with_name(user_name)


# guessing user's age
def guess_age(x, y, z):
    return (x * 70 + y * 21 + z * 15) % 105


print("Let me guess your age.")
print("Enter remainders of dividing your age by 3, 5 and 7.")

r3 = int(input())
r5 = int(input())
r7 = int(input())

user_age = guess_age(r3, r5, r7)
print("Your age is " + str(user_age) + ": that's a good time to start programming!")


# counting from 0 to user's number
def count_to_number(number):
    counter = 0
    while counter <= number:
        print(str(counter) + " !")
        counter += 1


print("Now I will prove to you that I can count to any number you want.")

user_number = int(input())

count_to_number(user_number)


print("Let's test your programming knowledge.")
print("Why do we use methods?")
print("1. To repeat a statement multiple times.")
print("2. To decompose a program into several small subroutines.")
print("3. To determine the execution time of a program.")
print("4. To interrupt the execution of a program.")
user_answer = int(input())
while user_answer != 2:
    print("Please, try again.")
    user_answer = int(input())

if user_answer == 2:
    print("Completed, have a nice day!")

print("Congratulations, have a nice day!")
