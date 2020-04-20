def samsfunction(x):
    return x*x

def main():

    word = "description"

    # write code here to get the length of the word, and put it in a
    # variable called "length"

    length = len(word)

    
    # write code here to take 1 letter as input and put it in a variable called "guess"
    guess=input()
    length = len(guess)
    if length == 1:
        for letter in word:
            if guess == letter:
                print(letter)#
            else:
                print("-")
    else:
        print("You cannot put more than 1 character")
        


    # write code here to print a "-" for every letter in the word, unless the letter
    # is equal to the guess, in whcih case print the letter.
    # for example, if the word is "fart" and the guess is "a", print "-a--".
    # if the guess is "x" which is not in the word, your code should print "----"

    


if __name__ == "__main__":
    main()


for z in [1, 2, 3]:
    print(z)



z=1
print(z)
z=2
print(z)
z=3
print(z)
