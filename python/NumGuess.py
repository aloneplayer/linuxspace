import random
secret = random.randint(1, 50)
guess = 0
tries = 0


answer = raw_input("Lily! Do you want to play a game? (y/n)")
if answer != "y":
    exit();

print "It is a number from 1 to 50. I'll give you 6 tries. "

while guess != secret and tries < 6:
    guess = input("What's yer guess?")
    if guess<secret:
        print "Too low! "
    elif guess > secret:
         print "Too high!"
    tries = tries + 1

if guess == secret:
    print "Yes! you got it!"
else:
    print "No more guesses!"
    print "The secret number was", secret
